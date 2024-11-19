#Exercise 8 : Star Wars Quiz
#Instructions
#This project allows users to take a quiz to test their Star Wars knowledge.
#The number of correct/incorrect answers are tracked and the user receives different messages depending on how well they did on the quiz.

#Here is an array of dictionaries, containing those questions and answers

data = [
    {
        "question": "What is Baby Yoda's real name?",
        "answer": "Grogu"
    },
    {
        "question": "Where did Obi-Wan take Luke after his birth?",
        "answer": "Tatooine"
    },
    {
        "question": "What year did the first Star Wars movie come out?",
        "answer": "1977"
    },
    {
        "question": "Who built C-3PO?",
        "answer": "Anakin Skywalker"
    },
    {
        "question": "Anakin Skywalker grew up to be who?",
        "answer": "Darth Vader"
    },
    {
        "question": "What species is Chewbacca?",
        "answer": "Wookiee"
    }
]


#Create a function that asks the questions to the user, and check his answers. Track the number of correct, incorrect answers. Create a list of wrong_answers

def main():
    score = 0
    incorrect_answers = []

    for item in data:
        result = question_asker(item['question'], item['answer'])

    if result[0] == 'correct':
        score +=1
        print('You got it')
        print(f'youre scor is {score}')

    else:
        print('you got it wrong. Go rewatch.')
        print(f'your score is {score}')
        incorrect_answers.append(result[1])
        print(f'you have {3 - len(incorrect_answers)} chances left.')  
        print(f'the correct answer was {item['answer']}, you answered {incorrect_answers[-1]['user_answer']}')         
    
    if len(incorrect_answers) >=  3:
        Print('you lose!')
        return

def question_asker(question, answer):
    user_answer = input(question)

    if user_answer.lower() == answer.lower():
        return ('correct', {question, answer})
    else:
        return ('incorrect', {question, user_answer})

main()

#Create a function that informs the user of his number of correct/incorrect answers.



#Bonus : display to the user the questions he answered wrong, his answer, and the correct answer.
#If he had more then 3 wrong answers, ask him to play again.
