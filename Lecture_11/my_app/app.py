from flask import Flask, render_template
import json

# Router
app = Flask("hello_world")
# change default templates dir
# app.template_folder = 'my_template'

# https://materializecss.com/cards.html

@app.route('/')
def index():
    return render_template(
        'index.html', 
        author = "Jatin",
        languages = ['python', 'c++', 'java', 'GO', 'JS', 'TS', 'Kotlin', 'PHP', 'HACK']
    )

# Eager Loading
with open("data.json", "r+") as file:
    student_data = json.load(file)

@app.route('/student/<int:roll>')
def student(roll):
    try: 
        my_student = next(
            filter(
                lambda x: x['roll'] == roll, 
                student_data
            )
        )
        return render_template(
            'student.html',
            student = my_student
        )
    except StopIteration:
        return "Student not found"

@app.route('/special_url/<number>')
def special(number):
    return "parameter: {}".format(number)

@app.route('/square/<int:number>')
def square(number):
    return "square: {}".format(number**2)

@app.route('/add/<int:number1>/<int:number2>')
def add(number1, number2):
    return "add: {}".format(number1+number2)

if __name__ == "__main__":
    app.run(port=8000, debug=True)
