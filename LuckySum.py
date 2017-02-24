'''
Ask for 3 ints
print their sum, however if the number is
evenly divisble by 3 and 5, then
the number is not added and
the number to the right is not added

'''

firstnumber = int(raw_input("first number"))
secondnumber = int(raw_input("second number"))
thirdnumber = int(raw_input("third number"))

#is each number divisble by 3 or 5
if(firstnumber % 3 == 0 and firstnumber%5 ==0):
	print(thirdnumber)
elif(secondnumber % 3 == 0 and secondnumber%5 ==0):
	print(firstnumber)
elif(thirdnumber % 3 == 0 and thirdnumber%5 ==0):
	print(firstnumber+secondnumber)
else:
    print(firstnumber+secondnumber+thirdnumber)



#print their appropriate sum