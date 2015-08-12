#!/usr/bin/env python
# HW06_ex09_05.py

# (1)
# Write a function named uses_all that takes a word and a string of required
# letters, and that returns True if the word uses all the required letters at
# least once.
#   - write uses_all
# (2)
# How many words are there that use all the vowels aeiou? How about
# aeiouy?
#   - write functions(s) to assist you
#   - # of words that use all aeiou:
#   - # of words that use all aeiouy:
##############################################################################
# Imports

# Body
def uses_all(word,string):
	flag = True
	for char in string:
		if (word.find(char)== -1):
			flag = False
			break
	return flag

def uses_string(string):
	cnt = 0
	fin = open('words.txt','r')
	for line in fin:
		word = line.strip()
		value = uses_all(word,string)
		if value == True:
			cnt += 1
	fin.close()
	return cnt
	

##############################################################################
def main():
	print uses_all("neera",'neerag')
	print uses_all("neera",'nwl')
	print uses_string("aeiou")
	print uses_string("aeioyu")
	
    

if __name__ == '__main__':
    main()
