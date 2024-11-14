from flask import Blueprint,Flask, jsonify, render_template, request, redirect, url_for

auth_page = Blueprint("authpage", __name__, static_folder="../static", template_folder="../templates/authpage")

@auth_page.route('/')
def index():
    return render_template('authpage.html')
  
@auth_page.route("/login", methods=["POST"])
def api_login():
    data = request.get_json()
    password = data.get("password")
    
    if password == "letmeinnnnnnnnNMNMNnnnn":
        return jsonify({"message": "CTF{Client_Auth_Logic_bad_bad}"})
    else:
        return jsonify({"message": "Nuh uh"})