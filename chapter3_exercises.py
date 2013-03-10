# Exercises for chapter 3: Problems 3.1, 3.2, 3.3, and 3.4 in Think Python

# Jingni Wei

# 3.1
'''
Error: "'repeat_lyrics' is not defined"
'''

#3.2 
'''
No errors
'''

#3.3 

def right_justify(target):
	length = len(target)
	space= 70 - length

	output= space*" "+target
	print output

right_justify('hello world')

#3.4

def do_twice(f, arg): 
	f(arg)
	f(arg)

def print_twice (arg):
	print arg
	print arg

def do_four(f, arg):
	do_twice(f, arg)
	do_twice(f, arg)

do_four( print_twice , 'hollla world')