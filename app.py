from flask import Flask, request, render_template, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Database connection configuration
db_config = {
    'host': 'localhost',           # Database host, typically 'localhost'
    'user': 'root',                # Replace with your database username
    'password': 'Abhishek@1259',   # Replace with your database password
    'database': 'test'             # Replace with your database name
}

# Route to render the registration form
@app.route('/')
def register_form():
    return render_template('register.html')

# Route to handle form submission for registration
@app.route('/submit_registration', methods=['POST'])
def submit_registration():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    salary = request.form['salary']
    gender = request.form['gender']

    # Connect to the existing MySQL database
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    try:
        cursor.execute('INSERT INTO users (name, email, password, salary, gender) VALUES (%s, %s, %s, %s, %s)', 
                       (name, email, password, salary, gender))
        conn.commit()
    except mysql.connector.IntegrityError:
        return "Email already registered. Please use a different email."
    finally:
        cursor.close()
        conn.close()

    return redirect(url_for('register_form'))

# Route to render the update form
@app.route('/update')
def update_form():
    return render_template('update.html')

# Route to handle form submission for updating salary
@app.route('/submit_update', methods=['POST'])
def submit_update():
    salary = request.form['salary']
    name = request.form['name']

    # Connect to the existing MySQL database
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    try:
        # Update the user's salary based on the name provided
        cursor.execute('UPDATE users SET salary = %s WHERE name = %s', (salary, name))
        conn.commit()
    finally:
        cursor.close()
        conn.close()

    return redirect(url_for('update_form'))

if __name__ == '__main__':
    app.run(debug=True)
