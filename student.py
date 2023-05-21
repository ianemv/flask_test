from flask import Blueprint, jsonify, request
from flask_cors import CORS, cross_origin
from database import get_db, Student

student_bp = Blueprint('student', __name__, url_prefix='/students')
CORS(student_bp, supports_credentials=True, origins='http://127.0.0.1:5501')
db = get_db()

@student_bp.route('/', methods=['POST', 'OPTIONS'], strict_slashes=False)
@cross_origin(supports_credentials=True)
def create_student():

    print(request.method)

    if request.method == 'OPTIONS':
        response = jsonify({'message': 'CORS preflight request successful'})
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        return response

    data = request.get_json()
    name = data['name']
    city = data['city']
    addr = data['addr']
    pin = data['pin']
    student = Student(name=name, city=city, addr=addr, pin=pin)
    db.session.add(student)
    db.session.commit()
    response = jsonify({'message': 'Student created successfully'})
    return response, 201

@student_bp.route('/', methods=['GET'])
def get_students():
    return 'Hello from students route'