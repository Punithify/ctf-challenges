from flask import Blueprint, render_template, request, jsonify, make_response
from dotenv import load_dotenv
import os

biscuit_page = Blueprint("biscuit", __name__, static_folder="static", template_folder="../templates/biscuit")

load_dotenv()

C1_FLAG_1 = os.getenv("C1_FLAG_1")

@biscuit_page.route('/')
def index():
    resp = make_response(render_template('biscuit.html'))
    resp.set_cookie('flag', C1_FLAG_1)
    return resp
    
@biscuit_page.route('/punith')
def punith():
    return render_template('punith.html')

@biscuit_page.route('/api/validateFlag', methods=['GET'])
def validate_flag():
    flag = request.args.get('flag')
    correct_flag = C1_FLAG_1 
    image_url = 'https://sund-images.sunnxt.com/72235/1600x1200_Raajakumara_72235_fe14c09e-ef3c-444e-9cb0-edbfe241b28c.jpg' 

    if flag.lower() == correct_flag:
        return jsonify({'success': True, 'imageURL': image_url})
    else:
        return jsonify({'success': False})
