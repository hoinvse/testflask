from flask import flask, jsonify

app = Flask(__name__)

@app.route("/")
def hello():
    return jsonify({"msg":"hello dcmm"})

if __name__ == "__main__":
    app.run