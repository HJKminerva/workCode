from flask import Flask, jsonify, request, abort 
app = Flask(__name__)

# 模拟用户数据
users = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"}
]

# GET /api/users：获取所有用户
@app.route('/api/users', methods=['GET'])
def get_users():
    return jsonify(users)

# GET /api/users/<int:id>：获取特定用户
@app.route('/api/users/<int:id>', methods=['GET'])
def get_user(id):
    user = next((u for u in users if u['id'] == id), None)
    if user is None:
        abort(404, description="User not found")
    return jsonify(user)

# POST /api/users：创建新用户
@app.route('/api/users', methods=['POST'])
def create_user():
    if not request.json or not 'name' in request.json or not 'email' in request.json:
        abort(400, description="Invalid request")
    new_user = {
        "id": users[-1]['id'] + 1 if users else 1,
        "name": request.json['name'],
        "email": request.json['email']
    }
    users.append(new_user)
    return jsonify(new_user), 201

# PUT /api/users/<int:id>：更新用户信息
@app.route('/api/users/<int:id>', methods=['PUT'])
def update_user(id):
    user = next((u for u in users if u['id'] == id), None)
    if user is None:
        abort(404, description="User not found")
    user['name'] = request.json.get('name', user['name'])
    user['email'] = request.json.get('email', user['email'])
    return jsonify(user)

# DELETE /api/users/<int:id>：删除用户
@app.route('/api/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    global users
    users = [u for u in users if u['id'] != id]
    return '', 204

# 启动服务器
if __name__ == '__main__':
    app.run(debug=True)