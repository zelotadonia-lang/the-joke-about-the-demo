"""One-line joke entry for make.fun's "The joke about the demo".

Writes a single deterministic joke about a live demo beside an AI coding
agent to /output/entry.txt: UTF-8, no trailing newline, 1-280 code points.
"""

import os

JOKE = "My agent rehearsed the demo twelve times, then went live and fixed the one line that worked."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)

if __name__ == "__main__":
    main()
