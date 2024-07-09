#  Importar las herramientas
# Acceder a las herramientas para crear la app web
from flask import Flask, request, jsonify

# Para manipular la DB
from flask_sqlalchemy import SQLAlchemy

# Módulo cors es para que me permita acceder desde el frontend al backend
from flask_cors import CORS

# Crear la app
app = Flask(__name__)

# permita acceder desde el frontend al backend
CORS(app)

# Configurar a la app la DB
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://usuario:contraseña@localhost:3306/nombre_de_la_base_de_datos'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://codogrupo22:codo2024@codogrupo22.mysql.pythonanywhere-services.com/codogrupo22$codo'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Crear un objeto db, para informar a la app que se trabajará con sqlalchemy
db = SQLAlchemy(app)


# Definir la tabla
class Profesional(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    apellido=db.Column(db.String(50))
    especialidad=db.Column(db.String(50))
    imagen=db.Column(db.String(400))

    def __init__(self,nombre,apellido,especialidad,imagen):   #crea el  constructor de la clase
        self.nombre=nombre   # no hace falta el id porque lo crea sola mysql por ser auto_incremento
        self.apellido=apellido
        self.especialidad=especialidad
        self.imagen=imagen


# 8. Crear la tabla al ejecutarse la app
with app.app_context():
    db.create_all()

# Crear ruta de acceso
# / es la ruta de inicio
@app.route("/")
def index():
    return f'App Web de Consultoios CaC para el primer cuatrimestre 2024'

# Crear un registro en la tabla Profesional
@app.route("/registro", methods=['POST'])
def registro():
    # {"nombre": "Felipe", ...} -> input tiene el atributo name="nombre"
    nombre_recibido = request.json["nombre"]
    apellido=request.json['apellido']
    especialidad=request.json['especialidad']
    imagen=request.json['imagen']

    nuevo_registro = Profesional(nombre=nombre_recibido,apellido=apellido,especialidad=especialidad,imagen=imagen)
    db.session.add(nuevo_registro)
    db.session.commit()

    return "Solicitud de post recibida"


# Retornar todos los registros en un Json
@app.route("/profesionales",  methods=['GET'])
def profesionales():
    # Consultar en la tabla todos los registros
    # all_registros -> lista de objetos
    all_registros = Profesional.query.all()

    # Lista de diccionarios
    data_serializada = []

    for objeto in all_registros:
        data_serializada.append({"id":objeto.id, "nombre":objeto.nombre, "apellido":objeto.apellido, "especialidad":objeto.especialidad, "imagen":objeto.imagen})

    return jsonify(data_serializada)


# Modificar un registro
@app.route('/update/<id>', methods=['PUT'])
def update(id):
    # Buscar el registro a modificar en la tabla por su id
    profesional = Profesional.query.get(id)

    # {"nombre": "Felipe"} -> input tiene el atributo name="nombre"
    nombre = request.json["nombre"]
    apellido=request.json['apellido']
    especialidad=request.json['especialidad']
    imagen=request.json['imagen']

    profesional.nombre=nombre
    profesional.apellido=apellido
    profesional.especialidad=especialidad
    profesional.imagen=imagen
    db.session.commit()

    data_serializada = [{"id":profesional.id, "nombre":profesional.nombre, "apellido":profesional.apellido, "especialidad":profesional.especialidad, "imagen":profesional.imagen}]

    return jsonify(data_serializada)


@app.route('/borrar/<id>', methods=['DELETE'])
def borrar(id):

    # Se busca a la tabla profesional por id en la DB
    profesional = Profesional.query.get(id)

    # Se elimina de la DB
    db.session.delete(profesional)
    db.session.commit()

    data_serializada = [{"id":profesional.id, "nombre":profesional.nombre, "apellido":profesional.apellido, "especialidad":profesional.especialidad, "imagen":profesional.imagen}]

    return jsonify(data_serializada)

if __name__ == "__main__":
    app.run(debug=True)
