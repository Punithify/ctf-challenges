from flask import Flask, render_template, request, jsonify,make_response,send_from_directory
from routes.hidden_js import hidden_js_page
from routes.hermes_cloak import hermes_cloak_page

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'



app.register_blueprint(hidden_js_page,url_prefix="/hidden_js")
app.register_blueprint(hermes_cloak_page,url_prefix="/hermes_cloak")


@app.route('/')
def index():
    return render_template('index.html')
    
    
@app.route('/robots.txt')
def robots_txt():
    return send_from_directory(app.root_path, 'robots.txt')



if __name__ == '__main__':
    app.run(debug=True)