# Generates a list L of random nonnegative integers at most equal to some value
# input by the user, and of length also input by the user, and outputs a list
# consisting of the longest streak of consecutive occurrences of the same value in L,
# possibly looping around (as if the list was a ring). In the case multiple value
# have the longest streak of consecutive occurrences in L, then the smallest value is chosen.
#
# Written by *** and Eric Martin for COMP9021


import sys
from random import seed, randint


try:
    arg_for_seed, length, max_value = input('Enter three nonnegative integers: ').split()
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    arg_for_seed, length, max_value = int(arg_for_seed), int(length), int(max_value)
    if arg_for_seed < 0 or length < 0 or max_value < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(arg_for_seed)
L = [randint(0, max_value) for _ in range(length)]
print('\nThe generated list is:')
print('  ', L)

R = L
# Insert your code here
len1=1 #current length
max1=1 #longest length
H=max_value # if length is the same,to choose the smallest list
j=0 #tag to distinguish whether the list is like [2,2],
R=[]
for i in range(-len(L),len(L)-1):
	if L[i]==L[i+1]:
		len1=len1+1
	else:
		if len1 >max1:
			max1 = len1
			H=L[i]
		elif len1== max1:
			if L[i]<=H:
				H=L[i]
		len1=1
		j=1	
if L==[]:
	R=[]
else:
	if j==0:
		for i in range(0,len(L)):
			R.append(L[i])
	else:
		for i in range(0,max1):
			R.append(H)
#######################################
print('\nThe longest streak of the same value is:')
print('  ', R)
