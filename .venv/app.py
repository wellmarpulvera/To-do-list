import json
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder='todolist')

# Load tasks from a JSON file if it exists, otherwise initialize with a default task
try:
    with open('tasks.json', 'r') as file:
        todolist = json.load(file)
except FileNotFoundError:
    todolist = [{"task": "default task", "done": False}]

@app.route('/')
def index():
    return render_template("index.html", todolist=todolist)

@app.route("/add", methods=["POST"])
def add():
    todo = request.form['todo']
    todolist.append({"task": todo, "done": False})
    save_tasks()
    return redirect(url_for('index'))

@app.route("/edit/<int:index>", methods=["GET", "POST"])
def edit(index):
    todo = todolist[index]
    if request.method == "POST":
        todo["task"] = request.form['todo']
        save_tasks()
        return redirect(url_for('index'))
    else:
        return render_template("edit.html", todo=todo, index=index)

@app.route("/delete/<int:index>")
def delete(index):
    del todolist[index]
    save_tasks()
    return redirect(url_for('index'))

@app.route("/check/<int:index>")
def check(index):
    todolist[index]["done"] = not todolist[index]["done"]
    save_tasks()
    return redirect(url_for('index'))

def save_tasks():
    with open('tasks.json', 'w') as file:
        json.dump(todolist, file)

if __name__ == '__main__':
    app.run(debug=True)
