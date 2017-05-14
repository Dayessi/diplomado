from flask import Flask
from flask.templating import render_template

app = Flask(__name__)


@app.route('/inicio')
def hello_world():
    return render_template("inicio.html")

if __name__ == '__main__':
    app.run(debug=True)
