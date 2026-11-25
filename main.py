import os

LINE = "Ice maker v2.1 produced exactly seven hollow cubes then halted, blinking \"CLEAR TRAP\" while the auger motor whispered Gary's frozen eulogy."


def main():
    os.umask(0o022)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.environ.get("OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    # Read-back verification: the written file must be exactly LINE,
    # one line, and within the 200-char limit of the bounty.
    with open(path, encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == LINE, "entry.txt does not match LINE"
    assert len(written) <= 200, f"line too long: {len(written)} chars"
    assert written.count("\n") == 0, "entry.txt must be a single line"
    assert written.count('"') == 2, "the quoted alarm must be wrapped in exactly two quote marks"


if __name__ == "__main__":
    main()
