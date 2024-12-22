import json
import os
import re
from flask import Flask, render_template, request, redirect, url_for # type: ignore

app = Flask(__name__)

# Ensure passwords.json exists and is empty at the start
if not os.path.exists('passwords.json'):
    with open('passwords.json', 'w') as file:
        json.dump({}, file)

# Function to load passwords from the JSON file
def load_passwords():
    with open('passwords.json', 'r') as file:
        return json.load(file)

# Function to save passwords to the JSON file
def save_passwords(passwords):
    with open('passwords.json', 'w') as file:
        json.dump(passwords, file)

# Function to validate service name (only text or numbers and no more than 5 words)
def is_valid_service(service):
    # Check if the service name only contains letters, numbers, and spaces
    if not re.match(r'^[a-zA-Z0-9\s]+$', service):
        return False
    # Check if the service name has more than 5 words
    if len(service.split()) > 5:
        return False
    return True

# Home page showing saved passwords and the form to add new passwords
@app.route('/')
def index():
    saved_services = load_passwords()
    return render_template('index.html', saved_services=saved_services)

# Route to handle saving a new password
@app.route('/store', methods=['POST'])
def store_password():
    service = request.form['service']
    password = request.form['password']

    # Validate the service name
    if not is_valid_service(service):
        return "Invalid service name. It should contain only letters, numbers, and no more than 5 words.", 400

    saved_services = load_passwords()
    saved_services[service] = password
    save_passwords(saved_services)

    return redirect(url_for('index'))

# Route to handle deleting a password
@app.route('/delete/<service>', methods=['GET'])
def delete_password(service):
    saved_services = load_passwords()

    # Remove password if it exists
    if service in saved_services:
        del saved_services[service]

    # Save updated passwords
    save_passwords(saved_services)

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)