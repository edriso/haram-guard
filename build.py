#!/usr/bin/env python3
"""Generate skills/haram-guard/SKILL.md from GUIDE.md.

Installing copies the skill file out of this repo and away from GUIDE.md, so it has to
be self-contained. Self-contained means duplicated, and duplicated drifts. So it is
generated, and --check fails when the committed copy no longer matches GUIDE.md.

    python3 build.py            # write the skill
    python3 build.py --check    # exit 1 if stale

Stdlib only.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "GUIDE.md")
OUT = os.path.join(HERE, "skills", "haram-guard", "SKILL.md")

FRONTMATTER = """---
name: haram-guard
description: >-
  Check whether a task is work the user should take on, against their stated ethical
  boundary (Islamic halal/haram rules, or any conscience line they have set). Use when a
  task involves lending, interest, APR, credit or financing; gambling, betting, prize
  draws or loot boxes; alcohol, tobacco or other intoxicants; adult or immodest content;
  devotional or religious objects; deceptive commerce such as hidden fees, fake scarcity,
  fake reviews or dark patterns; or tracking and engagement mechanics built to be hard to
  leave. Also use when asked "should I build this", "is this halal", "is this haram",
  when asked to review a plan, spec, branch or contract against that boundary, or when
  the user seems uneasy about a task without saying why. It raises the question and
  reasons it through; it never decides for the user.
---
"""

NOTE = (
    "<!-- Generated from GUIDE.md by build.py in github.com/edriso/haram-guard."
    " Edit there, not here. -->\n"
)


def render():
    guide = open(SRC, encoding="utf-8").read().strip()
    return FRONTMATTER + NOTE + "\n" + guide + "\n"


def main():
    content = render()
    if "--check" in sys.argv:
        if not os.path.exists(OUT):
            sys.exit(f"{OUT} is missing. Run: python3 build.py")
        if open(OUT, encoding="utf-8").read() != content:
            sys.exit("skills/haram-guard/SKILL.md is STALE vs GUIDE.md. Run: python3 build.py")
        print("CHECK OK. The skill matches GUIDE.md.")
        return
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as fh:
        fh.write(content)
    print(f"wrote {os.path.relpath(OUT, HERE)} ({len(content)} bytes)")


if __name__ == "__main__":
    main()
