def diceroll6():
	dice = []
	print('How many dice?')
	n = input()
	n = int(n)
	for i in range(1, n+1):
		d = random.randrange(1,7)
		dice.append(d)
		print('Dice', i, "-", d)
	total = sum(dice)
	print(total)
