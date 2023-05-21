from flask import Flask, redirect, url_for, request
from flask_cors import CORS
from database import db

def create_app():
    app = Flask(__name__)
    CORS(app, origins='http://127.0.0.1:5501', supports_credentials=True)
 
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://myuser:mypassword@localhost:3306/mydatabase'

    app.config["SQLALCHEMY_ECHO"] = True
    app.config["SQLALCHEMY_RECORD_QUERIES"] = True
    db.init_app(app)
    
    with app.app_context():
        from student import student_bp
        app.register_blueprint(student_bp)

    return app

app = create_app()

@app.route('/hello/<name>')
def hello_name(name):
    return 'Hello %s!' % name

@app.route('/success/<name>/<password>')
def success(name, password):
    return 'Hello ' + name + ' your password is: ' + password

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['username']
        password = request.form['password']
        return redirect(url_for('success', name=user, password=password))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success', name=user))


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
