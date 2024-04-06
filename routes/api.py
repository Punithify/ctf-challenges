from flask import jsonify, request, abort, Blueprint, current_app
from functools import wraps
from datetime import datetime, timedelta
import jwt  # Import PyJWT

# Create a Blueprint for the API endpoints
api_page = Blueprint("api_page", __name__)

# Decorator for authentication
def require_auth(role):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Get the token from the Authorization header
            token = request.headers.get('Authorization')

            # Check if the token is present
            if not token:
                abort(401)

            try:
                # Decode the token
                data = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=['HS256'])
                # Check if the decoded token has the required role
                if data['role'] != role:
                    abort(403)
            except jwt.DecodeError:
                abort(401)

            # Call the endpoint function if authentication is successful
            return func(*args, **kwargs)
        return wrapper
    return decorator

# Authentication endpoint
@api_page.route('/auth', methods=['POST'])
def authenticate():
    # Get username and password from request body
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Allow any username and password
    if username and password:
        # Check if the username is 'admin'
        if username == 'admin':
            # Generate a JWT token with role=admin
            token = jwt.encode({'role': 'admin', 'exp': datetime.utcnow() + timedelta(minutes=30)}, current_app.config['SECRET_KEY'], algorithm='HS256')
            return jsonify({'token': token})
        else:
            # Generate a JWT token with role=normal
            token = jwt.encode({'role': 'normal', 'exp': datetime.utcnow() + timedelta(minutes=30)}, current_app.config['SECRET_KEY'], algorithm='HS256')
            return jsonify({'token': token})
    else:
        # Return 401 Unauthorized if username or password is missing
        abort(401)

# Admin endpoint - requires admin role
@api_page.route('/admin', methods=['GET'])
@require_auth('admin')
def admin_endpoint():
    # Return the flag if authentication is successful
    return jsonify({'flag': 'CTF{Congratulations! You have obtained the flag as an admin.}'})

# Normal user endpoint - requires normal role
@api_page.route('/normal', methods=['GET'])
@require_auth('normal')
def normal_endpoint():
    # Return a message indicating that the user is not authorized to get the flag
    return jsonify({'message': 'You need to be an admin to get the flag.'})
