import sys
from pathlib import Path
import argparse





parser = argparse.ArgumentParser(prog="pycat")
parser.add_argument("file",nargs="*")
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

    # fileNames = sys.argv[1:]


    # for file in fileNames:
    for file in args.file:
        p = Path(file)

        try:
            fileName = p.resolve(strict=True)
        except FileNotFoundError:
            print(f"{sys.argv[0]}: {file}: No such file or directory exist")
            sys.exit(1)



        with open(fileName,"r") as file:
            print(file.read())


