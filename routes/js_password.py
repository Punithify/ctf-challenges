from flask import Flask, render_template, request,Blueprint
js_password_page = Blueprint("js_password", __name__, static_folder="static", template_folder="../templates/js_password")

@js_password_page.route('/')
def index():
    return render_template('login.html')

@js_password_page.route('/submit', methods=['POST'])
def submit():
    entered_password = request.form.get('password')

    correct_password = 'starlightflagpursuit'

    if entered_password == correct_password:
        return """<h1 class="text-center">correct</h1>"""
    else:
        return """<img src="https://miro.medium.com/v2/resize:fit:600/format:webp/0*NsfFeu-AcAPlBl6z.png">na</img>"""
