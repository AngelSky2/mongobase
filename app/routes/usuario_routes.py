from flask import Blueprint
from app.controllers import usuario_controller

usuario_bp =Blueprint('usuario',__name__,url_prefix="/usuarios")

usuario_bp.route("/",methods=["POST"])
(usuario_controller.crear)
usuario_bp.route("/",methods=["GET"])
(usuario_controller.listar)

@usuario_bp.route('/usuarios',methods=['GET'])
def get_usuarios():
    return{"mensaje":"Servidor funcionando correctamente"}

