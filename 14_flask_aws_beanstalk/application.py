from flask import Flask
from flask import render_template

application = Flask(__name__)


@application.route("/")
def index():
    return "Hello World from Flask Main Page"


@application.route("/help")
def help_page():
    return "<b><font color=blue>This is The Help Page!</font></b>"


@application.route("/user")
def user_page():
    return "Users page."


@application.route("/user/<username>")
def show_user_page(username):
    return f"Hello {username.upper()}"


@application.route("/path/<path:subpath>")
def print_subpath(subpath):
    return f"SubPath is: {subpath()}"


@application.route("/square/<int:x>")
def calculate_square(x):
    return f"Square of {str(x)} equals {str(x*x)}"


@application.route("/htmlpage")
def show_html_page():
    myfile = open("mypage.html", mode='r')
    page = myfile.read()
    myfile.close()
    return page


# -------------Main------------------
if __name__ == "__main__":
    application.debug = True
    application.env = "Dev"
    application.run()
# -----------------------------------
