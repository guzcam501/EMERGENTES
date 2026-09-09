from flask import Flask

app = Flask(__name__)

@app.route("/cadena/<string:nombre>")
def demo_cadena(nombre):
    return f" cadena: {nombre} => tipo de datos: {type(nombre).__name__}"
 
@app.route("/entero/<int:numero>")
def demo_entero(numero):
    return f" entero: {numero} => tipo de datos: {type(numero).__name__}"
 
@app.route("/decimal/<float:decimal>")
def demo_float(decimal):
    return f" float: {decimal} => tipo de datos: {type(decimal).__name__}"

@app.route("/ruta/<path:ruta>")
def demo_ruta(ruta):
    return f" ruta: {ruta}"

@app.route("/recurso/<uuid:identificador>/detalle")
def demo_uuid_detalle(identificador):
    return f"uuid: {identificador} => tipo: {type(identificador).__name__}"

@app.route("/archivo/<path:ruta>.txt")
def demo_path_txt(ruta):
    return f"archivo: {ruta}.txt => tipo: {type(ruta).__name__}"

if __name__== "__main__":
    app.run(debug=True)