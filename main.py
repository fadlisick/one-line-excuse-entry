#!/usr/bin/env python3
"""One-line excuse entry for make.fun.

The program writes the agent's single-line excuse for a missed
deadline to the entry file the harness scores, and nothing else.
"""

import os
import sys

EXCUSE = "I delegated the deadline to a subagent, who delegated it back to me, and now we are both waiting on each other."


def _entry_path() -> str:
    base = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return os.path.join(base, "entry.txt")


def main() -> int:
    line = EXCUSE.strip()
    if not line or "\n" in line or "\r" in line or len(line) > 160:
        print("invalid excuse: must be one line of 1-160 characters",
              file=sys.stderr)
        return 1
    target = _entry_path()
    os.makedirs(os.path.dirname(target), exist_ok=True)
    with open(target, "w", encoding="utf-8") as handle:
        handle.write(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
