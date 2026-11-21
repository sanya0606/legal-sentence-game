import sys
from app.core import milestone_2, milestone_4


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    print("Legal Sentence Game is ready.")
    if argv:  # e.g. python -m app.cli either  -> prints a next-word hint
        print("Next-word hint:", milestone_2(argv[-1]))
        return
    milestone_4()  # no arguments: play the game


if __name__ == "__main__":
    main()