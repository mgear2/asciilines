# Copyright © 2019 Matthew Geary
# [This program is licensed under the "MIT License"]
# Please see the file LICENSE in the source
# distribution of this software for license terms.

import sys

class Canvas():
    """ Canvas class used to build and render a canvas from a tvg file """

    def __init__(self):
        self.FORMAT_ERROR = "Data file error: incorrect formatting, please verify...\n"

    def read(self, filename):
        """ Method to read the tvg file and initialize a blank canvas of correct size """
    
        # https://stackoverflow.com/questions/3277503/how-to-read-a-file-line-by-line-into-a-list#3277516
        self.data = [line.rstrip('\n') for line in open(filename)]
        size = self.data[0].split(" ")
        rows = int(size[0])
        columns = int(size[1])
        # https://stackoverflow.com/questions/2397141/how-to-initialize-a-two-dimensional-array-in-python#2397192
        self.canvas = [["." for y in range(columns+1)] for x in range(rows+1)]
        # https://stackoverflow.com/questions/10713004/find-length-of-2d-array-python#10713016
        self.y = len(self.canvas)-1
        self.x = len(self.canvas[0])-1

    def alter(self, hflag, line_len, primary, secondary, coord, to_render):
        """ Method used to alter a single line of the canvas based on tvg data"""

        if line_len + primary > coord:
            line_len = coord
        else:
            line_len = line_len + primary
        for i in range(primary, line_len):
            if hflag:
                self.canvas[secondary][i] = to_render
            else:
                self.canvas[i][secondary] = to_render

    def parse(self):
        """ Method to parse tvg data and call alter() on each line """

        for index, line in enumerate(self.data):
            if index == 0:
                continue
            lnlst = line.split(" ")
            to_render = lnlst[0]
            row_pos = int(lnlst[1])
            col_pos = int(lnlst[2])
            line_dir = lnlst[3]
            line_len = int(lnlst[4])
            if line_dir == "h":
                self.alter(True, line_len, col_pos, row_pos, self.x, to_render)
            elif line_dir == "v":
                self.alter(False, line_len, row_pos, col_pos, self.y, to_render)
            else:
                sys.stderr.write(FORMAT_ERROR)

    def render(self):
        """ Method to render the canvas to the command line """

        for i in range(0,self.y):
            for j in range(0,self.x):
                sys.stdout.write(self.canvas[i][j])
            sys.stdout.write("\n")

if __name__ == "__main__":
    usage = "python asciilines.py <tvg-file-path>"
    if len(sys.argv) != 2:
        print(usage)
    else:
        filename = sys.argv[1]
        canvas = Canvas()
        canvas.read(filename)
        canvas.parse()
        canvas.render()
