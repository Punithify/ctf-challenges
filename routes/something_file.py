from flask import Blueprint, send_from_directory

something_file_page = Blueprint('static_files', __name__)

@something_file_page.route('/donotgo/whywillyou/9HxjWZQVYK3eS6rD.txt')
def serve_static():
    return send_from_directory('static', "9HxjWZQVYK3eS6rD.txt")

