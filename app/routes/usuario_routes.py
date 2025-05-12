from flask import Blueprint
from app.controllers import usuario_controller


usuario_bp =Blueprint('usuario',__name__,url_prefix="/usuarios")

usuario_bp.route("/crear", methods=["POST"])(usuario_controller.crear)
usuario_bp.route("/",methods=["GET"])(usuario_controller.listar)

@usuario_bp.route('/ping',methods=['GET'])
def ping():
    return{"mensaje":"Servidor funcionando correctamente"}

