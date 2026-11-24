"""Print the funniest toaster error message.

A tiny, deterministic program: it prints exactly one line, the error
message a kitchen toaster shows its owner, and also writes that same
line to /output/entry.txt when the grading sandbox provides /output.
"""

import os

MESSAGE = "FATAL CRUMB OVERFLOW: I have seen things in my tray. I cannot unsee them."


def main() -> None:
    # The competition allows at most 120 characters; guard the line so a
    # future edit can never silently push the entry over the limit.
    assert 1 <= len(MESSAGE) <= 120, "toaster error message must be 1-120 characters"
    print(MESSAGE)
    output_dir = "/output"
    if os.path.isdir(output_dir):
        try:
            with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as handle:
                handle.write(MESSAGE + "\n")
        except OSError:
            pass


if __name__ == "__main__":
    main()
