from flask import Flask

app = Flask(name)

@app.route("/")
def home():
return "Website Running Successfully"

if name == "main":
app.run()
