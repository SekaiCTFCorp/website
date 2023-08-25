from flask import *

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/contact", methods=["POST"])
def contact():
    # TODO: Implement this
    return "test"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
