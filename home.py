from flask import Flask, render_template, url_for
app = Flask(__name__)

#Home page
@app.route("/")
@app.route("/home")
def home():
    return render_template('report.html')

#About page
@app.route("/about")
def about():
    return "<h1>About page</h1>"

if __name__ == '__main__':
    app.run(debug=True)