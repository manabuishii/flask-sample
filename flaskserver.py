from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    # Server on 0.0.0.0 and port 15000
    app.run(host='0.0.0.0', port=15000)
