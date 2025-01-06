import sys
from pathlib import Path
import argparse

parser = argparse.ArgumentParser(prog="pycat")
parser.add_argument("file",nargs="*", help="The file(s) that you want to print to stdout")
parser.add_argument("-b",action="store_true", help="Print non-blank output lines, starting at 1.")
args = parser.parse_args()


if len(sys.argv) <2:
    try:
        while(True):
            userInput = input()
            print(userInput)
    except KeyboardInterrupt:
        print("\nClosing for now.")
        sys.exit(0)
else:
    for file in args.file:
        p = Path(file)
        try:
            fileName = p.resolve(strict=True)
        except FileNotFoundError:
            print(f"{sys.argv[0]}: {file}: No such file or directory exist")
            continue

        with open(fileName,"r") as file:
            if args.b:
                line_count = 1
                for line in file:
                    if line == "\n":
                        continue
                    print(f"{line_count:>5} {line}")
                    line_count+=1
            print(file.read())


