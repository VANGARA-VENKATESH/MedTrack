from flask import Flask, render_template, request, redirect, url_for, session, flash
from datetime import datetime
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secure key in production

# Sample in-memory storage (you can later replace this with a database like SQLite or DynamoDB)
users = []
appointments = []

# ------------------------- Helpers -------------------------

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

# ------------------------- Routes -------------------------

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/homepage')
def homepage():
    return render_template('homepage.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        users.append({
            'name': request.form['name'],
            'email': request.form['email'],
            'password': request.form['password'],
            'role': request.form['role']
        })
        flash('Registration successful! Please login.')
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = next((u for u in users if u['email'] == email and u['password'] == password), None)
        if user:
            session['user'] = user
            flash(f"Welcome back, {user['name']}!")
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid credentials')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return render_template('logout.html')

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

@app.route('/doctor_dashboard')
@login_required
def doctor_dashboard():
    return render_template('doctor_dashboard.html')

@app.route('/patient_dashboard')
@login_required
def patient_dashboard():
    return render_template('patient_dashboard.html')

@app.route('/book_appointment', methods=['GET', 'POST'])
@login_required
def book_appointment():
    if request.method == 'POST':
        appointment = {
            'doctor': request.form['doctor'],
            'date': request.form['date'],
            'time': request.form['time'],
            'patient': session['user']['name'],
            'email': session['user']['email'],
            'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        appointments.append(appointment)
        flash('Appointment booked successfully.')
        return redirect(url_for('view_appointments'))
    return render_template('book_appointment.html')

@app.route('/view_appointments')
@login_required
def view_appointments():
    user = session['user']
    if user['role'] == 'doctor':
        doctor_appointments = [a for a in appointments if a['doctor'].lower().endswith(user['name'].lower())]
        return render_template('view_appointment_doctor.html', appointments=doctor_appointments)
    else:
        patient_appointments = [a for a in appointments if a['email'] == user['email']]
        return render_template('view_appointment_patient.html', appointments=patient_appointments)

@app.route('/view_appointment')
@login_required
def view_all_appointments():
    return render_template('view_appointment.html', appointments=appointments)

@app.route('/lab_results')
@login_required
def lab_results():
    return render_template('lab_results.html')

@app.route('/secure_complaint', methods=['GET', 'POST'])
@login_required
def secure_complaint():
    if request.method == 'POST':
        flash('Your complaint has been securely submitted.')
        return redirect(url_for('dashboard'))
    return render_template('secure_complaint.html')

@app.route('/smart_booking')
@login_required
def smart_booking():
    return render_template('smart_booking.html')

@app.route('/schedule')
@login_required
def schedule():
    return render_template('schedule.html')

@app.route('/messages_calls')
@login_required
def messages_calls():
    return render_template('messages_calls.html')

@app.route('/search_results')
def search_results():
    return render_template('search_results.html')

# ------------------------- Main -------------------------

if __name__ == '__main__':
    app.run(debug=True)
