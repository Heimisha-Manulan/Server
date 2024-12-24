# from flask import Blueprint, request, jsonify
# from sqlalchemy.orm import Session
# from database.mysql_database import get_session  # פונקציה שמחזירה סשן של SQLAlchemy
# from services.client_service import create_client, get_client_by_id, update_client, delete_client

# client_bp = Blueprint('client', __name__, url_prefix='/clients')

# @client_bp.route('/', methods=['POST'])
# def add_client():
#     """API להוספת לקוח חדש"""
#     data = request.json
#     with db.get_session() as session:
#         client = create_client(
#             session,
#             first_name=data['first_name'],
#             last_name=data['last_name'],
#             address=data['address'],
#             mail=data['mail'],
#             phone=data['phone'],
#             referred_by=data.get('referred_by', None)
#         )
#         return jsonify({"message": "Client added", "client": repr(client)}), 201

# @client_bp.route('/<int:client_id>', methods=['GET'])
# def get_client(client_id):
#     """API לשליפת פרטי לקוח"""
#     with get_session() as session:
#         client = get_client_by_id(session, client_id)
#         if not client:
#             return jsonify({"message": "Client not found"}), 404
#         return jsonify({"client": repr(client)})

# @client_bp.route('/<int:client_id>', methods=['PUT'])
# def update_client_route(client_id):
#     """API לעדכון פרטי לקוח"""
#     data = request.json
#     with get_session() as session:
#         client = update_client(session, client_id, **data)
#         if not client:
#             return jsonify({"message": "Client not found"}), 404
#         return jsonify({"message": "Client updated", "client": repr(client)})

# @client_bp.route('/<int:client_id>', methods=['DELETE'])
# def delete_client_route(client_id):
#     """API למחיקת לקוח"""
#     with get_session() as session:
#         client = delete_client(session, client_id)
#         if not client:
#             return jsonify({"message": "Client not found"}), 404
#         return jsonify({"message": "Client deleted"})
