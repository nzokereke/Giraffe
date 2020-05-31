class Question:
    def __init__(self, prompt, answer):   # attributes of class are 'prompt and 'answer'
        self.prompt = prompt
        self.answer = answer


questions_prompts = ['What is the colours of the Nigerian flag?\n(a) green/white/blue\n(b) green/black/white\n(c) '
                     'green/white/green\nenter',
                     'Name the capital of Nigeria\n(a) abuja\n(b) accra\n(c) lagos\nenter',
                     'Which of the following countries do not border Nigeria\n(a) ghana\n(b) chad\n(c) '
                     'cameroun\nenter '
                     ]
questions = [Question(questions_prompts[0], 'c'),
             Question(questions_prompts[1], 'a'),
             Question(questions_prompts[2], 'a')]


# score = 0


def run_test(questions):

    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print('you got ' + str(score) + '/' + str(len(questions)) + 'correct')


run_test(questions)
