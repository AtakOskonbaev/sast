import os
import sqlite3
from flask import Flask, request, make_response

app = Flask(__name__)

# Hardcoded secret (Sensitive Data Exposure)
SECRET_KEY = 'hardcoded_super_secret_key'
PASSWORD = 'skysoc'

@app.route('/unsafe_sql', methods=['GET'])
def unsafe_sql():
    user_id = request.args.get('user_id')

    # SQL Injection vulnerability (with unsanitized input)
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE id = '%s'" % user_id
    cursor.execute(query)
    result = cursor.fetchall()
    conn.close()

    return str(result)

@app.route('/os_command', methods=['GET'])
def os_command():
    cmd = request.args.get('cmd')

    # OS Command Injection vulnerability
    os.system(cmd)

    return "Command executed: " + cmd

@app.route('/xss', methods=['GET'])
def reflected_xss():
    name = request.args.get('name', '')

    # Reflected XSS vulnerability
    return f"<h1>Hello {name}</h1>"

@app.route('/path_traversal', methods=['GET'])
def path_traversal():
    filepath = request.args.get('filepath', '')

    # Path Traversal vulnerability
    with open('/var/data/' + filepath, 'r') as file:
        data = file.read()

    return data

    

@app.route('/insecure_cookie', methods=['GET'])
def insecure_cookie():
    resp = make_response("Setting insecure cookie")
    # Insecure cookie with no flags
    resp.set_cookie('sessionid', '123456')

    return resp

@app.route('/open_redirect', methods=['GET'])
def open_redirect():
    url = request.args.get('url', '/')
    
    # Open Redirect vulnerability
    return f'<a href="{url}">Click here</a>'

if __name__ == '__main__':
    # Debug mode exposes code execution via Werkzeug debugger
    app.run(debug=True, host='0.0.0.0')
