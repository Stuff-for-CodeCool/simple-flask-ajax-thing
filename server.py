from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.get("/")
def reading_data():
    data = "ce am citit din baza de date"
    return render_template("index.html", data=data, script=True)


@app.post("/")
def adding_new_data():
    data = f"adaug in baza de date '{request.json.get('name')}'"
    return jsonify({"message": data})


@app.put("/")
def modifying_data():
    data = f"modific in baza de date '{request.json.get('name')}'"
    return jsonify({"message": data})


@app.delete("/")
def removing_data():
    data = f"Am sters absolut totul"
    return jsonify({"message": data})


if __name__ == "__main__":
    app.run(debug=True)
