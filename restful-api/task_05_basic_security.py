#!/usr/bin/python3
"""
Module for API security and authentication techniques.
"""
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity, get_jwt
)
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'your-secret-key-change-this'
jwt = JWTManager(app)
auth = HTTPBasicAuth()

users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}


@auth.verify_password
def verify_password(username, password):
    """
    Verifies basic authentication credentials.

    Args:
        username: The username
        password: The password

    Returns:
        str: The username if credentials are valid, None otherwise
    """
    if username in users and check_password_hash(
            users[username]['password'], password):
        return username
    return None


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """
    Handles unauthorized JWT errors.
    """
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """
    Handles invalid JWT token errors.
    """
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    """
    Handles expired JWT token errors.
    """
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    """
    Handles revoked JWT token errors.
    """
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    """
    Handles fresh token required errors.
    """
    return jsonify({"error": "Fresh token required"}), 401


@app.route('/basic-protected', methods=['GET'])
@auth.login_required
def basic_protected():
    """
    Basic authentication protected route.
    """
    return "Basic Auth: Access Granted"


@app.route('/login', methods=['POST'])
def login():
    """
    Login endpoint that returns a JWT token.
    """
    if not request.is_json:
        return jsonify({"error": "Invalid JSON"}), 400

    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if username not in users:
        return jsonify({"error": "Invalid credentials"}), 401

    if not check_password_hash(users[username]['password'], password):
        return jsonify({"error": "Invalid credentials"}), 401

    access_token = create_access_token(
        identity=username,
        additional_claims={"role": users[username]['role']}
    )
    return jsonify({"access_token": access_token})


@app.route('/jwt-protected', methods=['GET'])
@jwt_required()
def jwt_protected():
    """
    JWT protected route.
    """
    return "JWT Auth: Access Granted"


@app.route('/admin-only', methods=['GET'])
@jwt_required()
def admin_only():
    """
    Admin-only route protected by JWT and role check.
    """
    claims = get_jwt()
    role = claims.get('role')

    if role != 'admin':
        return jsonify({"error": "Admin access required"}), 403

    return "Admin Access: Granted"


if __name__ == '__main__':
    app.run()

