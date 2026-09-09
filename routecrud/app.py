from flask import Flask, jsonify

app = Flask(__name__)

tareas =[
    {"id":1, 'tarea':'aprender', 'completada':False},
    {"id":2, 'tarea':'practicar falsk', 'completada':False}
]
#GET
@app.route("/api/tareas", methods=['GET'])
def lista_tareas():
    return jsonify(tareas)

@app.route("/api/tareas/<int:tarea_id>", methods=['GET'])
def obtener_tareas(tarea_id):
    tarea = None
    for t in tareas:
        if t['id'] == tarea_id:
            tarea = t
            break
    if tarea:
        return jsonify(tarea)
    return jsonify({'error':'tarea no encontrada'}),404     
#POST
@app.route("/api/tareas", methods=['POST'])
def crear_tareas():
    nueva_tarea ={
        'id' :len(tareas)+1,
        'tarea' :request.json.get('tarea',''),
        'completada' :request.json.get('completada',False)
    }
    tareas.append(nueva_tarea)
    return jsonify(nueva_tarea),201

@app.route('/api/tareas/<int:tarea_id>', methods=['DELETE'])
def eliminar_tarea(tarea_id):
    global tareas
    tareas = [t for t in tareas if t['id'] != tarea_id]
    return jsonify({'message': 'Tarea eliminada'}), 200

@app.route('/api/tareas/<int:tarea_id>/completar', methods=['PATCH'])
def completar_tarea(tarea_id):
    tarea = next((t for t in tareas if t['id'] == tarea_id), None)
    if not tarea:
        return jsonify({'error': 'Tarea no encontrada'}), 404
    tarea['completada'] = True
    return jsonify(tarea), 200

@app.route('/api/tareas/completadas', methods=['GET'])
def tareas_completadas():
    resultado = [t for t in tareas if t['completada'] is True]
    return jsonify(resultado), 200

if __name__== "__main__":
    app.run(debug=True)