from flask import Flask, render_template

app = Flask(__name__)

@app.route("/search.html", methods=['GET', 'POST'])
@app.route("/", methods=['GET', 'POST'])
def hello_world():
    return render_template("search.html")

if __name__ == "__main__":
    app.run()