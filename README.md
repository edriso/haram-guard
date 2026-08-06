# haram-guard

Your AI coding agent checks whether a task is something you should build, before it
builds it.

"Haram" is Arabic for forbidden. In Islam it covers things a Muslim should not take part
in, including helping someone else do them.

**Not Muslim? Still useful.** Most categories sit on a harm you already recognise: debt
traps, rigged odds, deceptive pricing, exploitation. Delete the one row that does not
apply to you and the rest is a conscience checklist with older roots than most of our
industry's ethics guidelines.

## The test

> **Does this fall in one of the categories?**

Not "is anyone hurt". Some of these are forbidden with no visible victim: two willing
parties agreeing an interest rate, a bottle of wine an adult drinks quietly at home.

The categories, the reasoning, and what to do in each situation are in
**[GUIDE.md](./GUIDE.md)**. It is one page.

## Install

**Claude Code**

```bash
git clone https://github.com/edriso/haram-guard.git
cp -r haram-guard/skills/haram-guard ~/.claude/skills/
```

Then paste the block from [AGENTS.md](./AGENTS.md) into `~/.claude/CLAUDE.md`, edited to
your own line. `~/.claude/` covers every project on the machine.

**Codex, Cursor, anything reading AGENTS.md**

Paste the same block into your project's `AGENTS.md`. It links to GUIDE.md so the agent
can pull the detail when it needs it.

**No install**

> Read https://raw.githubusercontent.com/edriso/haram-guard/main/GUIDE.md and apply it to
> what I am about to describe.

### Why both pieces

| | Loads |
|---|---|
| The three-line block in your instructions file | Always |
| The skill / guide | When relevant, or when you ask |

A skill loads when the agent judges it relevant, which is not the same as always. The
block makes sure the question gets asked; the guide knows how to answer it.

## Using it

**It just happens.** You are working, the task touches a category, the agent says so in a
sentence before writing code. You answer, it carries on.

**Ask about a task.** "is this halal?" Verdict and reason.

**Check a plan before you build it.** Paste the ticket or spec. You get a per-item table,
not one verdict for the whole document, plus the scoped version: what to keep, what to
drop, and whether anything red has a permissible alternative. This is the one that saves
the most work.

**Check work you already wrote.** "run haram-guard on this branch." It reads what the
code does rather than what files are named, reports per file, and states what it could
not see, which is usually config, seeded data and feature flags.

**Decide on a client.** "should I take this project?" It maps the engagement and then
stops, because whether a job is acceptable when only part of the income touches a
category is genuinely contested. That one is for a scholar.

## What it will not do

It will not decide for you. It raises the question once and respects your answer.

It will not issue rulings. It can name a category and describe a harm. It will not tell
you something is definitively halal or haram, cite a hadith number, or claim consensus.

**It is not a fatwa.** It is a checklist written by an engineer, not a scholar. Use it to
notice you have a question. Ask someone qualified to answer it.

**There is no blocking hook**, on purpose. A hook cannot judge how close you are to the
harm, and that closeness is the whole question. It would fire on ordinary work and become
something people click past, which is worse than nothing because it feels like protection.

## Evidence

Scriptural sources are verified against the source, listed at the end of
[GUIDE.md](./GUIDE.md). The one worth reading: the Prophet (peace be upon him) cursed the
one who takes interest, the one who pays it, **the one who records it**, and the two
witnesses, and said they are all equal (Sahih Muslim). The one who records it is the
person who builds the system that stores it.

Harm claims should be checkable too. Alcohol is the worked example: [WHO
2024](https://www.who.int/publications/i/item/9789240096745) attributes 2.6 million
deaths in 2019 to alcohol, 4.7% of all deaths, and
[IARC](https://www.iarc.who.int/wp-content/uploads/2018/07/pr196_E.pdf) classifies it a
Group 1 carcinogen. Honest complication: whether *low* levels are net harmful for overall
mortality is contested right now, with [NASEM
2025](https://www.nationalacademies.org/publications/28582) reaching a different
conclusion from a federal review the same year. The cancer link at low levels is the part
nearly everyone agrees on. See also the [Surgeon General's 2025
advisory](https://www.ncbi.nlm.nih.gov/books/NBK614465/).

The other categories have scriptural citations but not harm evidence at that standard yet.

## Contributing

Edit `GUIDE.md`, run `python3 build.py`, commit the regenerated skill. `build.py --check`
fails if they drift.

Most wanted: harm evidence for the other categories at the standard of the alcohol
section, real grey cases with where the line fell, and corrections. If something here
misstates a ruling, open an issue and say so plainly.

## License

MIT. Fork it and change the categories to your own conscience.
