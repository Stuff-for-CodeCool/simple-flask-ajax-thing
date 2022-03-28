from flask import Flask, render_template, request, jsonify
from database_manager import connection_handler

app = Flask(__name__)


@connection_handler
def read_stuff_from_db(cursor):
    query = "SELECT * FROM your_database;"
    cursor.execute(query)
    return cursor.fetchall()

@connection_handler
def insert_stuff_into_database(cursor, other, values):
    query = "INSERT INTO your_database (some, thing) VALUES (%(ceva)s, %(altceva)s);"
    cursor.execute(query, {
        "ceva": other,
        "altceva": values
    })


@app.get("/")
def reading_data():
    data = read_stuff_from_db()
    return render_template("index.html", data=data, script=True)


@app.post("/")
def adding_new_data():
    insert_stuff_into_database("fake data", data)
    data = f"adaug in baza de date 'fake data' si '{request.json.get('name')}'"
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
