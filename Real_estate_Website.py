from flask import render_template
from flask import Flask, request


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def hello(latitude=None, longitude=None):
    if request.method == "POST":
        latitude = request.form["lat"]
        longitude = request.form["long"]
        print(latitude, longitude)
        return render_template("index.html", latitude=latitude, longitude=longitude)
    else:
        return render_template("index.html", latitude=latitude, longitude=longitude)

if __name__=='__main__':
    app.run(debug=True)