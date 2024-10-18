from flask import Blueprint,Flask, jsonify, render_template, request, redirect, url_for
import os

hidden_js_page = Blueprint("hidden_js", __name__, static_folder="../static", template_folder="../templates/hidden_js")
scatter_text = os.environ.get('SCATTER_TEXT')

@hidden_js_page.route('/')
def index():
    scatter_text = os.environ.get('SCATTER_TEXT')
    return render_template('hidden_js.html', scatter_text=scatter_text)

@hidden_js_page.route('/get_scatter_text', methods=['POST'])
def get_scatter_text():
    # Serve the scatter text as a JSON response
    return jsonify({'scatter_text': scatter_text})
