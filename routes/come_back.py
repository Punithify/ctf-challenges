from flask import Flask, render_template, request,Blueprint,Response,redirect
come_back_page = Blueprint("come_back", __name__, static_folder="static", template_folder="../templates/come_back")


# Define the word
word = "something"

@come_back_page.route('/')
def index():
    # Serve the HTML file
    return render_template('something.html')


@come_back_page.route('/file-content')
def file_content():
    global word
    # Check if there are characters left in the word
    if len(word) > 0:
        # Get the first character of the word
        char = word[0]
        # Remove the first character from the word
        word = word[1:]
        # Return the character
        return char
    else:
        # Return an empty response if all characters have been served
        return ""

