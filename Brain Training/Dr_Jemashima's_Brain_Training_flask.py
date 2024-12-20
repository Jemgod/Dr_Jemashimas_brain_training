from flask import Flask, render_template, request, redirect, url_for, session #This is used to create a session for the web link connecting to the html files.
import random #random package is used to generate random numbers.
import time #time package is used to get the current time.

app = Flask(__name__)
app.secret_key = 'your_secret_key'  #This would be replaced with a random secret key in an actual application e.g a randomly generated hex token.

def generate_question(): #Function to generate a random question
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operation = random.choice(['+', '-', '*', '/'])

    if operation == '/': #To avoid division by zero.
        num1 = num1 * num2
    question = f"{num1} {operation} {num2}"
    correct_answer = eval(question)
    return question, correct_answer

@app.route('/', methods=['GET', 'POST']) #The main route for the web application.
def index():
    if 'score' not in session: #This makes sure the score is set to zero when logged in.
        session['score'] = 0  # Initialize score
        session['start_time'] = time.time()  # Record the start time

    if request.method == 'POST': #This is used to get the response back from the user.
        user_answer = request.form.get('answer')
        if user_answer is not None:
            try:
                user_answer = float(user_answer)
                correct_answer = float(request.form.get('correct_answer'))
                if user_answer == correct_answer:
                    session['score'] += 1  # Increment score for correct answer
                    feedback = "Correct!"
                else:
                    session['score'] -= 1  # Decrement score for incorrect answer
                    feedback = f"Incorrect. The correct answer is {correct_answer}."
            except ValueError:
                return redirect(url_for('index'))

    # Generate a new question after processing the answer
    question, correct_answer = generate_question()
    return render_template('index.html', question=question, correct_answer=correct_answer, score=session['score'], feedback=feedback if 'feedback' in locals() else None)

@app.route('/end', methods=['POST']) #This is used to end the quiz and see the results.
def end_game():
    score = session.get('score', 0)
    start_time = session.get('start_time', time.time())
    duration = time.time() - start_time  # Calculate duration in seconds
    duration_minutes = int(duration // 60)
    duration_seconds = int(duration % 60)
    
    message = ""
    if score > 10:
        message = "Well done! You have been practicing well!"
    elif score < -5:
        message = "It looks like you need more practice... Try again!"
    
    session.pop('score', None)  # Clear the score
    session.pop('start_time', None)  # Clear the start time
    return render_template('end.html', score=score, message=message, duration=f"{duration_minutes} minutes and {duration_seconds} seconds")

if __name__ == "__main__": #This is used to run the application.
    app.run(debug=True)