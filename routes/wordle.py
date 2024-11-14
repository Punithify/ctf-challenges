from flask import Blueprint,Flask, jsonify, render_template, request

wordle_page = Blueprint("wordle", __name__, static_folder="../static", template_folder="../templates/wordle")

CORRECT_ANSWER = ["wireguard", "openvpn", "ikev2", "softether", "pptp", "l2tp", "ipsec", "sstp"]

@wordle_page.route('/')
def index():
    return render_template('wordle.html')
  
@wordle_page.route('/check', methods=['POST'])
def check_answer():
    data = request.get_json()
    user_answer = data.get('answer')

    # Check if the answer is correct
    if user_answer.lower() in CORRECT_ANSWER:
        return jsonify({"message": "CTF{YaY_Lets-Fly}"})
    else:
        return jsonify({"message": "Incorrect answer. Try again!"})