from flask import Flask, render_template, request,Blueprint,Response,redirect,make_response
feedback_form_page = Blueprint("feedback_form_page", __name__, static_folder="static", template_folder="../templates/feedback_form")


import bleach  # For HTML sanitization

FLAG = "CTF{HTTP_only_cookie_flag}"

@feedback_form_page.route('/')
def index():
    return render_template('login_feedback.html')

# Login page
@feedback_form_page.route('/perform', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == 'password':
            # Set HTTP-only cookie with flag value upon successful login
            resp = make_response(render_template('logged_in.html'))
            resp.set_cookie("are_you_sure", "ctf{}", httponly=True, secure=True, samesite="Strict")
            return resp
        else:
            return render_template('login_feedback.html', message='Invalid credentials. Please try again.')
    return render_template('login.html')

# Page vulnerable to XSS
@feedback_form_page.route('/profile')
def profile():
    return render_template('profile.html')