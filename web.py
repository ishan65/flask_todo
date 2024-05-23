from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import socket
from secrets_info import password


app = Flask(__name__)
app.config["SECRET_KEY"] = ""
app.config["MYSQL_DB"] = "todoapp"
app.config["MYSQL_PASSWORD"] = password
app.config["MYSQL_USER"] = "mydb"
# app.config["MYSQL_HOST"] = "mysql-db"
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_PORT"] = 3306
app.config["SQLALCHEMY_DATABASE_URI"] = (
        f"mysql+pymysql://{app.config['MYSQL_USER']}:{app.config['MYSQL_PASSWORD']}@{app.config['MYSQL_HOST']}:{app.config['MYSQL_PORT']}/{app.config['MYSQL_DB']}"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
mysql = SQLAlchemy(app)


class Todo(mysql.Model):
    id = mysql.Column(mysql.Integer, primary_key=True)
    title = mysql.Column(mysql.String(50), unique=True, nullable=False)
    message = mysql.Column(mysql.String(200), unique=True, nullable=False)

    def __repr__(self):
        return f"Todo {self.title}"


with app.app_context():
    mysql.create_all()


@app.route("/")
def index():
    hostname = socket.gethostname()
    requester = request.remote_addr
    context = {"hostname": hostname, "requester": requester}
    return render_template("index.html", context=context)


@app.route("/todo")
def todo():
    tasks = Todo.query.all()
    return render_template("todo.html", tasks=tasks)


@app.route("/todo/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        title = request.form["title"]
        message = request.form["message"]
        newtask = Todo(title=title, message=message)
        mysql.session.add(newtask)
        mysql.session.commit()
        return redirect(url_for("todo"))
    return render_template("create.html")


@app.route("/todo/<int:post_id>")
def post(post_id):
    single_task = Todo.query.get(post_id)
    return render_template("detailed_post.html", detailed_post=single_task)


@app.route("/todo/<int:post_id>/edit", methods=["GET", "POST"])
def edit(post_id):
    edit_task = Todo.query.get(post_id)
    if request.method == "POST":
        edit_task.title = request.form["title"]
        edit_task.message = request.form["message"]
        mysql.session.commit()
        return redirect(url_for("todo"))
    return render_template("edit.html", old_data=edit_task)


@app.route("/todo/<int:post_id>/delete")
def delete(post_id):
    delete_task = Todo.query.get(post_id)
    mysql.session.delete(delete_task)
    mysql.session.commit()
    return redirect(url_for("todo"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5789, debug=True)
