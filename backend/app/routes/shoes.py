from flask import Blueprint, jsonify
from app.models import Shoe
from app import db

shoes_bp = Blueprint('shoes', __name__)

@shoes_bp.route('/shoes', methods=['GET'])
def get_all_shoes():
    """
    Devuelve TODAS las zapatillas de la base de datos real
    """
    try:
        # Obtener todas las zapatillas de la BD
        shoes = Shoe.query.all()
        
        # Convertir a JSON
        shoes_data = [shoe.to_dict() for shoe in shoes]
        
        return jsonify({
            "success": True,
            "count": len(shoes_data),
            "shoes": shoes_data
        })
    
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500