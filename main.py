from flask import Flask, request, redirect, render_template
import cgi


app = Flask(__name__)

app.config['DEBUG'] = True   

@app.route("/")
def index():
    something = 5
    return render_template('home.html')

@app.route("/welcome", methods=['POST'])
def welcome():
    error1 = ''
    error2 = ''
    error3 = ''
    error4 = ''
    user = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']
    validEmail = True
    emailCheck = False
    andCount = 0
    periodCount = 0
    emailError = ''
    if len(user) > 20 or len(user) < 3:
        error1 = 'Must be between 3 and 20 characters'
    if len(password) > 20 or len(password) < 3:
        error2 = 'Must be between 3 and 20 characters'
    if len(verify) > 20 or len(verify) < 3:
        error3 = 'Must be between 3 and 20 characters'
    if len(email) > 20 or len(email) < 3:
        error4 = 'Must be between 3 and 20 characters'
    if password != verify:
        error3 = "Passwords do not match!"
    if user == '':
        error1 = 'Must type a username'
    if password == '':
        error2 = 'Must type a password'
    if verify == '':
        error3 = 'Must verify password'

    if len(email) > 0:
        while validEmail == True and emailCheck == False:
            for character in email:
                if character == ' ':
                    validEmail = False
                    emailError = 'No Spaces in Emails'
                if character == '@':
                    andCount +=1
                    if andCount > 1:
                        validEmail = False
                        emailError = 'Too many @ signs'
                if character == '.':
                    periodCount += 1
                    if periodCount > 1:
                        validEmail = False
                        emailError = 'Too many periods'
                        
            emailCheck = True
    if validEmail == False:
        error4 = emailError
    if error1 == '' and error2 == '' and error3 == '' and error4 == '':   
        return render_template('welcome.html', username=user)
    else:
        return render_template('home.html', username=user, email=email, error1=error1, error2=error2, error3=error3, error4=error4)

app.run()

