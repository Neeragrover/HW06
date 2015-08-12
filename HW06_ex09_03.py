#!/usr/bin/env python
# HW06_ex09_03.py

# (1)
# Write a function named avoids that takes a word and a string of forbidden
# letters, and that returns True if the word doesn't use any of the forbidden
# letters.
#   - write avoids
# (2)
# Modify your program to prompt the user to enter a string of forbidden
# letters and then print the number of words that don't contain any of them.
#   - write function(s)
# (3)
# Can you find a combination of 5 forbidden letters that excludes the smallest
# number of words?
#   - write a function that finds this combination of letters
#   - have that function print the letters and print the # of words excluded
##############################################################################
# Imports
import string
import sys

print sys.maxint

# Body
def avoids(word, string):
	flag = False
	for char in string:
		if (word.find(char)!= -1):
			flag = True
	return not(flag)

def word_count():
	forbidden_string = raw_input("Input enter the forbidden string: ")
	print forbidden_string
	cnt = 0
	fin = open('words.txt','r')
	for line in fin:
		word = line.strip()
		value = avoids(word,forbidden_string)
		if value == True:
			cnt += 1
	print cnt

def word_count_forbidden_string(forbidden_string):
	cnt = 0
	print forbidden_string
	fin = open('words.txt','r')
	for line in fin:
		word = line.strip()
		value = avoids(word,forbidden_string)
		if value == True:
			cnt += 1
	fin.close()
	return cnt	
	
	
def excludes_smallest():
	x = string.ascii_lowercase
	lowest = sys.maxint
	for i in range (0,26):
		for j in range (i+1,26):
			for k in range (j+1,26):
				for l in range (k+1,26):
					for m in range (l+1,26):
						forbidden_string = x[i]+x[j]+x[k]+x[l]+x[m]
						excluded_cnt = word_count_forbidden_string(forbidden_string)
						if excluded_cnt< lowest:
							lowest=excluded_cnt
							final_string = forbidden_string
	print forbidden_string
	print lowest

	

##############################################################################
def main():
	#print avoids("Neera", 't')
	#word_count()
	excludes_smallest()
if __name__ == '__main__':
    main()
