stats = []
modtab = []
srn = 0
dex = 0
con = 0
ing = 0
wis = 0
cha = 0
choice = 0

def diceroll6():

	import random

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


def statroll():

        import random

        stats = []
        modtab = []
        t = 0

        def roll():
                dice = []
                for i in range(0,6):
                        for j in range(0,4):
                                d = random.randrange(1,7)
                                dice.append(d)
                        dice.sort()
                        dice.pop(0)
                        t = sum(dice)
                        stats.append(t)
                        dice = []
                        t = 0
                        d = 0

        def modcalc():
                for m in range(len(stats)):
                        if stats[m] in range(18, 20):
                                modtab.append(4)
                        elif stats[m] in range(16, 18):
                                modtab.append(3)
                        elif stats[m] in range(14, 16):
                                modtab.append(2)
                        elif stats[m] in range(12, 14):
                                modtab.append(1)
                        elif stats[m] in range(10, 12):
                                modtab.append(0)
                        elif stats[m] in range(8, 10):
                                modtab.append(-1)
                        elif stats[m] in range(6, 8):
                                modtab.append(-2)
                        elif stats[m] in range(4, 6):
                                modtab.append(-3)
                        elif stats[m] in range(2, 4):
                                modtab.append(-4)
                        elif stats[m] == 1:
                                modtab.append(-5)

        def getval():

                def getsrn():
                        srn = int(input('What did you roll for STRENGTH? '))
                        if srn in range(3,19):
                                stats.append(srn)
                        else:
                                print("Impossible roll. Try again.")
                                getsrn()
                def getdex():
                        dex = int(input('What did you roll for DEXTERITY? '))
                        if dex in range(3,19):
                                stats.append(dex)
                        else:
                                print("Impossible roll. Try again.")
                                getdex()
                def getcon():
                        con = int(input('What did you roll for CONSTITUTION? '))
                        if con in range(3,19):
                                stats.append(con)
                        else:
                                print("Impossible roll. Try again.")
                                getcon()
                def geting():
                        ing = int(input('What did you roll for INTELLIGENCE? '))
                        if ing in range(3,19):
                                stats.append(ing)
                        else:
                                print("Impossible roll. Try again.")
                                geting()
                def getwis():
                        wis = int(input('What did you roll for WISDOM? '))
                        if wis in range(3,19):
                                stats.append(wis)
                        else:
                                print("Impossible roll. Try again.")
                                getwis()
                def getcha():
                        cha = int(input('What did you roll for CHARISMA? '))
                        if cha in range(3,19):
                                stats.append(cha)
                        else:
                                print("Impossible roll. Try again.")
                                getcha()
                getsrn()
                getdex()
                getcon()
                geting()
                getwis()
                getcha()
        
        def randroll():

                roll()
                print(stats)
                modcalc()
                print(modtab)

                print('STATS:')
                print('------')
                print('STR: ' + str(stats[0]) + '\tMOD: ' + str(modtab[0]))
                print('DEX: ' + str(stats[1]) + '\tMOD: ' + str(modtab[1]))
                print('CON: ' + str(stats[2]) + '\tMOD: ' + str(modtab[2]))
                print('INT: ' + str(stats[3]) + '\tMOD: ' + str(modtab[3]))
                print('WIS: ' + str(stats[4]) + '\tMOD: ' + str(modtab[4]))
                print('CHA: ' + str(stats[5]) + '\tMOD: ' + str(modtab[5]))
                print('------\n')
                
                def setval():
                        print('Accept these values (Y) or roll again? (N)')
                        yn = input()
                        if yn in ('y','Y','ye','yes'):
                                return
                        elif yn in ('n','N','no','nope'):
                                stats.clear()
                                modtab.clear()
                                randroll()
                        else:
                                print('Please type either Y or N.')
                                setval()
                        
                setval()

        def manuroll():

                
                getval()
                print(stats)

                modcalc()
                print(modtab)

                print('STATS:')
                print('------')
                print('STR: ' + str(stats[0]) + '\tMOD: ' + str(modtab[0]))
                print('DEX: ' + str(stats[1]) + '\tMOD: ' + str(modtab[1]))
                print('CON: ' + str(stats[2]) + '\tMOD: ' + str(modtab[2]))
                print('INT: ' + str(stats[3]) + '\tMOD: ' + str(modtab[3]))
                print('WIS: ' + str(stats[4]) + '\tMOD: ' + str(modtab[4]))
                print('CHA: ' + str(stats[5]) + '\tMOD: ' + str(modtab[5]))
                print('------\n')
                
                def setval():

                        print('Accept these values (Y) or roll again? (N)')
                        yn = input()
                        if yn in ('y','Y','ye','yes'):
                                return
                        elif yn in ('n','N','no','nope'):
                                stats.clear()
                                modtab.clear()
                                manuroll()
                        else:
                                print('Please type either Y or N.')
                                setval()

                setval()
                        

        print('\n-----------------')
        print('STAT ROLLER v.0.1')
        print('-----------------\n')

        print('Would you like to:')
        print('1) Roll random values?')
        print('2) Manually input values?')
        print('3) Exit the program?')
        choice = input()
        choice = int(choice)

        if choice == 1:
                randroll()
        if choice == 2:
                manuroll()
        if choice == 3:
                return

