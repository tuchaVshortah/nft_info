from flask import Flask, render_template, request
import handler

app = Flask(__name__)

@app.route("/search.html")
@app.route("/")
def index():
    print("returned search.html")
    return render_template("index.html")

@app.route("/search", methods=["POST"])
def search():
    search = request.form["search"]
    print("The search is: " + search)

    result = handler.handler(search)
    return result

        

if __name__ == "__main__":
    app.run()