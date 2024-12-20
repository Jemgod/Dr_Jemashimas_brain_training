#Dr Jemashima's Brain Training
# This Version has been scripted in python 3.12.4

import random

def generate_question(): #This is what we will use to generate the questions, with the below picking a random integer from 1 to 10.
    num1 = random.randint(1, 10) 
    num2 = random.randint(1, 10)

    operation = random.choice(['+', '-', '*', '/']) #This will randomly select an operation.

    if operation == '/':
        num1 = num1 * num2 #This makes sure that the number is divisible by the other number.
    question = f"{num1} {operation} {num2}" #This is what the question will look like e.g 8 - 6.
    correct_answer = eval(question) #This will evaluate the question and return the correct answer.
    return question, correct_answer

def main():
    correct_count = 0
    incorrect_count = 0

    while True: #This is an infinite loop, which will keep asking the user for input until they decide to quit.
        question, correct_answer = generate_question()
        print(f"Question: {question}")

        try: #This will try to get the users answer.
            
            user_answer = float(input("Please type your answer or type exit to end: ")) #End will allow the loop to be ended.
            if user_answer == correct_answer:
                print("Correct!")
                correct_count += 1 #This increases the correct score by 1.
            
            else:
                print(f"Incorrect. \nThe correct answer is {correct_answer} .\n Try Again!")
                incorrect_count += 1 #This increases the incorrect score by 1.
            
        except ValueError: #This will catch the ValueError if the user types something that isn't a number.
            user_input = input("Do you wish to continue? (yes/no): ")
            if user_input.lower() == "yes":
                continue
            else:
                break

    print("Game over, thank you for playing! \nCorrect Answers: ", {correct_count}, "\nIncorrect Answers: ", {incorrect_count})
    
if __name__ == "__main__": 
    print("Welcome to Dr Jameashima's Brain Training \nAnswer the equations or type exit to end the game.")
    main()


