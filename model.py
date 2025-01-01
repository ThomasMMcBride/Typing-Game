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
        # TODO: Obtain sentences from local .txt file
        # Hint: Look into 'open' which is a built-in python function
        with open("____TODO_____") as sentence_file:
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
        # TODO: Return the selected sentence within this class
        # Hint: use self. to access the fields of this class
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
        # TODO: Set the self.start_time field to the current time
        # Hint: Look into the time module for Python
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
        # TODO: Set the self.end_time field to the current time
        # Hint: Should be very similar to the implementation of start_timer()
        self.end_time = time.time()

    def calculate_speed(self, user_input: str) -> float:
        '''
        Provides the player's typing speed in words per minute.

        Args:
            user_input (str): The player's typed sentence.

        Returns:
            A float representing the typing speed in words per minute. 
        '''
        time_taken = self.end_time - self.start_time
        word_count = len(user_input.split())

        # TODO: Using the time_taken(in seconds) and the word_count, calculate the speed in words per minute
        speed = word_count / (time_taken / 60)
        return round(speed, 2)

    def calculate_accuracy(self, user_input: str) -> float:
        '''
        Provides the player's accuracy in typing the provided sentence.

        Args:
            user_input (str): What the user typed.

        Returns:
            A float representing the accuracy of the user's typed input

        '''
        correct_chars = sum(a == b for a, b in zip(self.selected_sentence, user_input))
        total_chars = len(self.selected_sentence)

        # TODO: Calculate the user's accuracy using the correct_chars and total_chars variables.
        # Also, try to handle the division by 0 case where total_chars is 0
        accuracy = (correct_chars / total_chars) * 100 if total_chars > 0 else 0
        return round(accuracy, 2)