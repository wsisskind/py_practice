def dnd():

    import random
    import math
    import os

    savedata = {}
    stats = []
    modtab = []

    if os.path.isfile('./dnd.dnd'):
        try:

            with open('dnd.dnd', 'r') as f:
                for line in f:
                    name, value = line.split('=')
                    savedata[name] = int(value)

        except ValueError:
            print('Could not load saved data!')

        try:

            stats.append(savedata['srn'])
            stats.append(savedata['dex'])
            stats.append(savedata['con'])
            stats.append(savedata['ing'])
            stats.append(savedata['wis'])
            stats.append(savedata['cha'])

            modtab.append(savedata['srnmod'])
            modtab.append(savedata['dexmod'])
            modtab.append(savedata['conmod'])
            modtab.append(savedata['ingmod'])
            modtab.append(savedata['wismod'])
            modtab.append(savedata['chamod'])

        except KeyError:
            print('Could not find data to load.')
    else:
        print('dnd.dnd not found.')

    choice = 0

    def savestats():
        if len(stats) != 0:
            with open('dnd.dnd', 'w') as f:
                f.write(str('srn= ' + str(stats[0])))
                f.write(str('\n'))
                f.write(str('dex= ' + str(stats[1])))
                f.write(str('\n'))
                f.write(str('con= ' + str(stats[2])))
                f.write(str('\n'))
                f.write(str('ing= ' + str(stats[3])))
                f.write(str('\n'))
                f.write(str('wis= ' + str(stats[4])))
                f.write(str('\n'))
                f.write(str('cha= ' + str(stats[5])))
                f.write(str('\n'))
                f.write(str('srnmod= ' + str(modtab[0])))
                f.write(str('\n'))
                f.write(str('dexmod= ' + str(modtab[1])))
                f.write(str('\n'))
                f.write(str('conmod= ' + str(modtab[2])))
                f.write(str('\n'))
                f.write(str('ingmod= ' + str(modtab[3])))
                f.write(str('\n'))
                f.write(str('wismod= ' + str(modtab[4])))
                f.write(str('\n'))
                f.write(str('chamod= ' + str(modtab[5])))
                f.close()
        else:
            print('No data to save! Exiting...')

    def rolldice():

        dice = []
        print('How many dice?')
        n = int(input())
        if n in range(11):
            for i in range(1, n+1):
                d = random.randrange(1,7)
                dice.append(d)
                print('\nDice', i, "-", d)
            total = sum(dice)
            print('Your ' + n + ' dice total: ' total)
        else:
            print("Too many dice. Try up to 10.")
            rolldice()

    def statroll():

        #stats = []
        #modtab = []
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
                    modtab.append(5)

        def getval():

            def getsrn():
                srn = int(input('What did you roll for strength? '))
                if srn in range(3, 19):
                    stats.append(srn)
                else:
                    print("Impossible roll. Try again.")
                    getsrn()
            def getdex():
                dex = int(input('What did you roll for dexterity? '))
                if dex in range(3, 19):
                    stats.append(dex)
                else:
                    print("Impossible roll. Try again.")
                    getdex()
            def getcon():
                con = int(input('What did you roll for constitution? '))
                if con in range(3, 19):
                    stats.append(con)
                else:
                    print("Impossible roll. Try again.")
                    getcon()
            def geting():
                ing = int(input('What did you roll for intelligence? '))
                if ing in range(3, 19):
                    stats.append(ing)
                else:
                    print("Impossible roll. Try again.")
                    geting()
            def getwis():
                wis = int(input("What did you roll for wisdom? "))
                if wis in range(3, 19):
                    stats.append(wis)
                else:
                    print("Impossible roll. Try again.")
                    getwis()
            def getcha():
                cha = int(input("What did you roll for charisma? "))
                if cha in range(3, 19):
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

            stats.clear()
            modtab.clear()

            roll()
            modcalc()

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
                yn = input('Accept these values (Y) or roll new ones (N)? ')
                if yn in ('y','Y','ye','yes'):
                    start()
                elif yn in ('n','N','no'):
                    stats.clear()
                    modtab.clear()
                    randroll()
                else:
                    print('Please type either Y or N.')
                    setval()

            setval()

        def manuroll():
            stats.clear()
            modtab.clear()

            getval()
            modcalc()

            print('\nSTATS:')
            print('------')
            print('STR: ' + str(stats[0]) + '\tMOD: ' + str(modtab[0]))
            print('DEX: ' + str(stats[1]) + '\tMOD: ' + str(modtab[1]))
            print('CON: ' + str(stats[2]) + '\tMOD: ' + str(modtab[2]))
            print('INT: ' + str(stats[3]) + '\tMOD: ' + str(modtab[3]))
            print('WIS: ' + str(stats[4]) + '\tMOD: ' + str(modtab[4]))
            print('CHA: ' + str(stats[5]) + '\tMOD: ' + str(modtab[5]))
            print('------\n')

            def setval():
                yn = input('Accept these values (Y) or roll new ones (N)? ')
                if yn in ('y','Y','ye','yes'):
                    start()
                elif yn in ('n','N','no'):
                    stats.clear()
                    modtab.clear()
                    manuroll()
                else:
                    print('Please type either Y or N.')
                    setval()

            setval()

        def titleprn():
            print('\n-----------------')
            print('STAT ROLLER v.0.1')
            print('-----------------')
            start()

        def start():
            print('\nCHOICES')
            print('-------')
            print('1) Roll random values')
            print('2) Manually input values')
            print('3) See last saved values')
            print('4) Roll some six-sided dice')
            print('5) Exit the program\n')

            try:
                choice = int(input('What would you like to do? '))
            except ValueError:
                print('Invalid input.')
                start()

            if choice == 1:
                print(' \n ')
                randroll()
            elif choice == 2:
                (print(' \n '))
                manuroll()
            elif choice == 3:
                print(' \n ')
                if len(modtab) != 0:
                    if len(stats) != 0:
                        print('STATS:')
                        print('------')
                        print('STR: ' + str(stats[0]) + '\tMOD: ' + str(modtab[0]))
                        print('DEX: ' + str(stats[1]) + '\tMOD: ' + str(modtab[1]))
                        print('CON: ' + str(stats[2]) + '\tMOD: ' + str(modtab[2]))
                        print('INT: ' + str(stats[3]) + '\tMOD: ' + str(modtab[3]))
                        print('WIS: ' + str(stats[4]) + '\tMOD: ' + str(modtab[4]))
                        print('CHA: ' + str(stats[5]) + '\tMOD: ' + str(modtab[5]))
                        print('------\n')
                    else:
                        print('\nNo saved stats data.')
                else:
                    print('\nNo saved modifier data.')
                start()
            elif choice == 4:
                print(' \n ')
                rolldice()
                start()
            elif choice == 5:
                savestats()
                return
            else:
                print('Invalid input.')
                start()

        titleprn()

    statroll()

dnd()
