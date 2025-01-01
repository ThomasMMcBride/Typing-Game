from model import TypingGameModel
from view import TypingGameView

class TypingGameController:
    '''
    Represents the controller for the Typing Game.
    '''

    
    def __init__(self):
        '''
        Constructs a default controller for the Typing Game.

        Args:
            None

        Returns:
            None
        '''
        self.model = TypingGameModel()
        self.view = TypingGameView()

    def run(self):
        '''
        Runs a single instance of the Typing Game.

        Args:
            None
        
        Returns:
            None
        '''
        # Start the game.
        self.view.display_welcome_and_instructions()
        sentence = self.model.get_selected_sentence()
        self.view.display_sentence_after_countdown(sentence)
        
        # Prompt the user to type and time them.
        self.model.start_timer()
        user_input = self.view.get_user_input()
        self.model.stop_timer()
        
        # Retrieve the speed and accuracy of their attempt.
        speed = self.model.calculate_speed(user_input)
        accuracy = self.model.calculate_accuracy(user_input)
        
        # Display the results to the user.
        self.view.display_results(speed, accuracy)
        self.view.display_goodbye()
