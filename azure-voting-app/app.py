from flask import Flask, request, render_template_string

app = Flask(__name__)

votes = {"Alice":0, "Bob":0}

html = """
<h2>Voting App</h2>

<form action="/vote" method="post">
<button name="candidate" value="Alice">Vote Alice</button>
<button name="candidate" value="Bob">Vote Bob</button>
</form>

<h3>Results</h3>
<p>Alice: {{alice}}</p>
<p>Bob: {{bob}}</p>
"""

@app.route("/")
def home():
    return render_template_string(html, alice=votes["Alice"], bob=votes["Bob"])

@app.route("/vote", methods=["POST"])
def vote():
    candidate = request.form["candidate"]
    votes[candidate] += 1
    return render_template_string(html, alice=votes["Alice"], bob=votes["Bob"])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)