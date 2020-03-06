from flask import Flask, Markup, render_template, make_response

app = Flask(__name__,
            instance_relative_config=False,
            template_folder="templates",
            static_folder="static")

@app.route("/1")
def hello():
    value = 9**2
    return value

@app.route("/2")
def hello2():
    return Markup("<h1>Hello World</h1>")


@app.route("/3")
def hello3():
    return render_template("index.html")

@app.route("/4")
def hello4():
    headers = {"Content-Type":"application/json"}
    return make_response("it worked", 200, headers)

app.run(port=5000)