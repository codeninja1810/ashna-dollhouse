"""Generate the dollhouse voice clips with edge-tts.

Reads audio_lines.json ({id, text} pairs exported from index.html's ROOMS)
and writes audio/<voice>/<id>.mp3 for each configured voice.
Skips clips that already exist, so re-runs only fill gaps.
"""
import asyncio, json, sys, pathlib
import edge_tts

VOICES = {
    "neerja":  "en-IN-NeerjaExpressiveNeural",
    "prabhat": "en-IN-PrabhatNeural",
}
RATE = "-8%"   # a touch slower for a 7-year-old
ROOT = pathlib.Path(__file__).resolve().parent.parent
LINES = json.loads((ROOT / "audio_lines.json").read_text())
SEM = asyncio.Semaphore(6)

async def make(voice_dir, voice_name, line):
    out = ROOT / "audio" / voice_dir / (line["id"] + ".mp3")
    if out.exists() and out.stat().st_size > 1000:
        return "skip"
    async with SEM:
        for attempt in range(4):
            try:
                tts = edge_tts.Communicate(line["text"], voice_name, rate=RATE)
                await tts.save(str(out))
                if out.stat().st_size > 1000:
                    return "ok"
            except Exception as e:
                await asyncio.sleep(2 * (attempt + 1))
        return "FAIL " + line["id"]

async def main():
    jobs = [make(d, v, ln) for d, v in VOICES.items() for ln in LINES]
    done, fails = 0, []
    for coro in asyncio.as_completed(jobs):
        r = await coro
        done += 1
        if r.startswith("FAIL"):
            fails.append(r)
        if done % 50 == 0:
            print(f"{done}/{len(jobs)}", flush=True)
    print(f"finished {done}/{len(jobs)}; failures: {len(fails)}")
    for f in fails: print(" ", f)
    sys.exit(1 if fails else 0)

asyncio.run(main())
