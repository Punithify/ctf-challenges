from flask import Blueprint,Flask, render_template

hades_cloak_page = Blueprint("hades_cloak", __name__, static_folder="../static", template_folder="../templates/hades_cloak")

@hades_cloak_page.route('/')
def index():
    return render_template('hades_cloak.html')
