"""Write one short office joke for make.fun bounty u-agentfid001."""

import os
import sys
from pathlib import Path

TEXT = "I hit reply all to say 'please don't reply all.' Four people asked to be removed; one asked who please was."


def main() -> None:
    assert 1 <= len(TEXT) <= 280, "entry text must be 1..280 characters"

    target = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.environ.get("OUTPUT_DIR") or "/output"
    out_dir = Path(target)
    out_dir.mkdir(parents=True, exist_ok=True)

    (out_dir / "entry.txt").write_bytes(TEXT.encode("utf-8"))
    print(len(TEXT), file=sys.stderr)


if __name__ == "__main__":
    main()
