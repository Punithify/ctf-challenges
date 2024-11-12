from flask import Blueprint,Flask, jsonify, render_template, request, redirect, url_for
import os

demo_page = Blueprint("demo", __name__, static_folder="../static", template_folder="../templates/demo")

@demo_page.route('/')
def index():
    return render_template('demo.html')
