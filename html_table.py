from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
@app.route('/<int:column>')
@app.route('/<int:column>/<int:row>')
@app.route('/<int:column>/<int:row>/<string:columncolor>/<string:rowcolor>')
def cookie_function2(columncolor="red", rowcolor="blue", column=4, row=4):
    return render_template('index.html', columncolor=columncolor, rowcolor=rowcolor, column=column, row=row)


@app.route('/lists')
def render_lists():
    # Soon enough, we'll get data from a database, but for now, we're hard coding data
    student_info = [
        {'firstname': 'Michael', 'lastname': 'Smith', 'fullname': 'Michael Smith'},
        {'firstname': 'John', 'lastname': 'Doe', 'fullname': 'John Doe'},
        {'firstname': 'Mark', 'lastname': 'Color', 'fullname': 'Mark Color'},
        {'firstname': 'KB', 'lastname': 'Beau', 'fullname': 'KB Beau'}
    ]
    return render_template("index.html", random_numbers=[3, 1, 5], students=student_info)


if __name__ == "__main__":
    app.run(debug=True)
