# SAVE BEFORE RUNNING FOR UPDATES

from flask import Flask, render_template, flash, request, jsonify, redirect, url_for
import random, copy
import json
from markupsafe import Markup

app = Flask(__name__)

# Key needed for session where flash message is stored
app.secret_key = 'super secret'

# Ensure responses aren't cached and have GET static 304 code
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# Shuffle function that takes the keys of the dictionary as argument
def shuffle(q):
    selected_keys = []
    i = 0
    while i < len(q):
        dict = list(q.keys())
        current_selection = random.choice(dict)
        if current_selection not in selected_keys:
            selected_keys.append(current_selection)
            i += 1
    return selected_keys


@app.route("/")
def index():
    # Read data from the file as str
    with open('static/encouragement.txt', encoding="utf-8") as f:
        messages = f.read()

    # Convert data to list
    encouragements = json.loads(messages)

    # Flash a random element from list
    flash(random.choice(encouragements))
    return render_template('index.html')


@app.route("/quiz.html", methods=["GET", "POST"])
def quiz():
    # Read data from the file as str
    with open('static\quiz.txt') as f:
        read = f.read()

    # Convert data to dict
    original_questions = json.loads(read)

    # Deepcopy so changes to the duplicated dict won't affect the original dict
    questions = copy.deepcopy(original_questions)

    # Shuffle questions
    questions_shuffled = shuffle(questions)

    # Shuffle answers
    for i in questions.keys():
        random.shuffle(questions[i])

    if request.method == "POST":
        correct = 0
        # Check user answers
        for i in questions.keys():
            answered = request.form[i]
            if original_questions[i][0] == answered:
                correct += 1

        if correct >= (len(original_questions) / 2):
            message = Markup("Congratulations! You have scored more than 50%. That's at least a 3 on the AP test!")
        else:
            message = Markup("You missed more than half. So sad. Better study more.")
        
        return render_template('quiz.html', message=message, shuffled = questions_shuffled, original = questions)

    else:
        return render_template('quiz.html', shuffled = questions_shuffled, original = questions)



# Get is for loading that page; Post is for submitting the "form" / set timer
@app.route("/pomodoro.html", methods=["GET", "POST"])
def pomodoro():

    if request.method == "POST":

        # Need to get user input and check if it's blank BEFORE casting; otherwise, get output None and NoneType error.
        hours = request.form.get("hours")
        minutes = request.form.get("minutes")
        seconds = request.form.get("seconds")

        #The server can not do a redirect from an ajax request.  
        # Redirect has to be done on client side, in the callback (JS).

        hours = int(hours)
        minutes = int(minutes)
        seconds = int(seconds)

        # Calculate total number of seconds from the user inputs
        totalTime = hours * 3600 + minutes * 60 + seconds

        return jsonify({'hours' : hours, 'minutes' : minutes, 'seconds' : seconds, 'totalTime' : totalTime})

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template('pomodoro.html')



@app.route("/studySkills.html")
def studySkills():
    # Read data from the file as str
    with open('static\studySkills.txt', encoding="utf-8") as f:
        read = f.read()

    # Convert data to list
    skills = json.loads(read)

    # Set button texts
    buttons = ["Often", "Sometimes", "Rarely"]
    return render_template('studySkills.html', buttons = buttons, skills = skills)


@app.route("/chatBot.html", methods=["GET", "POST"])
def chatBot():

    if request.method == "POST":
        # Get message from input box
        userText = request.form.get('userInput')

        return render_template('chatBot.html', userText=userText)
    
    else:
        return render_template('chatBot.html')

if __name__ == "__main__":
    app.run(debug=True)
