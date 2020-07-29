from nested_lookup import nested_lookup

standings = {
    'nle' : {
        'div' : 'NL East',
        'atl' : {
            'name' : 'Braves',
            'loc' : 'Atlanta',
            'w' : 2,
            'l' : 3,
        },
        'mia' : {
            'name' : 'Marlins',
            'loc' : 'Miami',
            'w' : 2,
            'l' : 1,
        },
        'nym' : {
            'name' : 'Mets',
            'loc' : 'New York',
            'w' : 3,
            'l' : 2,
        },
        'phi' : {
            'name' : 'Phillies',
            'loc' : 'Philadelphia',
            'w' : 1,
            'l' : 2,
        },
        'wsn' : {
            'name' : 'Nationals',
            'loc' : 'Washington',
            'w' : 1,
            'l' : 4,
        },
    },
    'nlc' : {
        'div' : 'NL Central',
        'chc' : {
            'name' : 'Cubs',
            'loc' : 'Chicago',
            'w' : 4,
            'l' : 1,
        },
        'stl' : {
            'name' : 'Cardinals',
            'loc' : 'St. Louis',
            'w' : 2,
            'l' : 2,
        },
        'mil' : {
            'name' : 'Brewers',
            'loc' : 'Milwaukee',
            'w' : 2,
            'l' : 3,
        },
        'cin' : {
            'name' : 'Reds',
            'loc' : 'Cincinnatti',
            'w' : 1,
            'l' : 4,
        },
        'pit' : {
            'name' : 'Pirates',
            'loc' : 'Pittsburgh',
            'w' : 2,
            'l' : 3,
        },
    },
    'nlw' : {
        'div' : 'NL West',
        'sdp' : {
            'name' : 'Padres',
            'loc' : 'San Diego',
            'w' : 4,
            'l' : 1,
        },
        'col' : {
            'name' : 'Rockies',
            'loc' : 'Colorado',
            'w' : 3,
            'l' : 1,
        },
        'lad' : {
            'name' : 'Dodgers',
            'loc' : 'Los Angeles',
            'w' : 3,
            'l' : 2,
        },
        'sfg' : {
            'name' : 'Giants',
            'loc' : 'San Francisco',
            'w' : 2,
            'l' : 3,
        },
        'ari' : {
            'name' : 'Diamondbacks',
            'loc' : 'Arizona',
            'w' : 2,
            'l' : 3,
        },
    },
    'ale' : {
        'div' : 'AL East',
        'tbr' : {
            'name' : 'Rays',
            'loc' : 'Tampa Bay',
            'w' : 4,
            'l' : 1,
        },
        'bal' : {
            'name' : 'Orioles',
            'loc' : 'Baltimore',
            'w' : 2,
            'l' : 1,
        },
        'nyy' : {
            'name' : 'Yankees',
            'loc' : 'New York',
            'w' : 2,
            'l' : 1,
        },
        'tor' : {
            'name' : 'Blue Jays',
            'loc' : 'Toronto',
            'w' : 3,
            'l' : 2,
        },
        'bos' : {
            'name' : 'Red Sox',
            'loc' : 'Boston',
            'w' : 1,
            'l' : 4,
        },
    },
    'alc' : {
        'div' : 'AL Central',
        'cle' : {
            'name' : 'Indians',
            'loc' : 'Cleveland',
            'w' : 4,
            'l' : 1,
        },
        'min' : {
            'name' : 'Twins',
            'loc' : 'Minnesota',
            'w' : 3,
            'l' : 1,
        },
        'det' : {
            'name' : 'Tigers',
            'loc' : 'Detroit',
            'w' : 3,
            'l' : 2,
        },
        'kcr' : {
            'name' : 'Royals',
            'loc' : 'Kansas City',
            'w' : 2,
            'l' : 3,
        },
        'chw' : {
            'name' : 'White Sox',
            'loc' : 'Chicago',
            'w' : 1,
            'l' : 4,
        },
    },
    'alw' : {
        'div' : 'AL West',
        'hou' : {
            'name' : 'Astros',
            'loc' : 'Houston',
            'w' : 3,
            'l' : 2,
        },
        'oak' : {
            'name' : 'Athletics',
            'loc' : 'Oakland',
            'w' : 3,
            'l' : 2,
        },
        'tex' : {
            'name' : 'Rangers',
            'loc' : 'Texas',
            'w' : 1,
            'l' : 3,
        },
        'laa' : {
            'name' : 'Angels',
            'loc' : 'Los Angeles',
            'w' : 2,
            'l' : 3,
        },
        'sea' : {
            'name' : 'Mariners',
            'loc' : 'Seattle',
            'w' : 1,
            'l' : 4,
        }
    }
}

#print(nested_lookup('loc', standings))
wins = nested_lookup('w', standings)
losses = nested_lookup('l', standings)
teamnames = nested_lookup('name', standings)

for items in wins:
    w = wins
for items in losses:
    l = losses

#for id, info in standings.items():
#    print('Division: ', id)

#    for s in info:
#        print(s + ':', info[s])

#for wi, li in zip(w, l):
#    print(wi/(wi+li))
#print('{0: <15}'.format('----')+'{0: <5}'.format('----')+'{0: <5}'.format(' ')+'{0: <4}'.format('------')+'{0: <5}'.format(' '))
#print('{0: <15}'.format('TEAM')+'{0: <5}'.format('WINS')+'{0: <5}'.format(' ')+'{0: <4}'.format('LOSSES')+'{0: <5}'.format(' '))
#print('{0: <15}'.format('----')+'{0: <5}'.format('----')+'{0: <5}'.format(' ')+'{0: <4}'.format('------')+'{0: <5}'.format(' '))

for t, wi, li in zip(teamnames, w, l):
    print('{0: <15}'.format(t)+'{0: <5}'.format('WINS: ')+'{0: <5}'.format(wi)+'{0: <5}'.format('LOSSES: ')+'{0: <5}'.format(li)+'{0: <5}'.format('W/L: ')+'{0: <5}'.format(round(wi/(wi+li),3)))
