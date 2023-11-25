import random

class Question:
    def __init__(self, question, subject, topic, difficulty, marks):
        self.question = question
        self.subject = subject
        self.topic = topic
        self.difficulty = difficulty
        self.marks = marks

class QuestionPaperGenerator:
    def __init__(self, question_store):
        self.question_store = question_store

    def generate_question_paper(self, total_marks, difficulty_distribution):
        question_paper = []
        
        for difficulty, percentage in difficulty_distribution.items():
            difficulty_questions = self._select_questions(difficulty, percentage, total_marks)
            question_paper.extend(difficulty_questions)

        return question_paper

    def _select_questions(self, difficulty, percentage, total_marks):
        difficulty_questions = [question for question in self.question_store if question.difficulty == difficulty]
        total_questions = int(total_marks * (percentage / 100))

        return random.sample(difficulty_questions, min(len(difficulty_questions), total_questions))

# Example usage:
question_store = [
    Question("What is the speed of light", "Physics", "Waves", "Easy", 5),
    Question("Who wrote Romeo and Juliet", "Literature", "Shakespeare", "Medium", 8),
    Question("What is the capital of France", "Geography", "Europe", "Easy", 4),
    Question("What is the formula for calculating area of a circle", "Mathematics", "Geometry", "Medium", 6),
    Question("Name the largest planet in our solar system", "Astronomy", "Planets", "Medium", 7),
    Question("What is the powerhouse of the cell", "Biology", "Cells", "Easy", 5),
    Question("What is the chemical symbol for gold", "Chemistry", "Elements", "Hard", 10),
    Question("Who painted the Mona Lisa", "Art", "Renaissance", "Hard", 9),
    Question("In which year did World War II end", "History", "World War II", "Medium", 8),
    Question("What is the main component of Earth's atmosphere", "Environmental Science", "Atmosphere", "Easy", 4),
    # Add more questions as needed
]

question_paper_generator = QuestionPaperGenerator(question_store)

# Define difficulty distribution
difficulty_distribution = {"Easy": 20, "Medium": 50, "Hard": 30}

# Generate a question paper with a total of 100 marks
generated_question_paper = question_paper_generator.generate_question_paper(100, difficulty_distribution)

# Print the generated question paper
for question in generated_question_paper:
    print(f"Question: {question.question}, Difficulty: {question.difficulty}, Marks: {question.marks}")
