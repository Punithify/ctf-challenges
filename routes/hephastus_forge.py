from flask import Blueprint, Flask, render_template, Response, abort, request, send_from_directory, make_response

hephastus_forge_page = Blueprint("hephastus_forge", __name__, static_folder="../static", template_folder="../templates/hephastus_forge")


@hephastus_forge_page.route('/')
def index():
    response = make_response(render_template('hephastus_forge.html'))
    response.set_cookie('forge_location', 'mount_olympus', max_age=60*60*24*30)
    
    return response
  
  
@hephastus_forge_page.route('mount_olympus', methods=['HEAD'])
def handle_head_request():
    response = Response()
    
    response.headers['Content-Type'] = 'text/html'
    response.headers['Content-Length'] = '1024'
    response.headers['Last-Modified'] = 'Mon, 01 Nov 2024 12:00:00 GMT'
    
    response.headers["box_key"] = 'hx*7sdmk_987'
    
    print("head triggered")

    return response
  
  
@hephastus_forge_page.route('/spawn', methods=['GET'])
def download_file():
    key = request.args.get('key')

    if key != 'hx*7sdmk_987':
        abort(403)  

    filename = 'archive/pandoras_box.zip' 
    try:
        return send_from_directory(hephastus_forge_page.static_folder, filename, as_attachment=True)
    except FileNotFoundError:
        abort(404)  # Not found if the file doesn't exist