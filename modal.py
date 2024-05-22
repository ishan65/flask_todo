from web import mysql


class Todo(mysql.Model):
    id = mysql.Column(mysql.Integer, primary_key=True)
    title = mysql.Column(mysql.String(50), unique=True, nullable=False)
    message = mysql.Column(mysql.String(200), unique=True, nullable=False)

    def __repr__(self):
        return f"Todo {self.title}"
