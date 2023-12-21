from Question import Question

question_prompts = [
    "What is Muay Thai?\n(a) Grappling\n(b) Art of 8 Limbs\n(c) Stick fighting\n\n",
    "What is a Kimura?\n(a) A dance\n(b) A song\n(c) A submission\n\n",
    "What is the UFC?\n(a) Ultimate Fight Championship\n(b) Ultra Frisbee Competition\n(c) United Freedom Charter\n\n"
]

questions = [
    Question(question_prompts[0],"b"),
    Question(question_prompts[1],"c"),
    Question(question_prompts[2],"a"),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1

    print ("You got " + str(score) + "/" + str(len(questions)))

run_test(questions)