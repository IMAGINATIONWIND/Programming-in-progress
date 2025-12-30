import argparse

parser = argparse.ArgumentParser()

parser.add_argument("name")
parser.add_argument("-r", "--repeat", type=int, default=1)

args = parser.parse_args()

for _ in range(args.repeat):
    print(f"Hello, {args.name}!")
