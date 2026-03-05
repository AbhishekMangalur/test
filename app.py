from flask import Flask, render_template, request

app = Flask(__name__)

votes = {"Python":0, "Java":0, "JavaScript":0}

@app.route("/", methods=["GET","POST"])
def index():
    if request.method == "POST":
        vote = request.form["language"]
        votes[vote] += 1

    return render_template("index.html", votes=votes)

if __name__ == "__main__":
    app.run()