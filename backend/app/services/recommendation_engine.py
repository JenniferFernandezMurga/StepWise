def calculate_match_score(user_data, shoe):
    """Calcula compatibilidad entre usuario y zapatilla"""
    score = 0
    factors = {}
    
    # ✅ NUEVO: OBTENER GÉNERO
    gender = user_data.get('gender', 'other')
    print(f"🔍 DEBUG: Género del usuario - {gender}")
    
    # 1. Ancho del pie (30%) - ✅ ACTUALIZADO CON GÉNERO
    user_width = user_data.get('foot_width')
    if user_width == shoe.width_fit:
        factors['width'] = 30
    elif _is_width_compatible(user_width, shoe.width_fit, gender):  # ✅ Género agregado
        factors['width'] = 20
    else:
        factors['width'] = 0
    
    # 2. Soporte de arco (25%)
    if user_data.get('arch_type') == shoe.arch_support:
        factors['arch'] = 25
    else:
        factors['arch'] = 0
    
    # 3. Peso vs capacidad (20%) - ✅ CONVERSIÓN NÚMERO + GÉNERO
    weight_input = user_data.get('weight', 70)
    try:
        weight = int(weight_input)  # ✅ CONVERTIR A NÚMERO
    except (ValueError, TypeError):
        weight = 70
    print(f"🔍 DEBUG: Weight convertido - {weight} (tipo: {type(weight)})")
    
    # ✅ RANGOS DIFERENCIADOS POR GÉNERO
    if gender == 'female':
        # Rangos para mujeres
        if weight < 60 and shoe.weight_capacity == 'light':
            factors['weight'] = 20
        elif 60 <= weight <= 75 and shoe.weight_capacity == 'medium':
            factors['weight'] = 20  
        elif weight > 75 and shoe.weight_capacity == 'heavy':
            factors['weight'] = 20
        else:
            factors['weight'] = 10
    else:
        # Rangos para hombres y otros
        if weight < 70 and shoe.weight_capacity == 'light':
            factors['weight'] = 20
        elif 70 <= weight <= 90 and shoe.weight_capacity == 'medium':
            factors['weight'] = 20  
        elif weight > 90 and shoe.weight_capacity == 'heavy':
            factors['weight'] = 20
        else:
            factors['weight'] = 10

    # 4. Tipo de pisada (25%) 
    user_footstrike = user_data.get('footstrike_type', 'neutral')
    factors['footstrike'] = _calculate_footstrike_compatibility(
        user_footstrike, 
        shoe.footstrike_support
    )
    
    # 5. Actividad (15%)
    if user_data.get('activity_type') == shoe.best_for_activity:
        factors['activity'] = 15
    else:
        factors['activity'] = _calculate_activity_compatibility(
            user_data.get('activity_type'),
            shoe.best_for_activity
        )

    # 6. Distancia (10%)
    factors['distance'] = _calculate_distance_compatibility(
        user_data.get('target_distance', 'training'),
        shoe.distance_capacity
    )

    # 7. Placa de carbono (5%)
    factors['carbon_plate'] = _calculate_carbon_plate_compatibility(
        user_data.get('running_level', 'beginner'),
        user_data.get('target_distance', 'training'),
        shoe.carbon_plate
    )

    # Debug
    print(f"🔍 Factores para {shoe.brand} {shoe.model}: {factors}")
    
    score = sum(factors.values())
    final_score = min(score, 100)
    print(f"🔍 Score final: {final_score}%")
    
    return final_score



def _calculate_footstrike_compatibility(user_footstrike, shoe_support):
    """
    Calcula compatibilidad de pisada (0-15 puntos)
    user_footstrike: 'over_pronation', 'under_pronation', 'neutral'
    shoe_support: 'pronation', 'supination', 'neutral'
    """
    # Si el usuario no sabe su pisada, damos puntos neutrales
    if user_footstrike in ['not_sure', '']:
        return 10
    
    # Usuario neutral es compatible con todo
    if user_footstrike == 'neutral':
        return 15
    
    # Matching específico
    compatibility_map = {
        'over_pronation': {  # Pronador
            'pronation': 15,   # Zapatilla para pronación → Perfecto
            'neutral': 8,      # Zapatilla neutral → Regular
            'supination': 0    # Zapatilla para supinación → Malo
        },
        'under_pronation': {   # Supinador
            'supination': 15,  # Zapatilla para supinación → Perfecto  
            'neutral': 8,      # Zapatilla neutral → Regular
            'pronation': 0     # Zapatilla para pronación → Malo
        }
    }
    
    return compatibility_map.get(user_footstrike, {}).get(shoe_support, 0)

def _calculate_activity_compatibility(user_activity, shoe_activity):
    """Compatibilidad entre actividades"""
    if user_activity == shoe_activity:
        return 15
    
    # Compatibilidad parcial entre tipos de running
    running_activities = ['road_running', 'trail_running']
    if user_activity in running_activities and shoe_activity in running_activities:
        return 8  # Algo de compatibilidad entre road y trail
    
    return 0  # No compatible

def _calculate_distance_compatibility(user_distance, shoe_distance):
    """Compatibilidad de distancia"""
    distance_map = {
        '5k': ['short', 'medium'],
        '10k': ['short', 'medium'], 
        'half_marathon': ['medium', 'long'],
        'marathon': ['long', 'ultra'],
        'ultra': ['ultra'],
        'training': ['short', 'medium', 'long']  # Entrenamiento es flexible
    }
    
    if shoe_distance in distance_map.get(user_distance, []):
        return 10
    return 5

def _calculate_carbon_plate_compatibility(running_level, target_distance, has_carbon):
    """Lógica inteligente para placa de carbono"""
    if not has_carbon:
        return 5  # Sin carbono es más versátil
    
    # Solo carbono para corredores avanzados en distancias largas
    if running_level in ['advanced', 'competitive'] and target_distance in ['half_marathon', 'marathon']:
        return 5  # ✅ Perfecto
    
    if running_level == 'beginner':
        return 0   # ❌ No recomendado
    
    return 2  # ⚠️ Neutral para intermedios

# def _is_width_compatible(user_width, shoe_width):
#     """Lógica inteligente para compatibilidad de ancho"""
#     compatibility_map = {
#         'narrow': ['narrow', 'standard'],
#         'standard': ['narrow', 'standard', 'wide'], 
#         'wide': ['standard', 'wide']
#     }
#     return shoe_width in compatibility_map.get(user_width, [])

def _is_width_compatible(user_width, shoe_width, gender='other'):
    """Lógica inteligente para compatibilidad de ancho - ✅ ACTUALIZADA CON GÉNERO"""
    
    # Mujeres generalmente necesitan tallas más estrechas
    if gender == 'female':
        compatibility_map = {
            'narrow': ['narrow', 'standard'],
            'standard': ['narrow', 'standard'],  # Menos compatibilidad con 'wide'
            'wide': ['standard', 'wide']
        }
    else:
        # Hombres y otros - mapping original
        compatibility_map = {
            'narrow': ['narrow', 'standard'],
            'standard': ['narrow', 'standard', 'wide'], 
            'wide': ['standard', 'wide']
        }
    
    compatible = shoe_width in compatibility_map.get(user_width, [])
    print(f"🔍 Compatibilidad ancho: usuario={user_width}, zapato={shoe_width}, género={gender} → {compatible}")
    return compatible