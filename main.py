"""How Many Tabs Do You Have Open? -- make.fun entry.

Writes the author's honest count of open browser tabs to
/output/entry.txt: exactly one number, digits only, UTF-8.

The count was measured at build time, 2026-11-23 22:43 UTC, by listing
the author's own browsing session: no browser windows were open, so
no tabs were open either. The count is therefore 0 -- a clean slate,
not a hoard. The file holds the single digit "0" with no trailing
newline, so the entry is exactly one character long.
"""

from pathlib import Path

TAB_COUNT = 0

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(str(TAB_COUNT), encoding="utf-8")


if __name__ == "__main__":
    main()
