
from math import *

print('Hi! I am your new frined - Python')
name=input('What is your name :)? :')
print(name, 'So beatiful name')
name=int(input('Can I calculate your body index? [0 - no; 1 - yes]:'))
if name==1:
	while True:
		height=input('Please enter your height:')
		try:
			height=int(height)
			if height>0 and height<273: break
		except:
			print('Height must be number integer')
	mass=-1
	while mass<0 or mass>400:		
		try:
			mass=input('Please enter your weight:')
			mass=float(mass)
		except:
			print('Mass must be integer or float')
	try:
		index=round(float(mass/((0.01*height)*(0.01*height))), 1)
		print('Your body index is: '+str(index))
		if index<16:
			print('Dangerous weight for health')
		elif index>16 and index<19:
			print('Less weigth')
		elif index>19 and index<25:
			print('Normal weight')
		elif index>25 and index<30:
			print('Over weight')
		elif index>30 and index<35:
			print('Fat')
		elif index>35 and index<40:
			print('A lot of fat')
		else:
			print('Dangerous fat for health')
	except:
		print('Invalid data')
else:
	print("So sad, this is usefull information")
	print()
print('See your soon, '+str(name)+ '! I will be wait, your Python!')