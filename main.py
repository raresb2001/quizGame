import requests
import json
import os


class QuizGame:
    def __init__(self):
        """
        Initialize a new instance.
        """
        self.questions = []  # List to store quiz questions
        self.current_question_index = 0  # Index of the current question being displayed
        self.score = 0  # Player's score
        self.question_points = {}  # Dictionary to store points for each question
        self.high_scores_file = "high_scores.json"  # File to store high scores
        self.high_scores = {}  # Dictionary to store high scores
        self.load_high_scores()  # Load high scores from file

    def load_questions(self):
        """
        Load quiz questions from using Trivia API.
        """
        urls = [
            "https://opentdb.com/api.php?amount=10&category=9&difficulty=easy&type=boolean",
            "https://opentdb.com/api.php?amount=10&category=9&difficulty=medium&type=boolean",
            "https://opentdb.com/api.php?amount=10&category=9&difficulty=hard&type=boolean"
        ]
        for url in urls:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                self.questions.extend(data['results'])
                print(f"Response from {url}:")
                print(json.dumps(data, indent=4))
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
            self.high_scores = {}

    def save_high_scores(self):
        """
        Save high scores to a JSON file.
        """
        with open(self.high_scores_file, 'w') as file:
            json.dump(self.high_scores, file, indent=4)

    def display_high_score(self):
        pass

    def play_game(self):
        pass

    def display_instructions(self):
        pass

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
    game.load_questions()
    game.menu()

