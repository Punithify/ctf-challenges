from flask import Flask, render_template, request, jsonify,make_response,send_from_directory
from routes.biscuit import biscuit_page
from routes.js_password import js_password_page
from routes.something_file import something_file_page
from routes.come_back import come_back_page
from routes.test import test_page
from routes.api import api_page
from routes.feedback_form import feedback_form_page
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

app.register_blueprint(biscuit_page,url_prefix="/biscuit")
app.register_blueprint(js_password_page,url_prefix="/js_password")
app.register_blueprint(something_file_page)
app.register_blueprint(come_back_page,url_prefix="/come_back")
# app.register_blueprint(come_back_page,url_prefix="/come_back")
app.register_blueprint(test_page,url_prefix="/test")
app.register_blueprint(api_page,url_prefix="/api")
app.register_blueprint(feedback_form_page,url_prefix="/feedback_form")








@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/robots.txt')
def robots_txt():
    return send_from_directory(app.root_path, 'robots.txt')


if __name__ == '__main__':
    app.run(debug=True)
