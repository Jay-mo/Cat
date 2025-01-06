import sys
from pathlib import Path
import argparse

parser = argparse.ArgumentParser(prog="pycat")
parser.add_argument("file",nargs="*", help="The file(s) that you want to print to stdout")
parser.add_argument("-b",action="store_true", help="Print non-blank output lines, starting at 1.")
parser.add_argument("-e", action="store_true", help="Display non-printing characters (see the -v option), \
                    and display a dollar sign (‘$’) at the end of each line.")
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
            if args.b and args.e:
                line_count = 1
                for line in file:
                    if line == "\n":
                        continue
                    # print(f"{line_count:>5} {line}$")
                    print(f"{line_count:>6}  " + line.rstrip('\n') + '$')
                    line_count+=1
            elif args.b:
                line_count = 1
                for line in file:
                    if line == "\n":
                        continue
                    print(f"{line_count:>5} {line}",end="")
                    line_count+=1
            elif args.e:
                for line in file:
                    # if line.endswith('\n'):
                    #     line.replace('\n','$')      
                    if line == "\n" or line == " ":
                        continue
                    #print(f"{line} yaaaa",end="$")
                    print(line.rstrip('\n') + '$')


            print(file.read())


