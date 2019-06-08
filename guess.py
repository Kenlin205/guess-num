import random
start = int(input("Please choose an number to start -> "))
end= int(input("Please choose an number to end -> "))
r = random.randint(start,end)
count = 0
while True:
	count += 1 # count = count +1 
	num = int(input("guess a number ->"))
	if num == r:
		print("you have guess it !!! ")
		print("This is" , count, "times guess")
		break
	elif num > r:
		print("bigger than answer ->")
	elif num < r:
		print("less than answer ->")
	print("This is" , count, "times guess")

