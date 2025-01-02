import time
import random

class TypingGameModel:
    '''
    Responsible for keeping track of:
    - The sentence the player needs to type
    - The amount of time taken for the player
      to finish typing the sentence
    '''

    def __init__(self):
        '''
        Constructs a typing game model.
        '''
        # Obtain sentences from local file
        with open("sentences.txt") as sentence_file:
            sentences = sentence_file.readlines() 
            sentences = [sentence.strip() for sentence in sentences]
        self.sentences = sentences

        # Select a random sentence from self.sentences
        # Hint: Look into the random module for Python
        self.selected_sentence = random.choice(self.sentences)

        self.start_time = None
        self.end_time = None

    def get_selected_sentence(self) -> str:
        '''
        Provides the sentence the user must type.

        Args:
            None
        
        Returns:
            The sentence the user must type 
        '''
        return self.selected_sentence

    def start_timer(self) -> None:
        '''
        Starts the timer for the player to start typing the sentence.
        EFFECT: The start_time field is mutated to the current time 

        Args:
            None
        
        Returns:
            None
        '''
        self.start_time = time.time()

    def stop_timer(self):
        '''
        Stops the timer, indicating that the player has completed typing the sentence.
        EFFECT: The stop_time field is mutated to the current time 

        Args:
            None
        
        Returns:
            None
        '''
        self.end_time = time.time()

    def calculate_speed(self, user_input) -> float:
        '''
        Provides the player's typing speed in words per minute.

        Args:
            user_input (str): The player's typed sentence.

        Returns:
            A float representing the typing speed in words per minute. 
        '''
        time_taken = self.end_time - self.start_time
        word_count = len(user_input.split())

        speed = word_count / (time_taken / 60)
        return round(speed, 2)

    def calculate_accuracy(self, user_input):
        '''
        Provides the player's accuracy in typing the provided sentence.

        Args:
            user_input (str): What the user typed.

        Returns:
            A float representing the accuracy of the user's typed input

        '''
        correct_chars = sum(a == b for a, b in zip(self.selected_sentence, user_input))
        total_chars = len(self.selected_sentence)
        accuracy = (correct_chars / total_chars) * 100 if total_chars > 0 else 0
        return round(accuracy, 2)