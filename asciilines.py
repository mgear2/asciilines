# Copyright © 2019 Matthew Geary
# [This program is licensed under the "MIT License"]
# Please see the file LICENSE in the source
# distribution of this software for license terms.

import sys

class Canvas():
  def __init__(self):
    self.FORMAT_ERROR = "Data file error: incorrect formatting, please verify...\n"

  def init(self, filename):
    # https://stackoverflow.com/questions/3277503/how-to-read-a-file-line-by-line-into-a-list#3277516
    data = [line.rstrip('\n') for line in open(filename)]
    self.data = data
    print(data)
    rows = int(data[0][0])
    columns = int(data[0][2])
    # https://stackoverflow.com/questions/2397141/how-to-initialize-a-two-dimensional-array-in-python#2397192
    canvas = [["." for y in range(rows+1)] for x in range(columns+1)]
    self.canvas = canvas
    # https://stackoverflow.com/questions/10713004/find-length-of-2d-array-python#10713016
    self.x = len(canvas)-1
    self.y = len(canvas[0])-1

  def build(self):
    for index, line in enumerate(self.data):
      if index == 0:
        continue
      lnlst = line.split(" ")
      to_render = lnlst[0]
      if lnlst[3] == "h":
        for i in range(0, self.x):
          self.canvas[int(lnlst[1])][i] = to_render
      elif lnlst[3] == "v":
        for i in range(0, self.y):
          self.canvas[i][int(lnlst[2])] = to_render
      else:
        sys.stderr.write(FORMAT_ERROR)

  def prnt(self):
    for i in range(0,self.y):
      for j in range(0,self.x):
        sys.stdout.write(self.canvas[i][j])
      print("\n")

if __name__ == "__main__":
  usage = "asciilines.py <tvg-file-path>"
  if len(sys.argv) != 2:
    print(usage)
  else:
    canvas = Canvas()
    canvas.init(sys.argv[1])
    canvas.build()
    canvas.prnt()
