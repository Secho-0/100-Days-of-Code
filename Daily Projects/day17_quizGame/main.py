
from data import question_data
import question_model as qm
from quiz_brain import QuizBrain

# Bake Questions
questions = []
for question in question_data:
    new_question = qm.Question(question["question"],question["correct_answer"])
    questions.append(new_question)

# Make Quiz Brain
quizbrain = QuizBrain(questions)

# Run the Quiz
while quizbrain.still_has_quesitons():
    quizbrain.get_question()
quizbrain.final_score()