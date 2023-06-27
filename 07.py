#def square (x):
#	return x * x

#def cube (x):
#	return x * x * x
#result = square
#print(result(4))


#def outer_func(message):
	
#	def inner_func():
#		print(message)
#	return inner_func
#
#hi_func = outer_func('Hi')
#hi_func()

# [1, 2, 3, 4] --- [1, 4, 9 16]

#my_list = [1, 2, 3, 4]

#def my_func(arg_list, func):
#	result = []
#	for i in arg_list:
#		result.append(func(i))

#	return result

#print(my_func(my_list, square))
#print(my_func(my_list, cube))

def disp_func():
	print('This is disp_func!')
	print('Hello world')

disp_func()