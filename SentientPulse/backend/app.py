from flask import Flask, request, jsonify, session
from flask_cors import CORS
from services.pulse_service import PulseService
from database.database import Database
import os

app = Flask(__name__)
app.secret_key = "pulse_ai_secret_key_2026" # Change this to anything secret
CORS(app, supports_credentials=True) # Essential for sessions

db = Database()
pulse_ai = PulseService()

# --- 1. SIGNUP ROUTE ---
@app.route('/api/signup', methods=['POST'])
def signup():
    data = request.json
    try:
        conn = db.get_connection()
        cursor = conn.cursor()
        
        query = "INSERT INTO users (name, email, password, dob) VALUES (%s, %s, %s, %s)"
        values = (data['name'], data['email'], data['password'], data['dob'])
        
        cursor.execute(query, values)
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({"message": "Account created successfully!"}), 201
    except Exception as e:
        return jsonify({"error": "Email already exists or database error"}), 400

# --- 2. LOGIN ROUTE ---
@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    try:
        conn = db.get_connection()
        cursor = conn.cursor(dictionary=True) # Returns data as a Dict
        
        query = "SELECT id, name, email FROM users WHERE email = %s AND password = %s"
        cursor.execute(query, (data['email'], data['password']))
        user = cursor.fetchone()
        
        if user:
            # Store user in session
            session['user_id'] = user['id']
            session['user_name'] = user['name']
            return jsonify({"message": "Login successful", "user": user}), 200
        else:
            return jsonify({"error": "Invalid email or password"}), 401
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# --- 3. CHAT ROUTE (Updated to use Session) ---
@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    user_text = data.get('message')
    # Get user_id from session or default to 1 for testing
    user_id = session.get('user_id', 1)

    result = pulse_ai.get_pulse_response(user_text)
    if result:
        result['user_text'] = user_text
        result['user_id'] = user_id
        db.save_chat_log(result)
        return jsonify(result)
    
    return jsonify({"error": "AI failed"}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)