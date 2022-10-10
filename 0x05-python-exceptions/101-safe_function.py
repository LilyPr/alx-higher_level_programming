#!/usr/bin/python3
import sy


def safe_function(fct, *args):
    try:
        return fct(*args)
    except Exception as ex:
        print("Exception: {}".format(ex), file=sys.stderr)
        return Nones
