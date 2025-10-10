from flask import Blueprint, request, jsonify
from app.models import Shoe
from app.services.recommendation_engine import calculate_match_score

recommendations_bp = Blueprint('recommendations', __name__)

@recommendations_bp.route('/recommend', methods=['POST'])
def get_recommendations():
    try:
        user_data = request.json
        
        # Validar datos mínimos
        required_fields = ['foot_width', 'arch_type', 'weight', 'activity_type']
        if not all(field in user_data for field in required_fields):
            return jsonify({"error": "Faltan campos requeridos"}), 400
        
        # Obtener todas las zapatillas de la BD
        all_shoes = Shoe.query.all()
        print(f"🔍 Zapatillas en BD: {len(all_shoes)}")
        
        # Calcular recomendaciones
        recommendations = []
        for shoe in all_shoes:
            score = calculate_match_score(user_data, shoe)
            print(f"🔍 {shoe.brand} {shoe.model}: {score} puntos")
            
            if score >= 50:  # Solo zapatillas con buen match
                shoe_data = shoe.to_dict()
                shoe_data['match_score'] = score
                shoe_data['match_percentage'] = f"{score}%"
                recommendations.append(shoe_data)
        
        print(f"🔍 Recomendaciones encontradas: {len(recommendations)}")
        
        # Ordenar por score descendente
        recommendations.sort(key=lambda x: x['match_score'], reverse=True)
        
        return jsonify({
            "success": True,
            "recommendations": recommendations[:5],  # Top 5
            "user_data_received": user_data
        })
    
    except Exception as e:
        print(f"❌ ERROR: {e}")
        return jsonify({"error": str(e)}), 500