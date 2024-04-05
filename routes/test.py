from flask import Flask, render_template, request,Blueprint,Response,redirect
test_page = Blueprint("test", __name__, static_folder="static", template_folder="../templates/test_page")

@test_page.route('/')
def index():
    return render_template('test/index.html')
