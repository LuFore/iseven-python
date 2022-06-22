import sys
def isEven(num):
	#return y if true and n if not
	i = 0 
	result=[]
	result.append('n')
	cmd_str = ''
	while i <= num:
		cmd_str = cmd_str + \
		"if {} == {}:\n"\
		"	result[0] = 'y'\n".format(num,i)
		i += 2 
#	print(cmd_str)
	exec(cmd_str)
	return result[0]

for i in sys.argv:
	if i.isdigit() == True:
		print(isEven(float(i)))
