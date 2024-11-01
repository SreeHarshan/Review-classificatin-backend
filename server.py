from flask import Flask, request, render_template
from flask_cors import CORS
import classifier as clf

app = Flask("Review classification")
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/", methods=["GET", "POST"])
def classify():
    if request.method == "POST":
        query = request.form.get("query")
        output = clf.predict(query)  
        return render_template("index.html", query=query, prediction=output)
    return render_template("index.html", query=None, prediction=None)

if __name__ == "__main__":
    app.run(debug=True)
