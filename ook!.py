"""
Interpreter Ook!.
===========

| Character         | Meaning                                                                                     |
|-------------------|---------------------------------------------------------------------------------------------|
|     Ook. Ook.     | increment the data pointer (to point to the next cell to the right).                        |
|     Ook! Ook!     | decrement the data pointer (to point to the next cell to the left).                         |
|     Ook. Ook?     | increment (increase by one) the byte at the data pointer.                                   |
|     Ook? Ook.     | decrement (decrease by one) the byte at the data pointer.                                   |
|     Ook! Ook.     | output the byte at the data pointer.                                                        |
|     Ook. Ook!     | accept one byte of input, storing its value in the byte at the data pointer.                |
|     Ook! Ook?     | if the byte at the data pointer is zero, then instead of moving the instruction pointer forward
                      to the next command, jump it forward to the command after the matching ] command.      |
|     Ook? Ook!     | if the byte at the data pointer is nonzero, then instead of moving the instruction pointer
                      forward to the,next command, jump it back to the command after the matching [ command.      |
"""

from collections import defaultdict
import sys
import argparse
import re


__author__ = 'ipetrash'
output=[]


def get_loops_block(source):
    begin_block = []
    blocks = {}
    i = 0
    words = re.findall("Ook[.?!] Ook[.?!]", source)
    l = len(words)  # Number of code symbols
    while i < l:
        s = words[i]
        if s == 'Ook! Ook?':
            begin_block.append(i)
        elif s == 'Ook? Ook!':
            b_i = begin_block.pop()  # b_i -- begin index
            blocks[i] = b_i
            blocks[b_i] = i
        i += 1
    return blocks


def execute(source):
    """
    EN:
    The function parses source code Ook! and execute it.
    :param source:
    :return:
    """

    i = 0  # A pointer to the row index in the code
    x = 0  # Cell index
    ook = defaultdict(int)  # Dictionary, which is stored in the key index of the cell, and in the value - its value
    words = re.findall("Ook[.?!] Ook[.?!]", source)
    l = len(words)  # Number of code symbols
    loops_block = get_loops_block(source)

    while i < l:
        s = words[i]
        if s == 'Ook. Ook?':  # Go to the next cell
            x += 1
        elif s == 'Ook? Ook.':  # Go to the previous cell
            x -= 1
        elif s == 'Ook. Ook.':  # Increasing the value of the current cell on 1
            ook[x] += 1
        elif s == 'Ook! Ook!':  # Decrease the value of the current cell on 1
            ook[x] -= 1
        elif s == 'Ook! Ook.':  # Printing the value of the current cell
            output.append(chr(ook[x]))
        elif s == 'Ook. Ook!':  # Enter a value in the current cell
            ook[x] = int(input("Input = "))
        elif s == 'Ook! Ook?':  # Begin loop
            if not ook[x]:  # If bf[x] == 0, then gets the index of the closing parenthesis
                i = loops_block[i]
        elif s == 'Ook? Ook!':  # End loop
            if ook[x]:  # bf[x] != 0, then gets the index of the opening parenthesis
                i = loops_block[i]
        i += 1


def create_parser():
    parser = argparse.ArgumentParser(description='Interpreter language Ook!.')
    parser.add_argument("path", help="Path to file")
    return parser


if __name__ == '__main__':
    parser = create_parser()

    if len(sys.argv) is 1:
        parser.print_help()
    else:
        args = parser.parse_args()
        file_name = args.path
        source = open(file_name).read()
        execute(source)

print '[%s]' % ''.join(map(str, output))