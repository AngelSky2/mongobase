from flask import Blueprint
from app.controllers.ingredientes_controller import crear_ingredientes, listar_ingredientes
from app import mongo

ingredientes_bp = Blueprint('ingredientes', __name__, url_prefix='/ingredientes')

@ingredientes_bp.route('', methods=['POST'])
def crear():
    return crear_ingredientes(mongo)

@ingredientes_bp.route('', methods=['GET'])
def listar():
    return listar_ingredientes(mongo)