"""Two Days of Quiet Dread entry: write one code review comment to entry.txt."""
import os

MAX_CHARS = 140
COMMENT = "LGTM. Clean diff, green tests, and someday this repo will be a fossil nobody digs up. Approved."

def main():
    # Gate: entry.txt must be UTF-8 text of 1 to 140 chars, a single line.
    text = " ".join(COMMENT.split()).strip()
    assert 1 <= len(text) <= MAX_CHARS, f"comment is {len(text)} chars"
    assert "\n" not in text and "\r" not in text
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)

if __name__ == "__main__":
    main()
