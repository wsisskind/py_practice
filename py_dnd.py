stats = []
modtab = []
srn = 0
dex = 0
con = 0
ing = 0
wis = 0
cha = 0

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
                        choice = input()
                        if choice in ('y','Y','ye','yes'):
                                return
                        elif choice in ('n','N','no','nope'):
                                stats.clear()
                                modtab.clear()
                                randroll()
                        else:
                                print('Please type either Y or N.')
                                setval()

                setval()

        def manuroll():

                stats = []
                modtab = []

                srn = input('What did you roll for STRENGTH?')
                stats.append(srn)
                dex = input('What did you roll for DEXTERITY?')
                stats.append(dex)
                con = input('What did you roll for CONSTITUTION?')
                stats.append(con)
                ing = input('What did you roll for INTELLIGENCE?')
                stats.append(ing)
                wis = input('What did you roll for WISDOM?')
                stats.append(wis)
                cha = input('What did you roll for CHARISMA?')
                stats.append(cha)
                
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
                        choice = input()
                        if choice in ('y','Y','ye','yes'):
                                return
                        elif choice in ('n','N','no','nope'):
                                randroll()
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

