from flask import Blueprint,Flask, jsonify, render_template, request, redirect, url_for
import os

hermes_cloak_page = Blueprint("hermes_cloak", __name__, static_folder="../static", template_folder="../templates/hermes_cloak")

@hermes_cloak_page.route('/')
def index():
    return render_template('hermes_cloak.html')
