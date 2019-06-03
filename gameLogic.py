from deck import Deck as dk

class Game(object):

    def __init__(self, g_player, g_gameMod):
        self.player = g_player
        self.gameMode = g_gameMod

    @property
    def player(self):
        return self._player

    @property
    def gameMode(self):
        return self._gamMode

    #declare for the Dealer
    dealerScore = 0

    # We declare 'containers', where we gonna store the cards for the player and the dealer
    playerCards = ()
    dalerCards = ()

    #We set values for the bet and if the bet has been 'doubled down'
    bet = 0
    doubleDown = False

    #We call this method to have a session of Black Jack!
    def play():
        
        return

    
    #FUNCTIONS

    def placeBet():
        x = input()    
        try:
            if (int(float(x)) > 0):
                return int(float(x))
            else:
                print('You should bet more than a $0')
                placeBet()
        except:
            print('Wrong data type - set an integer!')
            return placeBet()

    def calculateScore(*arg):
        score = 0
        for ar in arg:
            #Number card
            if ar[0] in ('2','3','4','5','6','7','8','9'):
                score += int(ar[0])
            #Ace card
            elif(ar[0] == 'A'):
                if(score + 10 <= 21):
                    score += 11
                else:
                    score += 1
            #Face card or 10 (put the 10 here, becuse I am evil and I like to do premature optimization)
            else:
                score += 10
        return score
    
    def checkResult():
        if player.score > 21:
            loose()
        if (player.score == dealerScore):
            draw()
        if (player.score > dealerScore):
            win()


    #Players options

    def hit():
        return
    def stand():
        return

    def surrender():
        return

    # def doubleDowm():
    # return
    # def split():
    #     return
    # def insurrance():
    #     return

    #END GAME FUNCTIONS


    def draw():
        card = dk.draw()
        for cr in playerCards
        if (card in playerCards):
            return card
        return

    # Win
    def payPlayer(pay):
        return
    
    # Loose
    def loose():
        return

    def resetSession():
        playerCards = {}
        dalerCards = {}
        bet = 0
        doubleDown = False
