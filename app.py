from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def main():
    return {"payload":"welcome to my project"}

@app.route("/read")
def read():
    return {"payload":"read successfully"}

@app.route("/create", methods=["POST"])
def create():
    return {"payload":"create successfully"}

@app.route("/delete", methods=["DELETE"])
def delete():
    return {"payload":"delete successfully"}

@app.route("/put", methods=["PUT"])
def put():
    return {"payload":"put successfully"}

if __name__ == "__main__":
    app.run(debug=True)