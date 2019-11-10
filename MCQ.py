from Question import Question

question_prompts = [
    "What is the capital of India?\na) Mew Delhi\nb) Banglore\n",
    "What is the national bird of India?\na) Parrot\nb) Peacock\n"
]

questions = [
    Question(question_prompts[0],"a"),
    Question(question_prompts[1],"b")
]

def run_test(questions):
    score=0
    for question in questions:
        answer = input(question.question)
        if answer == question.answer:
            score = score + 1
    print("You got " + str(score) + "/" + str(len(questions)) + "correct.")

run_test(questions)


