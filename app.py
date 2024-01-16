from flask import Flask, render_template, url_for

# Constants:
HTML_SNIPPET: str = '<h1> Hello, World </h1>'
MAIN_NAME: str = '__main__'
ENTRY_POINT_NAME: str = "index.html"

# Create a flask application object.
application: Flask = Flask(__name__)


# Define the application's entry point.
@application.route("/")
def app_main() -> str:
    return render_template(ENTRY_POINT_NAME)


@application.route("/home")
def home() -> str:
    return render_template("home.html")


# Call the application's entry point:
if __name__ == MAIN_NAME:
    application.run(debug=True)
