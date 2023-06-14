import sys


def build_args(argv):

    try:
        args = argv[1:]
    except IndexError:
        args = []
    return args


def check_args(args):

    if len(args) > 1:
        raise IndexError(
            "Two arguments are passed to fvpy. Continuing with first argument."
        )
    return args[0:1]


def main():

    args = check_args(build_args(sys.argv))

    from fvpy import application as app

    return app.run(args)
