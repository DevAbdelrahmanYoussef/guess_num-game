'''
Guess The Number 
Dev : AbdElrahman Youssef
Phone : 01141870926
Location : Egypt
'''
import random
import time

######################################
def main_guess_num():
	global name
	name = input('Player Name: ')
	print('--------------------')
	print('--------------------')
	print('  Guess The Number  ')
	print('--------------------')
	print('--------------------')
	global x
	x = random.randint(1,100)
#	print(x)
#-------------------------------------
def input_your_guess():
	global a 
	a  = int(input("Your Guess Number : "))
#-------------------------------------
def winner():
	print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
	print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
	print('          Yeah You Did It         ')
	print('             Winner',name)
	print('         Chicken Dinner :)        ')
	print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
	print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
#-------------------------------------
def check_num():
	if a == x :
		time.sleep(1)
		winner()
	elif a > x:
		print('Smaller')
		input_your_guess()
		check_num()
	elif a < x :
		print('Bigger')
		input_your_guess()
		check_num()
######################################	
if __name__=="__main__":
	main_guess_num()
# ******************
input_your_guess()
check_num()