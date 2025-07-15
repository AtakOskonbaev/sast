import os
import sqlite3
from flask import Flask, request

app = Flask(__name__)

# Hardcoded secret (Sensitive Data Exposure)
SECRET_KEY = 'my_super_secret_key_123'

@app.route('/unsafe_sql', methods=['GET'])
def unsafe_sql():
    user_id = request.args.get('user_id')
    
    # SQL Injection vulnerability
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE id = '{user_id}'"
    cursor.execute(query)
    result = cursor.fetchall()
    conn.close()
    
    return str(result)

@app.route('/os_command', methods=['GET'])
def os_command():
    filename = request.args.get('filename')

    # OS Command Injection vulnerability
    os.system(f"cat {filename}")

    return "Command executed"

@app.route('/xss', methods=['GET'])
def reflected_xss():
    name = request.args.get('name', '')
    
    # Reflected XSS vulnerability
    return f"<h1>Hello {name}</h1>"

@app.route('/path_traversal', methods=['GET'])
def path_traversal():
    filepath = request.args.get('filepath', '')

    # Path Traversal vulnerability
    with open(f'/var/data/{filepath}', 'r') as file:
        data = file.read()

    return data

if __name__ == '__main__':
    app.run(debug=True)
