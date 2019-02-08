while True:
	try:
		d1=int(input())
		break
	except:
		print('invalid')
		break
if d1%400==0 or d1%4==0 and d1%100!=0:
	print('yes')
else:
	print('no')
