# CS561: ASCIILines  
Copyright (c) 2019 Matthew Geary  
  
## Description  
Asciilines builds and renders a canvas from a .tvg  
(Text Vector Graphics) file using ascii characters  
on stdout.  
The file to use is given to the program via stdin.  
  
## Usage  
$ python asciilines.py <tvg-file-path>  

## TVG Format
Information on TVG Format drawn from  
https://moodle.cs.pdx.edu/mod/assign/view.php?id=114  
  
A "TVG" file contains "Text Vector Graphics".  
  
The first line of the file contains the "canvas size":  
the number of rows and columns of text to output (both  
must be greater than zero). The canvas starts out filled  
with . characters.  
  
The rest of the file is rendering commands, one per line.  
  
A rendering command is a line containing:  
* A character to render with  
* A row position to start at (0-based)  
* A column position to start at (0-based)  
* Either h for a horizontal line or v for a vertical line.  
* A length for the rendered line (must be greater than 0)  
  
The elements of the command should be separated by a single space.  
  
The character positions that are part of the rendering command's  
rendered line should be filled with the rendering character.  
It is legal for the line to extend outside the canvas. There is   
no wraparound: only points inside the canvas should be rendered,  
others should be ignored.  
  
Example: a TVG file containing  
  
3 4  
* 1 -1 h 5  
# -1 1 v 5  
  
should render as  
  
.#..  
*#**  
.#..  
  
## License  
  
This program is licensed under the "MIT License". Please  
see the file `LICENSE` in the source distribution of this  
software for license terms.  
