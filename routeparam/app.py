from flask import Flask

app = Flask(__name__)


@app.route("/usuario/<nombre>")
def perfil_usuario(nombre):
    return f"perfil de: <strong>{nombre}</strong>"


@app.route("/post/<id>")
def ver_post(id):
    return f"mostrando el post: <strong>{id}</strong>"

@app.route("/categoria/<categoria>/<producto>")
def productos(categoria,producto):
    return f"categoria: <strong>{categoria}</strong>, producto: <strong>{producto}</strong>"

@app.route("/producto/<codigo>")
def producto(codigo):
    return f"Código del producto: <strong>{codigo}</strong>"

@app.route("/clima/<ciudad>")
def clima(ciudad):
    return f"Clima en : <strong>{ciudad}</strong>"


if __name__== "__main__":
    app.run(debug=True)