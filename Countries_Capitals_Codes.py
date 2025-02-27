"""
Description:
This Python project is an interactive quiz game that tests the player's knowledge of countries, capitals, and country codes. The program generates random multiple-choice questions, ensuring that each question is unique. Players receive immediate feedback on their answers and a final score at the end of the quiz.

Key Features:
✔ Randomly generated questions about country capitals, names, and codes
✔ Unique questions per quiz session to avoid repetition
✔ User input validation and immediate feedback on correctness
✔ Score tracking with a final performance summary
"""
import random

class Country:
    def __init__(self, country, capital, code):
        self.country = country
        self.capital = capital
        self.code = code

class Question:
    def __init__(self, question_text, answer):
        self.question_text = question_text
        self.answer = answer

# Generate unique questions
class QuestionGenerator:
    def __init__(self, countries):
        self.countries = countries
        self.asked_questions = set()

    def generate_question(self):
        while True:
            country = random.choice(self.countries)
            question_type = random.choice(["capital", "country", "code"])

            if question_type == "capital":
                question_text = f"What is the capital of {country.country}?"
                answer = country.capital
            elif question_type == "code":
                question_text = f"What is the country code of {country.country}?"
                answer = country.code
            else:
                question_text = f"Which country has the capital {country.capital}?"
                answer = country.country

            if question_text not in self.asked_questions:
                self.asked_questions.add(question_text)
                return Question(question_text, answer)

class Quiz:
    def __init__(self, question_generator, num_questions=10):
        self.question_generator = question_generator
        self.num_questions = num_questions
        self.score = 0

    def start(self):
        for _ in range(self.num_questions):
            question = self.question_generator.generate_question()
            print(question)
            user_answer = input("Enter your answer: ").strip()

            if user_answer.lower() == question.answer.lower():
                self.score += 1
                print("✅ Correct!\n")
            else:
                print(f"❌ Incorrect! The correct answer is: {question.answer}\n")

            print(f"Your score is: {self.score}\n")
        print(f"Quiz finished! Your final score: {self.score}/{self.num_questions}")


def main():
    country_data = [
        {"country": "The Netherlands", "capital": "Amsterdam", "code": "NL"},
        {"country": "Greece", "capital": "Athens", "code": "GR"},
        {"country": "Germany", "capital": "Berlin", "code": "DE"},
        {"country": "Slovakia", "capital": "Bratislava", "code": "SK"},
        {"country": "Belgium", "capital": "Brussels", "code": "BE"},
        {"country": "Romania", "capital": "Bucharest", "code": "RO"},
        {"country": "Hungary", "capital": "Budapest", "code": "HU"},
        {"country": "Denmark", "capital": "Copenhagen", "code": "DK"},
        {"country": "Ireland", "capital": "Dublin", "code": "IE"},
        {"country": "Finland", "capital": "Helsinki", "code": "FI"},
        {"country": "Portugal", "capital": "Lisbon", "code": "PT"},
        {"country": "Slovenia", "capital": "Ljubljana", "code": "SI"},
        {"country": "Luxembourg", "capital": "Luxembourg", "code": "LU"},
        {"country": "Spain", "capital": "Madrid", "code": "ES"},
        {"country": "Cyprus", "capital": "Nicosia", "code": "CY"},
        {"country": "France", "capital": "Paris", "code": "FR"},
        {"country": "The Czech Republic", "capital": "Prague", "code": "CZ"},
        {"country": "Latvia", "capital": "Riga", "code": "LV"},
        {"country": "Italy", "capital": "Rome", "code": "IT"},
        {"country": "Bulgaria", "capital": "Sofia", "code": "BG"},
        {"country": "Sweden", "capital": "Stockholm", "code": "SE"},
        {"country": "Estonia", "capital": "Tallinn", "code": "EE"},
        {"country": "Malta", "capital": "Valletta", "code": "MT"},
        {"country": "Austria", "capital": "Vienna", "code": "AT"},
        {"country": "Lithuania", "capital": "Vilnius", "code": "LT"},
        {"country": "Poland", "capital": "Warsaw", "code": "PL"},
        {"country": "Croatia", "capital": "Zagreb", "code": "HR"},
        {"country": "The United Kingdom", "capital": "London", "code": "GB"}
    ]

    # Convert the data to country objects
    countries = [Country(**data) for data in country_data]

    # Instantiate a QuestionGenerator with the countries list
    question_generator = QuestionGenerator(countries)

    # Create a Quiz with 10 unique questions
    quiz = Quiz(question_generator, num_questions=10)
    quiz.start()

if __name__ == "__main__":
    main()