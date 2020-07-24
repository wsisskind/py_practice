import random

def diceroll6():
	dice = []
	print('How many dice?')
	n = input()
	n = int(n)
	p = round(n*.2)
	for i in range(1, n+1):
		d = random.randrange(1,7)
		dice.append(d)
		print('Dice', i, "-", d)
	dice = removeMin(dice, p)
	total = sum(dice)
	print(total)

def removeMin(l,n):
	for j in range(0,n):
		minval = min(l)
		print ("Removing lowest value: " + str(minval))
		l.remove(minval)
	return l

diceroll6()
