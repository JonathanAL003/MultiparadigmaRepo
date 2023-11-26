from flask import Blueprint,request,jsonify,render_template,redirect, url_for
from sqlalchemy import exc 
from models import User
from forms import UserForm
from app import db,bcrypt
from auth import tokenCheck,verificar


appuser=Blueprint('appuser',__name__,template_folder="templates")

# @appuser.route("/")
# def index():
#     return render_template("index.html")
@appuser.route('/404')
def Error():
    return render_template("error.html")

@appuser.route("/auth/registro",methods=["POST"])
def registro():
    user = request.get_json()
    userExists=User.query.filter_by(email=user['email']).first()
    if not userExists:
        usuario=User(email=user['email'],password=user['password'])
        try:
            db.session.add(usuario)
            db.session.commit()
            mensaje="Usuario Creado"
        except exc.SQLAlchemyError as e:
            mensaje="ERROR "+e
    return jsonify({"message":mensaje})

@appuser.route('/auth/login',methods=["POST"])
def login():
    try:
        user = request.get_json()
        usuario = User(email=user['email'],password=user['password'])
        searchUser = User.query.filter_by(email=usuario.email).first()
        if searchUser:
            validation = bcrypt.check_password_hash(searchUser.password,user["password"])
            if validation:
                auth_token=usuario.encode_auth_token(user_id=searchUser.id)
                response = {
                    'status':'success',
                    'message':'Login exitoso',
                    'auth_token':auth_token
                }
                print(response)
                return jsonify(response)
        return jsonify({"message":"Datos incorrectos"})
    except Exception as ex:
        return jsonify({"status":400, "message":"Ha ocurrido un incidente", "desc": str(ex)})

@appuser.route('/usuario/json',methods=['GET'])
@tokenCheck
def getUsers(usuario):
    print(usuario)
    print(usuario['admin'])
    if usuario['admin']:
        output=[]
        usuarios=User.query.all()
        for usuario in usuarios:
            usuarioData={}
            usuarioData['id']=usuario.id
            usuarioData['email']=usuario.email
            usuarioData['password']=usuario.password
            usuarioData['registered_on']=usuario.registered_on
            output.append(usuarioData)
        return jsonify({'usuarios':output})
    else:
        return jsonify({'Error':"No tienes permisos"})

@appuser.route('/')
@appuser.route('/main')
def main():
    try:
        return render_template('main.html')
    except Exception as ex:
        print(str(ex))
        return redirect(url_for('appuser.Error'))

@appuser.route('/login',methods=["GET","POST"])
def login_post():
    if(request.method=="GET"):
        token = request.args.get('token')
        if token:
            info = verificar(token)
            if(info['status']!="fail"):
                responseObject={
                    'status':"success",
                    'message':'valid token',
                    'info':info
                }
                return jsonify(responseObject)
        return render_template('login.html')
    else:
        email =request.json['email']
        password=request.json['password']
        print(request.json)
        usuario = User(email=email,password=password)
        searchUser = User.query.filter_by(email=email).first()
        if searchUser:
            validation = bcrypt.check_password_hash(searchUser.password,password)
            if validation:
                auth_token = usuario.encode_auth_token(user_id=searchUser.id)
                if searchUser.admin == True:
                    admin = 1
                else:
                    admin = 0
                responseObject={
                    'status':"success",
                    'login':'Loggin exitoso',
                    'auth_token':auth_token,
                    'admin': admin
                }
                print(responseObject['admin'])
                return jsonify(responseObject)
        return jsonify({'message':"Datos incorrectos"})
    
@appuser.route('/sign',methods=["GET","POST"])
def logint_post():
    if request.method=="GET":
        return render_template('register.html')
    else:
        email=request.json['email']
        password=request.json['password']
        usuario = User(email=email,password=password)
        userExists = User.query.filter_by(email=email).first()
        if not userExists:
            try:
                db.session.add(usuario)
                db.session.commit()
                responseObject={
                    'status':'success',
                    'message':"Registro exitoso"
                }
            except exc.SQLAlchemyError as e:
                responseObject={
                    'status':'error',
                    'message':e
                }
        else:
            responseObject={
                'status':'error',
                'message':'usuario existente'
            }
        return jsonify(responseObject)
    
@appuser.route('/usuario')
def Users():
    try:
        users = User.query.order_by("id").all()
        return render_template('indexUser.html', users = users)
    except Exception as ex:
        print(str(ex))
        return redirect(url_for('appuser.Error'))

@appuser.route('/usuario/edit/<string:mail>', methods = ["GET", "POST"])
def Editar(mail):
    try:
        user = User.query.filter_by(email = mail).first()
        formUser = UserForm(obj = user)
        if request.method == "POST":
            if formUser.validate_on_submit():
                formUser.populate_obj(user)
                user.encodePassword(user.password)          #Encripta la password
                #user.admin = bool(user.admin)               
                if user.admin == "True":                    #Convierte la respuesta del RadioButton de String a Booleano
                    user.admin = True
                else:
                    user.admin = False
                db.session.commit()
                return redirect(url_for('appuser.Users'))
        else:
            return render_template("editarUser.html", editUser = formUser)
    except Exception as ex:
        print(str(ex))
        return redirect(url_for('appuser.Error'))

