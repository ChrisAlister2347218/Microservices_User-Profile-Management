from flask import Blueprint, request, jsonify
from . import db
from .models import User

bp = Blueprint('routes', __name__)

@bp.route('/', methods=['GET'])
def index():
    return "Welcome to the User Profile Management System!"

@bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    user = User(username=data['username'], email=data['email'], password=data['password'])
    db.session.add(user)
    db.session.commit()
    return jsonify(user.serialize()), 201

@bp.route('/users', methods=['GET'])
def list_users():
    users = User.query.all()
    return jsonify([user.serialize() for user in users])

@bp.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    user = User.query.get(id)
    if user is None:
        return jsonify({'error': 'User not found'}), 404
    return jsonify(user.serialize())

@bp.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    data = request.get_json()
    user = User.query.get(id)
    if user is None:
        return jsonify({'error': 'User not found'}), 404
    user.username = data['username']
    user.email = data['email']
    user.password = data['password']
    db.session.commit()
    return jsonify(user.serialize())

@bp.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get(id)
    if user is None:
        return jsonify({'error': 'User not found'}), 404
    db.session.delete(user)
    db.session.commit()
    return '', 204
