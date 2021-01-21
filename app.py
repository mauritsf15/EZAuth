import os
from flask import Flask, request, Response, jsonify, render_template
from passlib.hash import sha256_crypt
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Auth(db.Model):
    __tablename__ = 'ezauth'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    username = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f"Auth(username='{self.username}', email='{self.email}', password='{self.password}'"

@app.route('/')
def index():
    return jsonify(success=True, message="EZAuth is working!")

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        try:
            username = request.form.get('username')
            password = request.form.get('password')
            if username == None:
                return Response('{"success": false, "cause": "Bad request"}', status=400, mimetype='application/json')
            else:
                if password == None:
                    return Response('{"success": false, "cause": "Bad request"}', status=400, mimetype='application/json')
                else:
                    try:
                        db_values = Auth.query.filter_by(username=username).first()
                        try:
                            db_pass = db_values.password
                            if sha256_crypt.verify(str(password), db_pass):
                                return Response('{"success": true, "message": "Logged in"}', status=200, mimetype='application/json')
                            else:
                                return Response('{"success": false, "cause": "Incorrect credentials"}', status=400, mimetype='application/json')
                        except:
                            return Response('{"success": false, "cause": "Something went wrong."}', status=400, mimetype='application/json')
                    except:
                        return Response('{"success": false, "cause": "Could not find that username"}', status=400, mimetype='application/json')
        except:
            return Response('{"success": false, "cause": "Bad request"}', status=400, mimetype='application/json')
    else:
        return Response('{"success": false, "cause": "Method not allowed"}', status=405, mimetype='application/json')

@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        try:
            username = request.form.get('username')
            email = request.form.get('email')
            password1 = request.form.get('password')
            password2 = request.form.get('confirmPassword')
            if password1 == password2:
                db_pass = sha256_crypt.hash(str(password1))
                usercheck = Auth.query.filter_by(username=username).all()
                if usercheck == []:
                    emailcheck = Auth.query.filter_by(email=email).all()
                    if emailcheck == []:
                        try:
                            register = Auth(username=username, email=email, password=db_pass)
                            db.session.add(register)
                            db.session.commit()
                            return Response('{"success": true, "message": "Signed up"}', status=200, mimetype='application/json')
                        except:
                            return Response('{"success": false, "cause": "An unknown error occured"}', status=400, mimetype='application/json')
                    else:
                        return Response('{"success": false, "cause": "Email is already in use"}', status=400, mimetype='application/json')
                else:
                    return Response('{"success": false, "cause": "Username is already in use"}', status=400, mimetype='application/json')
            else:
                return Response('{"success": false, "cause": "Passwords must match"}', status=400, mimetype='application/json')
        except:
            return Response('{"success": false, "cause": "Bad request"}', status=400, mimetype='application/json')
    else:
        return Response('{"success": false, "cause": "Method not allowed"}', status=405, mimetype='application/json')

@app.route('/version')
def version():
    return jsonify(success=True, version=1.0)

if __name__ == "__main__":
    app.run(debug=True)