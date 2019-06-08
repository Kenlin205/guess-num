import random
r = random.randint(1,100)
while True:
	num = int(input("guess a number ->"))
	if num == r:
		print("you have guess it !!! ")
		break
	elif num > r:
		print("bigger than answer ->")
	elif num < r:
		print("less than answer ->")

