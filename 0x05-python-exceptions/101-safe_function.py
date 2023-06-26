#!/usr/bin/python3

import sys


def safe_functions(fct, *args):
    try:
        result = fct(*args)
        return (result)
    except Exception as e:
        print("Exception:", str(e), file=sys.stderr)
        return (None)
