# Copyright © 2019 Matthew Geary
# [This program is licensed under the "MIT License"]
# Please see the file LICENSE in the source
# distribution of this software for license terms.

import sys

def tests1to5():
    """ Method to run tests 1 through 5 """

    filenames = [
        "tests/test1.tvg",
        "tests/test2.tvg",
        "tests/test3.tvg",
        "tests/test4.tvg",
        "tests/test5.tvg"
        ]

    from asciilines import Canvas
    canvas = Canvas()
    for filename in filenames:
        sys.stdout.write("\n")
        canvas.read(filename)
        canvas.parse()
        canvas.render()
