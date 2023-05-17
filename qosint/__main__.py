#!/usr/bin/python3

# These few lines of code is from the sherlock project

import sys

if __name__ == "__main__":
    # Check if the user is using the correct version of Python
    python_version = sys.version.split()[0]

    if sys.version_info < (3, 6):
        print("QOSINT requires Python 3.6+, but you are using Python %s, which is not supported by QOSINT" % (python_version))
        sys.exit(1)

    