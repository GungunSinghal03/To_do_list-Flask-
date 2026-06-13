from flask import Blueprint, render_template, request, redirect, url_for, flash, session

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

# In production, use a database instead of hardcoded credentials
USER_CREDENTIALS = {
    "admin": "1234"
}
# Add this to app/routes/auth.py
@auth_bp.route('/')
def home():
    if 'user' in session:
        return redirect(url_for('tasks.view_tasks'))
    return redirect(url_for('auth.login'))
@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
            session['user'] = username
            flash('Login Successful!', 'success')
            return redirect(url_for('tasks.view_tasks'))
        else:
            flash('Invalid Username or Password!', 'danger')
    
    return render_template('login.html')

@auth_bp.route('/logout')
def logout():
    session.pop('user', None)
    flash('Logged Out Successfully!', 'info')
    return redirect(url_for('auth.login'))

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Add registration logic here
        flash('Registration feature coming soon!', 'info')
        return redirect(url_for('auth.login'))
    
    return render_template('register.html')