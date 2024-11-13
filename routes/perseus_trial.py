from flask import Blueprint, Flask, render_template, Response, abort, request, send_from_directory, make_response

perseus_trial_page = Blueprint("perseus_trial", __name__, static_folder="../static", template_folder="../templates/perseus_trial")


@perseus_trial_page.route('/')
def index():
    response = make_response(render_template('perseus_trial.html'))
    response.set_cookie('medusa_location', 'gorgons_lair', max_age=60*60*24*30)  
    return response
  
  
@perseus_trial_page.route('gorgons_lair', methods=['HEAD'])
def handle_head_request():
    response = Response()
    
    response.headers['Content-Type'] = 'text/html'
    response.headers['Content-Length'] = '1024'
    response.headers['Last-Modified'] = 'Mon, 01 Nov 2024 12:00:00 GMT'
    
    response.headers["divine_blessing"] = "Ath3na's_P0l1sh3d_Shi3ld"
    
    print("head triggered")

    return response
  
  
@perseus_trial_page.route('spawn', methods=['GET'])
def download_file():
    blessing = request.args.get('blessing')

    if blessing != "Ath3na's_P0l1sh3d_Shi3ld":
        abort(403)  

    filename = 'archive/medusas_head.zip' 
    try:
        return send_from_directory(perseus_trial_page.static_folder, filename, as_attachment=True)
    except FileNotFoundError:
        abort(404)  # Not found if the file doesn't exist