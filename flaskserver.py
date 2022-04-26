import subprocess
from flask import Flask, render_template
from flask import request

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/testaccess")
def testaccess():
    return "Test Access complete."

@app.route("/datecmd")
def datecmd():
    cmd="date"
    return subprocess.Popen(
      cmd, stdout=subprocess.PIPE,
      shell=True).communicate()[0]

@app.route("/parametertest")
def parametertest():
    yourparameter = request.args.get('yourparameter')
    return "[%s] World  !" % yourparameter

@app.route("/templatehelloworld")
def templatehelloworldtest():
    yournameparameter = request.args.get('yournameparameter')
    return render_template('templatehelloworld.html', yournameparameter=yournameparameter)

@app.route("/submitform", methods=["GET", "POST"])
def submitform():
    yournameparameter = "No name passed."
    if request.method == "POST":
        yournameparameter = request.form['yournameparameter']
    return render_template('templatehelloworld.html', yournameparameter=yournameparameter)


if __name__ == "__main__":
    # Server on 0.0.0.0 and port 15000 and debug mode is on to hotload
    app.run(host='0.0.0.0', port=15000, debug=True)
