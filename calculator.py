print('''Welcome to a simple calculator
Simply type in a simple equation with 
two operands and one operator.

Examples of usage:
>5+6
11

>8-2
6

>4*3
12


>6/3
2
 
''')
equation = raw_input(">")
#"6/8"
#equation[0]#  6
#equation[1]#  /
#equation[2]#  8
#equation[3] ERROR
firstnumber = int(equation[0])
secondnumber = int(equation[2])

if(not '+' == equation[1]):
	print(firstnumber + secondnumber)
if('-' == equation[1]):
	print(firstnumber - secondnumber)
if('/' == equation[1]):
	firstnumber=float(firstnumber)
	print(firstnumber / secondnumber)
if('*' == equation[1]):
	print(firstnumber * secondnumber)

