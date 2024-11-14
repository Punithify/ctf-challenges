from flask import Flask, render_template, request, jsonify,make_response,send_from_directory
from routes.hidden_js import hidden_js_page
from routes.hades_cloak import hades_cloak_page
from routes.demo import demo_page
from routes.wordle import wordle_page
from routes.perseus_trial import perseus_trial_page
from routes.auth import auth_page

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'


app.register_blueprint(hidden_js_page, url_prefix="/veil_of_secrets")
app.register_blueprint(hades_cloak_page, url_prefix="/hades_cloak")
app.register_blueprint(demo_page, url_prefix="/demo")
app.register_blueprint(wordle_page, url_prefix="/lets_fly")
app.register_blueprint(perseus_trial_page, url_prefix="/perseus_trial")
app.register_blueprint(auth_page, url_prefix="/authpage")


@app.route('/')
def index():
    return render_template('index.html')
    
    
@app.route('/robots.txt')
def robots_txt():
    return send_from_directory(app.root_path, 'robots.txt')



if __name__ == '__main__':
    app.run(debug=True)