import requests
import json
import os
import random

class QuizGame:
    def __init__(self):
        """
        Initialize a new instance.
        """
        self.questions = []  # List to store quiz questions
        self.current_question_index = 0  # Index of the current question being displayed
        self.score = 0  # Player's score
        self.question_points = 10  # Points for each question
        self.high_scores_file = "high_scores.json"  # File to store high scores
        self.high_scores = []  # List to store high scores
        self.load_high_scores()  # Load high scores from file

    def load_questions(self):
        """
        Load quiz questions from the Trivia API.
        """
        url = "https://opentdb.com/api.php?amount=10&category=9&difficulty=easy&type=boolean"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            self.questions.extend(data['results'])
        else:
            print(f"Failed to fetch data from {url}")

    def load_high_scores(self):
        """
        Load high scores from a JSON file.
        """
        if os.path.exists(self.high_scores_file):
            with open(self.high_scores_file, 'r') as file:
                self.high_scores = json.load(file)
        else:
            self.high_scores = []

    def save_high_scores(self):
        """
        Save high scores to a JSON file.
        """
        with open(self.high_scores_file, 'w') as file:
            json.dump(self.high_scores, file, indent=4)

    def display_high_score(self):
        """
        Display the high scores.
        """
        if not self.high_scores:
            print("No high scores yet.")
        else:
            print("High Scores:")
            for idx, score in enumerate(self.high_scores, start=1):
                print(f"{idx}. {score}")

    def display_instructions(self):
        """
        Display the game instructions.
        """
        print("Instructions:")
        print("1. Answer the questions correctly to score points.")
        print("2. The game will ask easy questions.")
        print("3. You can quit the game at any time by typing 'quit'.")

    def play_game(self):
        """
        The main game loop.
        """
        self.load_questions()  # Load questions when the game starts
        self.score = 0
        random.shuffle(self.questions)
        for question in self.questions:
            print(f"Question: {question['question']}")
            answer = input("Answer with True/False: ").strip()
            if answer.lower() == 'quit':
                print("You chose to quit the game.")
                self.end_game()
                return

            if answer == question['correct_answer']:
                self.score += self.question_points
                print(f"Keep going! Your score is now {self.score}")
            else:
                print(f"I'm sorry! The correct answer was {question['correct_answer']}.")
                self.end_game()
                return

        self.end_game()

    def end_game(self):
        """
        End the game and update high scores.
        """
        print(f"Game Over! Your final score is {self.score}.")
        self.update_high_scores()
        self.save_high_scores()

    def update_high_scores(self):
        """
        Update the list of high scores.
        """
        self.high_scores.append(self.score)
        self.high_scores.sort(reverse=True)
        self.high_scores = self.high_scores[:10]

    def menu(self):
        """
        Display the main menu and handle user input.
        """
        while True:
            print("Menu:")
            print("1. Play Game")
            print("2. View Instructions")
            print("3. View High Scores")
            print("4. Quit")
            choice = input("Choose an option: ").strip()

            if choice == '1':
                self.play_game()
            elif choice == '2':
                self.display_instructions()
            elif choice == '3':
                self.display_high_score()
            elif choice == '4':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    game = QuizGame()
    game.menu()
