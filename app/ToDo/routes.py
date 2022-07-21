# import all the necessary library

from app.ToDo import main
from app import db
from app.ToDo.models import ToDos
from app.ToDo.forms import CreateToDo,EditToDoForm
from flask import render_template, request, flash, redirect, url_for
from flask_login import login_required


# company list display
@main.route('/todolist')
@login_required
def display_todo_name():
    todo_names = ToDos.query.all()
    return render_template('todo_list.html', todo_names=todo_names)

# home page display


@main.route('/dashboard')
@login_required
def display_dashboard():
    return render_template('home.html')

# route company create form
@main.route('/createtodo', methods=['GET','POST'])
@login_required
def create_todo():
    form = CreateToDo()
    
    if form.validate_on_submit():
        todo_info = ToDos(

            todo_name=form.todo_name.data,
            todo_status=form.todo_status.data,
            todo_description=form.todo_description.data,
            todo_created_date=form.todo_created_date.data)

        db.session.add(todo_info)
        db.session.commit()
        flash('Record save Sucessfuly')
        return redirect(url_for('main.create_todo'))

    return render_template('create_todo.html', form=form)
        

#  route edit company data form

@main.route('/edit/todo/<todo_id>', methods=['GET', 'POST'])
@login_required
def edit_todo(todo_id):
    todos = ToDos.query.get(todo_id)

    form = EditToDoForm(obj=todos)
    form.todo_status.choices = [todos.todo_status,'','NotStarted','OnGoing','Completed']
    if form.validate_on_submit():
        todos.todo_name = form.todo_name.data,
        todos.todo_status = form.todo_status.data,
        todos.todo_description = form.todo_description.data,
        todos.todo_created_date = form.todo_created_date.data,
        db.session.add(todos)
        db.session.commit()
        flash('Task Edited Successfully')
        return redirect(url_for('main.display_todo_name'))
    return render_template('edit_todo.html',form=form, todos=todos)
#

# route delete company data form

@main.route('/delete/todo/<todo_id>', methods=['GET', 'POST'])
@login_required
def delete_todo(todo_id):
    todos = ToDos.query.get(todo_id)
    if request.method == 'POST':
        db.session.delete(todos)
        db.session.commit()
        flash('Task deleted Sucessfully')
        return redirect(url_for('main.display_todo_name'))
    return render_template('delete_todo.html', todos=todos, todo_id=todo_id)


# route error handling

@main.app_errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404
