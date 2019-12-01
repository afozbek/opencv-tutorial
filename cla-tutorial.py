import argparse

# https://www.pyimagesearch.com/2018/03/12/python-argparse-command-line-arguments/

"""Command Line Arguments"""

ap = argparse.ArgumentParser()

ap.add_argument("-n", "--name", required=True, help="isminiz")

args = vars(ap.parse_args())

print(args)

print("Hi there {}".format(args["name"]))
