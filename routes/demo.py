from flask import Blueprint, Flask, render_template

demo_page = Blueprint("demo", __name__, static_folder="../static", template_folder="../templates/demo")

@demo_page.route('/')
def index():
    return render_template('demo.html')