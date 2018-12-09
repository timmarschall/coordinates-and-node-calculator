# coordinates-and-node-calculator
a simple littly python program to caclulate grid coordinates and their connections

I got a set of data that didn't make any sense. It was supposed to simply show the coordinates and their connections in a simple square grid... but somehow the data wasn't written in a logical order (i.e. left to right then bottom to top).

So I made this little program to figure out what was going on and to write the data both in logical and "dumb" order

# logical order

Coordinates are calculated starting at the bottom left point (0,0) and then move along the x-axis, then go a step up the y-axis and continue (left to right, bottom to top).

# "dumb" order

Coordinates go left to right *except* for the last points on the x-axis. Also the top axis is calculated after those.

So we go bottom left to top right, not calculating the last column. We also stop at the second to last row.

Then we calculate all the points on the end of the x-axis bottom to top, except the very top corner.

Then we calculate the the top row, excluding the left corner and the right corner.

We add those at the end.

# Nodes
Nodes in either case are calculated counterclockwise:

Left bottom -> right bottom -> right top -> left top

They are written as the numbered notes they connect.

It was a fun little project to help understand the data and to brush up on python.

# License

MIT license so you can almost do whatever you want with it. have fun.


Copyright (c) 2018 Tim Marschall

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
