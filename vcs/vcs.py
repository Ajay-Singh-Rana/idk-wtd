# h3avren

import argparse

parser = argparse.ArgumentParser()

# adding positional arguments
parser.add_argument("init", help = "Initialize the specidied directory or "\
                                   " this directory as version controlled..!")


args = parser.parse_args()

print(args.init)
