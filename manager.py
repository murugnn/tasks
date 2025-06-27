from flask import Flask, request, jsonify

app = Flask(__name__)

users = {}
user_id_counter = 1

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users), 200

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if user:
        return jsonify(user), 200
    return jsonify({"error": "User not found"}), 404

@app.route('/users', methods=['POST'])
def create_user():
    global user_id_counter
    data = request.json
    if not data.get('name') or not data.get('email'):
        return jsonify({"error": "Name and email are required"}), 400
    users[user_id_counter] = {
        "id": user_id_counter,
        "name": data['name'],
        "email": data['email']
    }
    user_id_counter += 1
    return jsonify(users[user_id_counter - 1]), 201

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.json
    user = users.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    user.update({
        "name": data.get("name", user["name"]),
        "email": data.get("email", user["email"])
    })
    return jsonify(user), 200

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id in users:
        del users[user_id]
        return jsonify({"message": "User deleted"}), 200
    return jsonify({"error": "User not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
