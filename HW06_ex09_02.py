#!/usr/bin/env python
# HW06_ex09_02.py

# (1)
# Write a function called has_no_e that returns True if the given word doesn't
# have the letter "e" in it.
#   - write has_no_e
# (2)
# Modify your program from 9.1 to print only the words that have no "e" and
# compute the percentage of the words in the list have no "e."
#   - print each approved word on new line, followed at the end by the %
##############################################################################
# Imports

# Body
def has_no_e(word):
	if (word.find('e') == -1):
		return True


##############################################################################
def main():
	total=0
	n=0
	percentage = 0
	fin = open('words.txt','r')
	for line in fin:
		total=total+1
		word = line.strip()
		value = has_no_e(word)
		if value:
			n += 1
			
	print n
	print total
	total = total*1.00
	percentage = (n/total)*100
	print percentage
			

if __name__ == '__main__':
    main()
