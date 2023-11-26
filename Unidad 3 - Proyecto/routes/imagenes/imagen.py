from flask import Blueprint,request,jsonify,render_template, redirect, url_for
from sqlalchemy import exc
from models import Images, User
from app import db, flash
from auth import tokenCheck,verificar
import base64

imagesUser = Blueprint('imageUser',__name__,template_folder="templates")

def render_image(data):
    render_img = base64.b64encode(data).decode('ascii')
    return render_img

@imagesUser.route("/display", methods = ["GET"])
def Display():
    token = request.args.get("token")
    info = verificar(token)["data"]
    searchImage = Images.query.filter_by(user_id=info['user_id']).first()
    if searchImage:
        return jsonify({"status":200, "data":searchImage.rendered_data})
    else:
        return jsonify({"status":400, "data":"error"})
    
@imagesUser.route("/displayImage", methods=["GET"])
def search_page():
    token = request.args.get('token')
    info = verificar(token)['data']
    print(info)
    searchImage = Images.query.filter_by(user_id=info['user_id']).first()
    if searchImage:
        image = searchImage.rendered_data
        return render_template('PerfilUsuario.html',imagen=image)
    else:
        return render_template('PerfilUsuario.html',imagen={})

@imagesUser.route('/uploadPerfil',methods=['POST'])
@tokenCheck
def upload(usuario):
    searchImage = Images.query.filter_by(user_id=usuario['user_id']).first()
    if searchImage:
        file = request.files['inputFile']
        data = file.read()
        render_file = render_image(data)
        searchImage.rendered_data= render_file
        searchImage.data=data
        db.session.commit()
        return jsonify({"Message":"Imagen Actualizada"})
    else:
        file = request.files['inputFile']
        data = file.read()
        render_file=render_image(data)
        newFile= Images()
        newFile.type = "Perfil"
        newFile.rendered_data=render_file
        newFile.data=data
        newFile.user_id=usuario['user_id']
        db.session.add(newFile)
        db.session.commit()
        return jsonify({"Message":"Imagen agregada"})

@imagesUser.route('/uploadImage', methods = ["GET", "POST"])
def UploadImage():
    if request.method == "POST":
        tkn = request.args.get("token")
        usuario = verificar(tkn)['data']
        searchImage = Images.query.filter_by(user_id=usuario['user_id']).first()
        if searchImage:
            file = request.files["file1"]
            data = file.read()
            renderer = render_image(data)
            searchImage.rendered_data = renderer
            searchImage.data = data
            db.session.commit()
        else:
            file = request.files['file1']
            data = file.read()
            render_file=render_image(data)
            newFile= Images()
            newFile.type = "Perfil"
            newFile.rendered_data=render_file
            newFile.data=data
            newFile.user_id=usuario['user_id']
            db.session.add(newFile)
            db.session.commit()
        flash("Se Ha Actualizado Su Foto De Perfil", "info")
        return redirect('/displayImage?token='+tkn)
    else:
        return render_template('updateImagenUsuario.html')