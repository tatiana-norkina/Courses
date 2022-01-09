from flask import *

from db import *


app = Flask(__name__)


@app.route("/")
def home():
    qry = "SELECT * FROM stocks ORDER BY price"
    data = sqldata(qry)
    return render_template("index.html", data = data)

if __name__== "__main__":
    app.run()