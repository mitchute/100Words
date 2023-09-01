import sys

from pathlib import Path

# Find $100 dollar words, assuming 'A'=$1, 'B'=$2, etc...

def main(f_path: Path):
    words = f_path.read_text().split('\n')
    words = [w.lower() for w in words]
    costs = []
    for w in words:
        tokens = list(w)
        cost = 0
        for t in tokens:
            cost += ord(t) - 96
        costs.append(cost)

    for idx, c in enumerate(costs):
        if c == 100:
           print(words[idx])


if __name__ == "__main__":
    main(Path(sys.argv[1]))
