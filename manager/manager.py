from .games import hangman
from .games import tictactoe


class MANAGER:

    def __init__(self):
        self.gameOptions = ['Hangman', 'Tictactoe']
        self.playAgainOptions = ['Yes', 'No']
        self.viewRecordOptions = ['Yes', 'No']
        self.gamesPlayed = 0
        self.playAgain = True
        self.tracker = {}
        
        self._initiateTracker()


    # creates dictionary to track wins/losses
    def _initiateTracker(self):
        
        for gameOption in self.gameOptions:
            self.tracker[gameOption] = {'Wins':0, 'Losses':0}


    # placeholder comment
    def _initiateGameSelection(self):

        print('\nGame Choices:')

        for i, game in enumerate(self.gameOptions):
            print('{}. {}'.format(i+1, game))

        while True:
            try:
                gameNumber = int(input("Select The Number Of The Game You Want To Play: ")) 

                if gameNumber in range(1, len(self.gameOptions)+1):
                    return gameNumber
                else:
                    print("Please select option an option between 1-{}".format(len(self.gameOptions)))      

            except ValueError:
                print("Provide an integer value...")


    def _initiatePlayAgainSelection(self):

        print('\nWould you like to play another game?')
                
        for i, playAgainOption in enumerate(self.playAgainOptions):
            print('{}. {}'.format(i+1, playAgainOption))

        while True:
            try:
                playAgainOption = int(input("Select an option: "))

                if playAgainOption in range(1, len(self.playAgainOptions)+1):
                
                    if playAgainOption == 1:
                        print("Onward! More games lies ahead...")
                        self.playAgain = True
                    elif playAgainOption == 2:
                        print("Thank you for playing, goodbye.")
                        self.playAgain = False
                    
                    return

            except ValueError:
                print("Provide an integer value...")


    # initializes manager
    def initiatePlay(self):

        while self.playAgain:

            if self.gamesPlayed > 0:
                self._initiatePlayAgainSelection()

            if self.playAgain:
                gameNumber = self._initiateGameSelection()

                if gameNumber == 1:
                    print("Loading up hangman...")
                elif gameNumber == 2:
                    print("Loading up TicTacToe...")
                
                self.playGame(self.gameOptions[gameNumber-1])
            
            else:
                self._displayResults()
        
        
    # initializes game/ track results       
    def playGame(self, game):

        if game == 'Hangman':
            x = hangman.HANGMAN().playGame()
        elif game == 'Tictactoe':
            x = tictactoe.TICTACTOE().playGame()

        if x['win'] == True:
            self.tracker[game]['Wins'] += 1
        else:
            self.tracker[game]['Losses'] += 1

        self.gamesPlayed += 1
    
       
    # track/record/calculate results 
    def _displayResults(self):
                
        print('\nWould you like to see your record?')
        
        for i, game in enumerate(self.viewRecordOptions):
                print('{}. {}'.format(i+1, game))
                
        while True:
            try:
                record = int(input("Select one of the options: ")) 
                
                if record in range(1, len(self.viewRecordOptions)):
                
                    if record==1 :
                        for i in self.gameOptions:
                            print('\nYour record for', i, 'is:', '\n', self.tracker[i])

                    return

                else:
                    print("Please select option betwen 1-{}".format(len(self.viewRecordOptions)))
            except ValueError:
                print("Provide an integer value...")