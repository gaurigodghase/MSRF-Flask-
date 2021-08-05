from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/hello')
def hello():
    return("<h1>Hello World!</h1>")

if __name__ == "__main__":
    print("Starting Python Flask Server")
    app.run()