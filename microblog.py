from flask import Flask

app = Flask("microblog")

@app.route("/")
def index():
    return "<h1 style='color:green;font-size:50px;background-color:#000;text-align:center;'>Olá Mundo</h1>"

app.run()