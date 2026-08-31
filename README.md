# Ashna's English Dollhouse

Grade 2 English practice, matched to Ashna's exam portion. A dollhouse with four
rooms — Comprehension, Grammar, Prose, Poetry — 124 questions drawn from her own
workbooks. Stars save in the browser (localStorage), so keep using the same device.

**Live:** https://codeninja1810.github.io/ashna-dollhouse/

## Stack
Single static page — no build step, no dependencies. `index.html` is the whole app.

## Vercel
- Project: `ashna-dollhouse` on team **Akiflow** (`akiflow-6412697e`)
- Project ID: `prj_ZukA7TglaRH19i4OFhjIEk3pFbO4` (linked in `.vercel/project.json`)
- Redeploy: ask Claude to redeploy this folder, or `npx vercel --prod` from here.

## Editing content
All questions live in the `ROOMS` array inside `index.html`. Each topic is
`{id, name, qs:[...]}`; questions are `{t:"mcq"|"spell", q, o?, a, why?, hint?}`.
The master copy also lives at `01-English/practice/dollhouse.html` (artifact
version) — keep the two in sync when adding units.
