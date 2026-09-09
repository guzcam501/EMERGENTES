from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return "<h1>pagina de inicio"

@app.route("/acerca-de")
def acerca_de():
    return"<h1>informacion sobre nosotros"

@app.route("/contacto")
def contacto():
    return "<h1>pagina de contacto"

@app.route("/info")
@app.route("/informacion")
@app.route("/about")
def informacion():
    return "<h1> pagina de informacion<h1>"

@app.route("/servicios")
def servicios():
    return"<h1>pagina de ofertas<h1>"

@app.route("/blog")
def blog():
    return "<h1>lista de entradas del blog<h1>"

if __name__ == "__main__":

    app.run(debug = True)
