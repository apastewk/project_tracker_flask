from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)

@app.route("/student-search")
def get_student_form():
    """Show form for searching for a student."""

    return render_template("student_search.html")

@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github', 'jhacks')
    first, last, github = hackbright.get_student_by_github(github)
    return render_template("student_info.html", 
                           github=github, 
                           first=first, 
                           last=last)

@app.route("/student-add-form")
def student_add_form():
    """Form to add a new student."""

    return render_template("student_add.html")

@app.route("/student-add", methods=['POST'])
def student_add():
    """Add a student."""

    first = request.form.get("first")
    last = request.form.get("last")
    github = request.form.get("github")

    # QUERY statements goes here

    return render_template("student_new.html")


if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)
