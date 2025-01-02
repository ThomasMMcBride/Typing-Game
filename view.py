import time

class TypingGameView:
    def display_sentence_after_countdown(self, sentence: str) -> None:
        '''
        Prints a countdown to the screen, followed by the sentence
        the user must type.

        Args:
            sentence (str): The sentence to type
        
        Returns:
            None
        '''
        print("\n3")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("1")
        time.sleep(1)
        print("---------------------------------------------------")
        print(f"{sentence}")
        print("---------------------------------------------------")

    def get_user_input(self) -> str:
        '''
        Prompts the user to type a value.

        Args:
            None
        
        Returns:
            A string representing what the user typed.
        '''

        return input("\nStart typing here: ")

    def display_results(self, speed: float, accuracy: float) -> None:
        '''
        Prints the user's typing speed and accuracy to the console.

        Args:
            speed (float): The player's typing speed.
            accuracy (float): The player's typing accuracy.
        
        Returns:
            None
        '''
        print(f"\nSpeed: {speed} WPM")
        print(f"Accuracy: {accuracy}%")
    
    def display_welcome_and_instructions(self) -> None:
        '''
        Displays the welcome screen and instructions for how to play the game.

        Args:
            None
        
        Returns:
            None
        '''
        print("\nWelcome to the Typing Game!")
        time.sleep(5)
        print("\nYou will be given a sentence.")
        time.sleep(5)
        print("\nType the sentence as accurately and as quickly as possible after the countdown.")
        time.sleep(5)

    def display_goodbye(self):
        '''
        Informs the user that the game is over.

        Args:
            None
        
        Returns:
            None
        '''
        print("\nThanks for playing!")