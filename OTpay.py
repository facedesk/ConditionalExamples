print("gimmeh pay rate")
rate = float(raw_input(">"))
print("gimmeh hours worked")
hours = float(raw_input(">"))


totalpay=0
if(hours<40):
	totalpay = rate * hours
else:
	leftover = hours - 40
	print(leftover)
	hours = 40
	otpay = rate * 1.5
	print (otpay)
	totalpay = (hours * rate) + (leftover * otpay)
print(totalpay)