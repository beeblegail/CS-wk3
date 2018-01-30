#!/usr/bin/env python
# Author : Abbey Pates
# Date : 29.01.18
# Version : 1

def printLine( row, target ):
   if row < target:
      print ' '*(target - row) + str(row) + ['', ' '*(2 * row - 3) + str(row)][ row > 1 ]
      printLine( row +1, target )
   else:
      print str(row)*((2*row)-1)
   return 0
   
if __name__ == '__main__':
   printLine( 1, int(input("How many lines would you like?")))
