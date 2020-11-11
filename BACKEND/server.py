from flask import Flask, request, flash, redirect
from flask import render_template, url_for
from flask import Response
import pymongo
from pymongo import MongoClient

# Configuraciones
app = Flask(__name__)
app.config['SECRET_KEY'] = "MSG"



# conexión
con = MongoClient("mongodb+srv://bredly:bredlybd2@clusterdb.0ts2t.mongodb.net/proyecto_sopes?retryWrites=true&w=majority")
db = con.proyecto_sopes
coleccion = db.estudiante


# colección
# Rutas del api

@app.route('/')
def index():
    datos = [{"nombre": "Hola"}, {"nombre": "Yoselin"}, {"nombre": "como"}, {"nombre": "estas?"}]
    return render_template('index.html', author="Yoselin", sunny=False, lista=datos)


@app.route('/consulta', methods=['POST'])
def consulta():
    carne = request.form['carne']
    anio = request.form['anio']
    semestre = request.form['semestre']
    if not (carne and semestre and anio):            
        return Response({'mensaje':'Faltan Datos para consultar'}, status=500, mimetype='application/json')
    else:
        consulta = {"carne": carne, "anio": anio, "semestre": semestre}
        x = coleccion.find(consulta)
        return Response({'mensaje': x}, status=201, mimetype='application/json')



@app.route('/insertar', methods=['POST'])
def insertar():
    if request.method == 'POST':
        nombre = request.form['nombre']
        carne = request.form['carne']
        dpi = request.form['dpi']
        semestre = request.form['semestre']
        anio = request.form['anio']
        grupo = request.form['grupo']
        correo = request.form['correo']

        if not (nombre and carne and dpi and semestre and grupo and correo):
            return Response({'mensaje':'Faltan Datos para insertar'}, status=500, mimetype='application/json')
        else:
            data = {"nombre": nombre, "carne": carne, "dpi": dpi, "semestre": semestre, "anio": anio, "grupo": grupo, "correo": correo}
            x = coleccion.insert_one(data)
            return Response({'mensaje': str(x)}, status=201, mimetype='application/json')

'''
@app.route('/grupo', methods=['GET', 'POST'])
def grupo():
    if request.method == "POST":
        grupo = request.form['grupo']

        if not grupo:
            flash('No se llenaron todos los campos del formulario, para consultar grupo')
            return redirect(url_for('grupo'))
        else:
            cadena = "SELECT carne, correo FROM student WHERE grupo='{0}'".format(grupo)
            conn = get_db_connection()
            datos = conn.execute(cadena).fetchall()
            conn.commit()
            conn.close()
            return render_template('grupo.html', datos=datos)

    return render_template('grupo.html')

@app.route('/delete', methods=['GET', 'POST'])
def delete():
    if request.method == "POST":
        cadena = "DELETE FROM student"
        conn = get_db_connection()
        conn.execute(cadena)
        conn.commit()
        conn.close()
        return redirect(url_for('index'))

    return render_template('delete.html')

'''


# @app.route('/grupo/int:<group_id>')
# def getgrupo(group_id):
#     return 'form_grupo ' + str(group_id)


if __name__ == 'main':
    app.run()
