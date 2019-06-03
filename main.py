from player import Player
from deck import Deck as dk

init_msg = 'What would you like to play as? \n 1: Dealer \n 2: Player'

def welcome():
    print(init_msg)
    x = input()
    if x.lower() in ('dealer', '1'):
        print('Dealer')
        return 'Dealer'
    elif x.lower() in ('player', '2'):
        print('player')
        return 'Player'
    else:
        print('Please put a valid input!')
        return welcome()

def chooseARole():
    #The user can pick ih he wants to play as a normaln player or as a dealer
    print('What would you like to play as? \n 1: Dealer \n 2: Player')
    x = input()
    if x.lower() in ('dealer', '1'):
        print('Dealer')
        return 'Dealer'
    elif x.lower() in ('player', '2'):
        print('player')
        return 'Player'
    else:
        print('Please put a valid input!')
        return chooseARole()

def setCash():
    # The user has to pick a how much money the player would have
    # We try-except becuase the player has input a value that can be parsed to an integer, so that we can pass it to the variable p_cash. If the string cannot be converted
    # to an int, it will throw an error and otherwise crash the program
    print('Set players cash: ')
    y = input()
    try:
        if (int(float(y)) > 0):
            return int(float(y))
        else:
            print('You should give some money to the player! (More than 0)')
            setCash()
    except:
        print('Wrong data type - set an integer!')
        return setCash()
    
def setName():
    #The user has to pick a display name for the player (the one that will be used for the resrt of the game)
    print('Set players name: ')
    s = input()
    if s.lower() == 'dealer':
        print('The Player should not be named the same as the Dealer')
        setName()
    elif len(s) < 3:
        print('Give a name of 3 or more character')
        setName()
    else:
        return s


# Setting the values
gameMode = chooseARole()
p_name = setName()
p_cash = setCash()

# Creating the Player object
pl = Player(str(p_name), p_cash)

print(pl)
