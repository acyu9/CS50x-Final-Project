# Chemistry Website
#### <https://chemistry-website.onrender.com>

## Description:
The goals of this project are to create a website that contain tools for my Chemistry students and to learn and practice different concepts on each webpage.

### layout.html:
This page contains the html layout for other html pages. It contains the basics, such as Bootstap and CSS links, as well as navigation bar to allow users to access different pages no matter what page they are on.

This page reduces redundancy on other html pages.

### index.html:
This is the homepage of the website. It provides a panel of fun testimonials to showcase why students should take Chemistry. Besides the navigation bar at the top, there is a fortune-cookie style message that changes every time the page is refreshed.

These messages are saved in encouragement.txt to abstract away the details for cleaner code on app.py. The txt file is read as string then converted back to list via json. The message is then flashed to the homepage in a random order.

### pomodoro.html:
The purpose of this page is to provide the digital version of the pomodoro study technique, where a timer is set and the user studies for that period of time. Unlike the traditional pomodoro where each study session is 25 minutes, this app allows students to choose their own time.

Because the timer relies on user to set the initial time, AJAX and Javascript are utilized in addition to Python. In app.py, user input is sent to the server side, where the data is then converted to int to allow the calculation of total time. This data is then returned to the client side via jsonify.

Initially, the timer calculation and user input validation are coded on the server side as I would like to have more practice with Python. However, I later realize that because my timer needs to be updated every second and AJAX request only sends once with every request, I end up coding these functionalities with Javascript on the client side instead.

In pomodoro.html, the timer function calculates the hours, minutes, and seconds as the timer updates. The setInterval function loads the timer every 1 second to sync with the actual second passing by. The load timer function is where the user input is validated to ensure there is an input and there is no negative number. When AJAX call is successful, the timer is updated and displayed in the same input field, until the timer reaches 0 time.

The cancel button does not cancel the timer, because Javascript does not allow the loop to be stopped with a button click. Also, it adds a little humor and motivation for students to keep going till the timer ends. 

The form contains min and max settings for the time to have better control of what users input.

### studySkills.html:
This page contains a self-assessment for student's study skills.

Again, the study skills are abstracted away in a separate txt file, studySkills.txt, to make app.py cleaner. Button texts are set in app.py to practice more Python and keep the studySkills.html cleaner.

The studySkills.html utilizes Jinja to allow easier addition of each study skills sentence and buttons to the table.

A short section of Javascript is added to change the color of button based on clicking once or clicking twice. It makes this page more interactive and easier to see the user's choices.

### quiz.html:
This page contains a mini quiz for students to test themselves. Students must answer all questions and a message will be displayed at the top whether they pass or not. The correct answers will not be shown to encourage students to study more.

Since the quiz questions come in question-answer pair, a dictionary is chosen to pair up the key and value. This is abstract away in the quiz.txt file.

Besides converting string back to dictionary when the file is read in app.py, a deepcopy of the file is made to avoid accidentally changing the original copy.

A shuffle function is written to shuffle the questions and random is imported to shuffle answers. This a good practice on Python. All the correct answers are set to be the first answer choice before shuffling to make checking user inputs easier. Markup is used to safely send the message to the html page.

On quiz.html, a nested for-loop and Jinja are used to easily set up the quiz table.

### chatBot.html:
This page is to introduce my students to the famous rubber duck debugger tool in the CS world. 

The original idea is to utilize machine learning for the duck to generate a variation of quacks. Unfortunately, too many bugs are encountered with the chatterbot package. I also realize since my goal is not to tailor a specific type of quack with what the student inputs, machine learning is not actually required. I then proceed to create a list of quacks to be inserted randomly; however, VS Code does not recognize Jinja double-bracket notation in Javascript. Although there is a way around this with certain setting, I decide to stay with the traditional duck response, the one simple quack.

On the html page, Javascript is written to first attach user and duck images next to their input fields. Then insert each user and duck texts into a chatbox. Because the user input stays in the field after submitting, a short code is written to clear the field every time the user submits input. User input is also checked to see if it's blank so it a blank line doesn't pop up in the chatbox.

### CSS:
There are 2 CSS files in this project. The main CSS file is Thomas Park's Minty Theme. It is a beautiful Boostrap theme that helps me save a lot of time formatting my own CSS. This file is edited to remove functions not utlized in this project.

The other file is custom.css to override the mintytheme.css file to add in new design, such as the testimonial boxes on the homepage, and adapt certain designs better to my website.

### images files:
The image files in the static folder make the website more visiually pleasing and fun. For example, the pomodoro timer shakes if the mouse hovers over it. 
