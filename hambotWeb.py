# Peter Savinelli

# Imports Hamilton class, and the web app framework
from flask import Flask, render_template, request
import Hamilton

# Creates a new hamilton object
ham = Hamilton.Hamilton()

# Creates a new Flask app object
app = Flask(__name__)


# Creates the primary webpage for the app (in this case it's the only webpage)
@app.route("/", methods=['GET', 'POST'])
# Code for main website, it gets a response from Hamilton if there is one and then loads the page's HTML
def main():
    result = ham.greet()
    if request.method == "POST":
        text = request.form['text']
        result = ham.genres(text)
    return render_template('display.html', result=result)


# Puts app in debug mode for testing purposes
if __name__ == '__main__':
    app.run(debug=True)
