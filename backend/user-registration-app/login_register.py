from flask import Flask, request, jsonify
import mysql.connector
from mysql.connector import Error
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
CORS(app)

def connect_to_database():
    try:
        # 连接到数据库
        db = mysql.connector.connect(
            host='116.205.162.4',
            user='root',
            password='123456',
            database='hjk'
        )
        return db
    except Error as e:
        print(f"Error connecting to the database: {e}")
        return None

@app.route('/register', methods=['POST'])
def register_user():
    try:
        # 获取前端发送的数据
        data = request.get_json()
        print(f"获取到前端数据: {data}")
        # 检查必要字段是否存在
        if not data or 'username' not in data or 'password' not in data:
            return jsonify({'error': '用户名和密码是必填项'}), 400

        # 提取数据
        user = data.get('username')
        password = data.get('password')
        email = data.get('email')
        print(f"用户名: {user}, 密码: {password}, 邮箱: {email}")
        # 在这里进行用户注册的逻辑处理，将用户信息保存到数据库中
        # 链接数据库
        db = connect_to_database()
        if db is None:
            return jsonify({'error': '无法连接到数据库'}), 500
        else:
            print("成功连接到数据库")

        cursor = db.cursor()

        # 插入数据
        sql = "INSERT INTO user_account_information (username, password, email) VALUES (%s, %s, %s)"
        cursor.execute(sql, (user, password, email))
        db.commit()
        # 查询数据
        sql = "SELECT * FROM user_account_information"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)

        # 返回接收到的数据
        response_data = {
            'message': '注册成功',
            'data': {
                'user': user,
                'password': '******',  # 隐藏密码内容
                'email': email
            }
        }

        return jsonify(response_data), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 500

    finally:
        # 关闭游标和数据库连接
        if cursor:
            cursor.close()
        if db and db.is_connected():
            db.close()

@app.route('/login', methods=['POST'])
def login_user():
    db = None
    cursor = None
    try:
        # 获取前端发送的数据
        data = request.get_json()
        user = data.get('username')
        password = data.get('password')
        print(f"获取到用户名: {user} 密码: {password}")

        # 链接数据库
        db = connect_to_database()
        
        if db is None:
            return jsonify({'error': '无法连接到数据库'}), 500

        with db.cursor() as cursor:
            # 查询数据
            sql = "SELECT * FROM user_account_information WHERE username = %s and password = %s"
            cursor.execute(sql, (user,password))
            result = cursor.fetchone()
            print(f"从数据库中查询结果: {result}")

            # 检查用户是否存在
            if result is None:
                return jsonify({'error': '用户名或密码错误'}), 401

            # 检查密码是否正确
            stored_password = result[1]  # 假设密码是查询结果的第二个字段
            if stored_password != password:  # 如果数据库存储的是明文密码
                return jsonify({'error': '用户名或密码错误'}), 401

            # 登录成功
            response_data = {
                'message': '登录成功',
                'data': {
                    'user': user,
                    'password': password  # 假设邮箱是查询结果的第三个字段
                }
            }
            return jsonify(response_data), 200

    except Exception as e:
        print(f"服务器内部错误: {e}")  # 打印具体错误信息
        return jsonify({'error': '服务器内部错误'}), 500
    finally:
        # 关闭游标和数据库连接
        if cursor:
            cursor.close()
        if db and db.is_connected():
            db.close()

if __name__ == '__main__':
    app.run(debug=True)  # 生产环境中应设置为 False