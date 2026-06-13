from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from app import db
from app.models import Task

# Change this line - remove the url_prefix
tasks_bp = Blueprint('tasks', __name__)

@tasks_bp.route('/')
def view_tasks():
    if 'user' not in session:
        return redirect(url_for('auth.login'))
    
    tasks = Task.query.all()
    return render_template('tasks.html', tasks=tasks)

# Rest of your code remains the same...
@tasks_bp.route('/add', methods=['POST'])
def add_task():
        if 'user' not in session:
            return redirect(url_for('auth.login'))
    
        title = request.form.get('title')
        if title:
            new_task = Task(title=title, status="Pending")
            db.session.add(new_task)
            db.session.commit()
            flash('Task Added Successfully!', 'success')
    
        return redirect(url_for('tasks.view_tasks'))


@tasks_bp.route('/toggle/<int:task_id>', methods=['POST'])
def toggle_status(task_id):
        if 'user' not in session:
            return redirect(url_for('auth.login'))
    
        task = Task.query.get_or_404(task_id)
    
    # Cycle through statuses: Pending -> Working -> Done -> Pending
        status_cycle = {
        "Pending": "Working",
        "Working": "Done",
        "Done": "Pending"
    }

@tasks_bp.route('/clear', methods=['POST'])
def clear_tasks():
    if 'user' not in session:
        return redirect(url_for('auth.login'))
    
    Task.query.delete()
    db.session.commit()
    flash('All Tasks Cleared!', 'danger')
    return redirect(url_for('tasks.view_tasks'))

@tasks_bp.route('/delete/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    if 'user' not in session:
        return redirect(url_for('auth.login'))
    
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    flash('Task Deleted Successfully!', 'success')
    return redirect(url_for('tasks.view_tasks'))