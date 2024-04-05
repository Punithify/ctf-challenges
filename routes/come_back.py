from flask import Flask, render_template, request,Blueprint,Response,redirect
come_back_page = Blueprint("come_back", __name__, static_folder="static", template_folder="../templates/come_back")

FLAG = "FLAG{example_flag}"
current_letter_index = 0
@come_back_page.route('/')
def index():
    return render_template('something.html')

@come_back_page.route('/next')
def next():
    global current_letter_index 
    current_letter = FLAG[current_letter_index]
    current_letter_index = (current_letter_index + 1) % len(FLAG)
    return serve_letter(current_letter)

def serve_letter(letter):
    response = Response(f"Content of letter {letter}", status=200, mimetype='text/plain')
    response.headers['X-Content-Type-Options'] = 'nosniff'  # Prevent MIME sniffing
    return response