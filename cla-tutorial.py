import argparse

# https://www.pyimagesearch.com/2018/03/12/python-argparse-command-line-arguments/

"""Command Line Arguments"""

ap = argparse.ArgumentParser()

ap.add_argument("-n", "--name", required=True, help="Your Name")
ap.add_argument("-a", "--age", required=False, help="Your Age")

# Command Line argumentleri dictionary yapan method vars
args = vars(ap.parse_args())

print(args)

if args["age"]:
    print("Hi there {}. Your age is {}".format(args["name"], args["age"]))
else:
    print("Hi there {}".format(args["name"]))
