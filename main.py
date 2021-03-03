# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
'''
Euro '88.

Part 1
'''

# de scorende spelers tijdens de finale...
gullit = 'Ruud Gullit'
van_basten = 'Marco van Basten'

# welke minuten werd er gescoord?
goal_0 = 32
goal_1 = 54

scorers = gullit+' '+ str(goal_0)+', '+ van_basten +' ' + str(goal_1) # wie scoorde er wanneer?
report = f'{gullit} scored in the {goal_0}nd minute\n{van_basten} scored in the {goal_1}th minute' # verslag van wedstrijd tav gescoorde goals


'''
Euro '88.

Part 2
'''

player = 'Ronald Koeman'
first_name = player[:player.find(' ')]
last_name_len = len(player[player.find('K'):])
name_short = first_name[0]+'. '+player[-last_name_len:]
chant = (len(first_name)*(first_name+'! '))[:-1] # wat scandeert het publiek?
good_chant = chant[-1]!=' ' # check of laatste waarde geen spatie is
