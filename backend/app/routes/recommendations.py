from flask import Blueprint, request, jsonify
from app.models import Shoe
from app.services.recommendation_engine import calculate_match_score

recommendations_bp = Blueprint('recommendations', __name__)

@recommendations_bp.route('/recommend', methods=['POST'])
def get_recommendations():
    try:
        user_data = request.json
        print(f"🔍 Datos recibidos del frontend: {user_data}")
        
        # ✅ VALIDACIÓN ACTUALIZADA CON GÉNERO
        required_fields = ['gender', 'foot_width', 'arch_type', 'weight', 'activity_type']  # ✅ Género agregado
        if not all(field in user_data for field in required_fields):
            return jsonify({"error": "Faltan campos requeridos"}), 400
        
        # ✅ VALIDACIÓN ADICIONAL: Verificar tipos de datos
        if not isinstance(user_data.get('weight'), (int, float)):
            print("⚠️  Weight no es número, convirtiendo...")
            try:
                user_data['weight'] = int(user_data['weight'])
            except (ValueError, TypeError):
                user_data['weight'] = 70
        
        print(f"🔍 Datos validados: {user_data}")
        
        # Obtener todas las zapatillas de la BD
        all_shoes = Shoe.query.all()
        print(f"🔍 Zapatillas en BD: {len(all_shoes)}")
        
        # Calcular recomendaciones
        recommendations = []
        for shoe in all_shoes:
            score = calculate_match_score(user_data, shoe)
            
            if score >= 50:
                shoe_data = shoe.to_dict()
                shoe_data['match_score'] = score
                shoe_data['match_percentage'] = f"{score}%"
                recommendations.append(shoe_data)
        
        print(f"✅ Recomendaciones encontradas: {len(recommendations)}")
        
        recommendations.sort(key=lambda x: x['match_score'], reverse=True)
        
        return jsonify({
            "success": True,
            "recommendations": recommendations[:5],
            "user_data_received": user_data
        })
    
    except Exception as e:
        print(f"❌ ERROR: {str(e)}")
        import traceback
        print(f"❌ TRACEBACK: {traceback.format_exc()}")
        return jsonify({"error": str(e)}), 500