def right_justify(target):
	length = len(target)
	space= 70 - length

	output= space*" "+target
	print output

right_justify('hello world')

