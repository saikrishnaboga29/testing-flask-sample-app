from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World"


@app.route('/test', methods=['GET'])
def test_route():
    print("Received test request.")
    return jsonify({"message": "Test route is working!"})

if __name__ == '__main__':
    app.run(debug=True)