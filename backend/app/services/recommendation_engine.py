# def calculate_match_score(user_data, shoe):
#     """Calcula compatibilidad entre usuario y zapatilla"""
#     score = 0
#     factors = {}
    
#     # ✅ NUEVO: OBTENER GÉNERO
#     gender = user_data.get('gender', 'other')
#     print(f"🔍 DEBUG: Género del usuario - {gender}")
    
#     # 1. Ancho del pie (30%) - ✅ ACTUALIZADO CON GÉNERO
#     user_width = user_data.get('foot_width')
#     if user_width == shoe.width_fit:
#         factors['width'] = 30
#     elif _is_width_compatible(user_width, shoe.width_fit, gender):  # ✅ Género agregado
#         factors['width'] = 20
#     else:
#         factors['width'] = 0
    
#     # 2. Soporte de arco (25%)
#     if user_data.get('arch_type') == shoe.arch_support:
#         factors['arch'] = 25
#     else:
#         factors['arch'] = 0
    
#     # 3. Peso vs capacidad (20%) - ✅ CONVERSIÓN NÚMERO + GÉNERO
#     weight_input = user_data.get('weight', 70)
#     try:
#         weight = int(weight_input)  # ✅ CONVERTIR A NÚMERO
#     except (ValueError, TypeError):
#         weight = 70
#     print(f"🔍 DEBUG: Weight convertido - {weight} (tipo: {type(weight)})")
    
#     # ✅ RANGOS DIFERENCIADOS POR GÉNERO
#     if gender == 'female':
#         # Rangos para mujeres
#         if weight < 60 and shoe.weight_capacity == 'light':
#             factors['weight'] = 20
#         elif 60 <= weight <= 75 and shoe.weight_capacity == 'medium':
#             factors['weight'] = 20  
#         elif weight > 75 and shoe.weight_capacity == 'heavy':
#             factors['weight'] = 20
#         else:
#             factors['weight'] = 10
#     else:
#         # Rangos para hombres y otros
#         if weight < 70 and shoe.weight_capacity == 'light':
#             factors['weight'] = 20
#         elif 70 <= weight <= 90 and shoe.weight_capacity == 'medium':
#             factors['weight'] = 20  
#         elif weight > 90 and shoe.weight_capacity == 'heavy':
#             factors['weight'] = 20
#         else:
#             factors['weight'] = 10

#     # 4. Tipo de pisada (25%) 
#     user_footstrike = user_data.get('footstrike_type', 'neutral')
#     factors['footstrike'] = _calculate_footstrike_compatibility(
#         user_footstrike, 
#         shoe.footstrike_support
#     )
    
#     # 5. Actividad (15%)
#     if user_data.get('activity_type') == shoe.best_for_activity:
#         factors['activity'] = 15
#     else:
#         factors['activity'] = _calculate_activity_compatibility(
#             user_data.get('activity_type'),
#             shoe.best_for_activity
#         )

#     # 6. Distancia (10%)
#     factors['distance'] = _calculate_distance_compatibility(
#         user_data.get('target_distance', 'training'),
#         shoe.distance_capacity
#     )

#     # 7. Placa de carbono (5%)
#     factors['carbon_plate'] = _calculate_carbon_plate_compatibility(
#         user_data.get('running_level', 'beginner'),
#         user_data.get('target_distance', 'training'),
#         shoe.carbon_plate
#     )

#     # Debug
#     print(f"🔍 Factores para {shoe.brand} {shoe.model}: {factors}")
    
#     score = sum(factors.values())
#     final_score = min(score, 100)
#     print(f"🔍 Score final: {final_score}%")
    
#     return final_score
# 00


# def _calculate_footstrike_compatibility(user_footstrike, shoe_support):
#     """
#     Calcula compatibilidad de pisada (0-15 puntos)
#     user_footstrike: 'over_pronation', 'under_pronation', 'neutral'
#     shoe_support: 'pronation', 'supination', 'neutral'
#     """
#     # Si el usuario no sabe su pisada, damos puntos neutrales
#     if user_footstrike in ['not_sure', '']:
#         return 10
    
#     # Usuario neutral es compatible con todo
#     if user_footstrike == 'neutral':
#         return 15
    
#     # Matching específico
#     compatibility_map = {
#         'over_pronation': {  # Pronador
#             'pronation': 15,   # Zapatilla para pronación → Perfecto
#             'neutral': 8,      # Zapatilla neutral → Regular
#             'supination': 0    # Zapatilla para supinación → Malo
#         },
#         'under_pronation': {   # Supinador
#             'supination': 15,  # Zapatilla para supinación → Perfecto  
#             'neutral': 8,      # Zapatilla neutral → Regular
#             'pronation': 0     # Zapatilla para pronación → Malo
#         }
#     }
    
#     return compatibility_map.get(user_footstrike, {}).get(shoe_support, 0)

# def _calculate_activity_compatibility(user_activity, shoe_activity):
#     """Compatibilidad entre actividades"""
#     if user_activity == shoe_activity:
#         return 15
    
#     # Compatibilidad parcial entre tipos de running
#     running_activities = ['road_running', 'trail_running']
#     if user_activity in running_activities and shoe_activity in running_activities:
#         return 8  # Algo de compatibilidad entre road y trail
    
#     return 0  # No compatible

# def _calculate_distance_compatibility(user_distance, shoe_distance):
#     """Compatibilidad de distancia"""
#     distance_map = {
#         '5k': ['short', 'medium'],
#         '10k': ['short', 'medium'], 
#         'half_marathon': ['medium', 'long'],
#         'marathon': ['long', 'ultra'],
#         'ultra': ['ultra'],
#         'training': ['short', 'medium', 'long']  # Entrenamiento es flexible
#     }
    
#     if shoe_distance in distance_map.get(user_distance, []):
#         return 10
#     return 5

# def _calculate_carbon_plate_compatibility(running_level, target_distance, has_carbon):
#     """Lógica inteligente para placa de carbono"""
#     if not has_carbon:
#         return 5  # Sin carbono es más versátil
    
#     # Solo carbono para corredores avanzados en distancias largas
#     if running_level in ['advanced', 'competitive'] and target_distance in ['half_marathon', 'marathon']:
#         return 5  # ✅ Perfecto
    
#     if running_level == 'beginner':
#         return 0   # ❌ No recomendado
    
#     return 2  # ⚠️ Neutral para intermedios

# # def _is_width_compatible(user_width, shoe_width):
# #     """Lógica inteligente para compatibilidad de ancho"""
# #     compatibility_map = {
# #         'narrow': ['narrow', 'standard'],
# #         'standard': ['narrow', 'standard', 'wide'], 
# #         'wide': ['standard', 'wide']
# #     }
# #     return shoe_width in compatibility_map.get(user_width, [])

# def _is_width_compatible(user_width, shoe_width, gender='other'):
#     """Lógica inteligente para compatibilidad de ancho - ✅ ACTUALIZADA CON GÉNERO"""
    
#     # Mujeres generalmente necesitan tallas más estrechas
#     if gender == 'female':
#         compatibility_map = {
#             'narrow': ['narrow', 'standard'],
#             'standard': ['narrow', 'standard'],  # Menos compatibilidad con 'wide'
#             'wide': ['standard', 'wide']
#         }
#     else:
#         # Hombres y otros - mapping original
#         compatibility_map = {
#             'narrow': ['narrow', 'standard'],
#             'standard': ['narrow', 'standard', 'wide'], 
#             'wide': ['standard', 'wide']
#         }
    
#     compatible = shoe_width in compatibility_map.get(user_width, [])
#     print(f"🔍 Compatibilidad ancho: usuario={user_width}, zapato={shoe_width}, género={gender} → {compatible}")
#     return compatible




#SEGUNDA OPCION CON GENDER INCLUIDO
# def calculate_match_score(user_data, shoe):
#     """NUEVO: Calcula compatibilidad con sistema de veto y género"""
#     factors = {}
#     veto_reasons = []  # ✅ RAZONES DE RECHAZO
    
#     # ✅ OBTENER GÉNERO
#     user_gender = user_data.get('gender', 'other')
#     shoe_gender = getattr(shoe, 'gender', 'unisex')
#     print(f"🔍 DEBUG: Género usuario={user_gender}, zapatilla={shoe_gender}")
    
#     # ✅ VETO 0: GÉNERO INCOMPATIBLE (PRIMER FILTRO)
#     if shoe_gender == 'male' and user_gender == 'female':
#         veto_reasons.append("❌ Zapatilla solo para hombres")
#         return 0, veto_reasons
        
#     if shoe_gender == 'female' and user_gender == 'male':
#         veto_reasons.append("❌ Zapatilla solo para mujeres") 
#         return 0, veto_reasons
    
#     # ✅ VETO 1: Pisada incompatible
#     user_footstrike = user_data.get('footstrike_type', 'neutral')
#     shoe_support = shoe.footstrike_support
    
#     if user_footstrike == 'over_pronation' and shoe_support == 'supination':
#         veto_reasons.append("❌ INCOMPATIBLE: Eres pronador pero la zapatilla es para supinadores")
#         return 0, veto_reasons
    
#     if user_footstrike == 'under_pronation' and shoe_support == 'pronation':
#         veto_reasons.append("❌ INCOMPATIBLE: Eres supinador pero la zapatilla es para pronadores") 
#         return 0, veto_reasons
    
#     # ✅ VETO 2: Actividad completamente incompatible
#     user_activity = user_data.get('activity_type')
#     shoe_activity = shoe.best_for_activity
    
#     activity_incompatibilities = {
#         'gym': ['road_running', 'trail_running', 'walking'],
#         'road_running': ['gym'],
#         'trail_running': ['gym'], 
#         'walking': ['gym']
#     }
    
#     if user_activity in activity_incompatibilities and shoe_activity in activity_incompatibilities[user_activity]:
#         veto_reasons.append(f"❌ INCOMPATIBLE: Para {user_activity} pero zapatilla de {shoe_activity}")
#         return 0, veto_reasons
    
#     # ✅ 2. SCORING PRINCIPAL (solo si pasa los vetos)
    
#     # 1. Ancho del pie (25 puntos) - ✅ CON GÉNERO
#     user_width = user_data.get('foot_width')
#     if user_width == shoe.width_fit:
#         factors['width'] = 25
#     elif _is_width_compatible(user_width, shoe.width_fit, user_gender):
#         factors['width'] = 15
#     else:
#         factors['width'] = 5
    
#     # 2. Soporte de arco (20 puntos)
#     if user_data.get('arch_type') == shoe.arch_support:
#         factors['arch'] = 20
#     else:
#         factors['arch'] = 8
    
#     # 3. Peso vs capacidad (20 puntos) - ✅ CONVERSIÓN NÚMERO + GÉNERO
#     weight_input = user_data.get('weight', 70)
#     try:
#         weight = int(weight_input)  # ✅ CONVERTIR A NÚMERO
#     except (ValueError, TypeError):
#         weight = 70
#     print(f"🔍 DEBUG: Weight convertido - {weight} (tipo: {type(weight)})")
    
#     # ✅ RANGOS DIFERENCIADOS POR GÉNERO
#     if user_gender == 'female':
#         # Rangos para mujeres
#         if weight < 60 and shoe.weight_capacity == 'light':
#             factors['weight'] = 20
#         elif 60 <= weight <= 75 and shoe.weight_capacity == 'medium':
#             factors['weight'] = 20  
#         elif weight > 75 and shoe.weight_capacity == 'heavy':
#             factors['weight'] = 20
#         else:
#             factors['weight'] = 8
#     else:
#         # Rangos para hombres y otros
#         if weight < 70 and shoe.weight_capacity == 'light':
#             factors['weight'] = 20
#         elif 70 <= weight <= 90 and shoe.weight_capacity == 'medium':
#             factors['weight'] = 20  
#         elif weight > 90 and shoe.weight_capacity == 'heavy':
#             factors['weight'] = 20
#         else:
#             factors['weight'] = 8
    
#     # 4. Tipo de pisada (15 puntos) - ✅ MEJORADO
#     factors['footstrike'] = _calculate_footstrike_compatibility(user_footstrike, shoe_support)
    
#     # 5. Actividad (10 puntos) - ✅ MEJORADO  
#     if user_activity == shoe_activity:
#         factors['activity'] = 10
#     elif _are_activities_related(user_activity, shoe_activity):
#         factors['activity'] = 6
#     else:
#         factors['activity'] = 2
    
#     # 6. Distancia (5 puntos)
#     factors['distance'] = _calculate_distance_compatibility(
#         user_data.get('target_distance', 'training'),
#         shoe.distance_capacity
#     )
    
#     # 7. Placa de carbono (5 puntos)
#     factors['carbon_plate'] = _calculate_carbon_plate_compatibility(
#         user_data.get('running_level', 'beginner'),
#         user_data.get('target_distance', 'training'),
#         shoe.carbon_plate
#     )
    
#     # ✅ BONUS: Puntos extra por match perfecto de género
#     if user_gender == shoe_gender:
#         factors['gender_match'] = 5  # Puntos extra
#     elif shoe_gender == 'unisex':
#         factors['gender_match'] = 3  # Puntos por unisex
#     else:
#         factors['gender_match'] = 0
    
#     score = sum(factors.values())
#     final_score = min(score, 100)
    
#     print(f"🔍 {shoe.brand} {shoe.model}: {final_score}% - Factores: {factors}")
#     if veto_reasons:
#         print(f"🔍 Vetos: {veto_reasons}")
    
#     return final_score, veto_reasons


# def _calculate_footstrike_compatibility(user_footstrike, shoe_support):
#     """✅ MEJORADO: Scoring más estricto para pisada"""
    
#     if user_footstrike in ['not_sure', '']:
#         return 8  # Neutral por defecto
    
#     # Usuario neutral es compatible con todo
#     if user_footstrike == 'neutral':
#         return 15
    
#     # Matching específico - MÁS ESTRICTO
#     compatibility_map = {
#         'over_pronation': {
#             'pronation': 15,   # Perfecto
#             'neutral': 6,      # Aceptable pero no ideal
#             'supination': 0    # Ya vetado arriba
#         },
#         'under_pronation': {
#             'supination': 15,  # Perfecto
#             'neutral': 6,      # Aceptable pero no ideal  
#             'pronation': 0     # Ya vetado arriba
#         }
#     }
    
#     return compatibility_map.get(user_footstrike, {}).get(shoe_support, 0)


# def _are_activities_related(activity1, activity2):
#     """✅ NUEVO: Determina si actividades son relacionadas"""
#     related_groups = {
#         'running_group': ['road_running', 'trail_running'],
#         'casual_group': ['walking', 'lifestyle']
#     }
    
#     for group in related_groups.values():
#         if activity1 in group and activity2 in group:
#             return True
#     return False


# def _calculate_distance_compatibility(user_distance, shoe_distance):
#     """Compatibilidad de distancia"""
#     distance_map = {
#         '5k': ['short', 'medium'],
#         '10k': ['short', 'medium'], 
#         'half_marathon': ['medium', 'long'],
#         'marathon': ['long', 'ultra'],
#         'ultra': ['ultra'],
#         'training': ['short', 'medium', 'long']  # Entrenamiento es flexible
#     }
    
#     if shoe_distance in distance_map.get(user_distance, []):
#         return 5
#     return 2


# def _calculate_carbon_plate_compatibility(running_level, target_distance, has_carbon):
#     """Lógica inteligente para placa de carbono"""
#     if not has_carbon:
#         return 5  # Sin carbono es más versátil
    
#     # Solo carbono para corredores avanzados en distancias largas
#     if running_level in ['advanced', 'competitive'] and target_distance in ['half_marathon', 'marathon']:
#         return 5  # ✅ Perfecto
    
#     if running_level == 'beginner':
#         return 0   # ❌ No recomendado
    
#     return 2  # ⚠️ Neutral para intermedios


# def _is_width_compatible(user_width, shoe_width, gender='other'):
#     """Lógica inteligente para compatibilidad de ancho - ✅ ACTUALIZADA CON GÉNERO"""
    
#     # Mujeres generalmente necesitan tallas más estrechas
#     if gender == 'female':
#         compatibility_map = {
#             'narrow': ['narrow', 'standard'],
#             'standard': ['narrow', 'standard'],  # Menos compatibilidad con 'wide'
#             'wide': ['standard', 'wide']
#         }
#     else:
#         # Hombres y otros - mapping original
#         compatibility_map = {
#             'narrow': ['narrow', 'standard'],
#             'standard': ['narrow', 'standard', 'wide'], 
#             'wide': ['standard', 'wide']
#         }
    
#     compatible = shoe_width in compatibility_map.get(user_width, [])
#     print(f"🔍 Compatibilidad ancho: usuario={user_width}, zapato={shoe_width}, género={gender} → {compatible}")
#     return compatible


# def _get_safe_weight(weight_input):
#     """✅ Helper: Conversión segura de peso"""
#     try:
#         return int(weight_input)
#     except (ValueError, TypeError):
#         return 70



#SISTEMA HIBRIDO ALGORITMO

def recommend_shoes_optimized(user_data):
    """Enfoque híbrido: filtrado estricto + scoring simplificado"""
    from app.models import Shoe
    
    print(f"🎯 Iniciando recomendación para: {user_data}")
    
    # ✅ PRIMERO: FILTRADO ESTRICTO (SQL en base de datos)
    query = Shoe.query
    
    # 1. Filtro por GÉNERO (obligatorio)
    user_gender = user_data.get('gender')
    if user_gender in ['male', 'female']:
        query = query.filter(
            (Shoe.gender == user_gender) | 
            (Shoe.gender == 'unisex')
        )
        print(f"🔍 Filtro género: {user_gender}")
    
    # 2. Filtro por ACTIVIDAD (incompatibilidades graves)
    user_activity = user_data.get('activity_type')
    if user_activity:
        if user_activity == 'trail_running':
            query = query.filter(Shoe.best_for_activity == 'trail_running')
        elif user_activity == 'road_running':
            query = query.filter(Shoe.best_for_activity == 'road_running') 
        elif user_activity == 'gym':
            query = query.filter(Shoe.best_for_activity == 'gym')
        elif user_activity == 'walking':
            query = query.filter(Shoe.best_for_activity == 'walking')
        print(f"🔍 Filtro actividad: {user_activity}")
    
    # 3. Filtro por PISADA (incompatibilidades graves)
    user_footstrike = user_data.get('footstrike_type')
    if user_footstrike:
        if user_footstrike == 'over_pronation':
            query = query.filter(Shoe.footstrike_support != 'supination')
        elif user_footstrike == 'under_pronation':
            query = query.filter(Shoe.footstrike_support != 'pronation')
        print(f"🔍 Filtro pisada: {user_footstrike}")
    
    # 4. Filtro por CARBONO para principiantes
    user_level = user_data.get('running_level', 'beginner')
    if user_level == 'beginner':
        query = query.filter(Shoe.carbon_plate == False)
        print(f"🔍 Filtro carbono: principiantes → sin carbono")
    
    # 5. Filtro por DISTANCIA para ultramaratón
    user_distance = user_data.get('target_distance')
    if user_distance == 'ultra':
        query = query.filter(Shoe.distance_capacity.in_(['ultra', 'long']))
        print(f"🔍 Filtro distancia: ultra → ultra/long")
    
    # Ejecutar query filtrada
    filtered_shoes = query.all()
    print(f"✅ Después de filtros: {len(filtered_shoes)} zapatillas")
    
    # ✅ SEGUNDO: SCORING SIMPLIFICADO (solo para filtradas)
    scored_shoes = []
    
    for shoe in filtered_shoes:
        score, match_details = calculate_simple_score(user_data, shoe)
        
        if score >= 50:  # Solo recomendaciones decentes
            shoe_data = shoe.to_dict()
            shoe_data['match_score'] = score
            shoe_data['match_percentage'] = f"{score}%"
            shoe_data['match_details'] = match_details  # Para mostrar por qué
            scored_shoes.append(shoe_data)
    
    # Ordenar por score descendente
    scored_shoes.sort(key=lambda x: x['match_score'], reverse=True)
    
    print(f"🎯 Recomendaciones finales: {len(scored_shoes)} zapatillas")
    for i, shoe in enumerate(scored_shoes[:3]):
        print(f"   {i+1}. {shoe['brand']} {shoe['model']} - {shoe['match_percentage']}")
    
    return scored_shoes[:8]  # Top 8


def calculate_simple_score(user_data, shoe):
    """Scoring simplificado - solo factores importantes"""
    score = 0
    match_details = []
    
    # ✅ FACTOR CRÍTICO 1: ANCHO DEL PIE (30 puntos)
    user_width = user_data.get('foot_width')
    if user_width == shoe.width_fit:
        score += 30
        match_details.append("✅ Ancho perfecto")
    elif _is_width_compatible(user_width, shoe.width_fit, user_data.get('gender')):
        score += 20
        match_details.append("✅ Ancho compatible")
    else:
        match_details.append("⚠️ Ancho no ideal")
    
    # ✅ FACTOR CRÍTICO 2: SOPORTE DE ARCO (25 puntos)
    if user_data.get('arch_type') == shoe.arch_support:
        score += 25
        match_details.append("✅ Arco perfecto")
    else:
        match_details.append("⚠️ Arco diferente")
    
    # ✅ FACTOR IMPORTANTE 3: PESO vs CAPACIDAD (20 puntos)
    weight = _get_safe_weight(user_data.get('weight'))
    user_gender = user_data.get('gender', 'other')
    
    if user_gender == 'female':
        if weight < 60 and shoe.weight_capacity == 'light':
            score += 20
            match_details.append("✅ Peso ideal (mujer)")
        elif 60 <= weight <= 75 and shoe.weight_capacity == 'medium':
            score += 20
            match_details.append("✅ Peso ideal (mujer)")
        elif weight > 75 and shoe.weight_capacity == 'heavy':
            score += 20
            match_details.append("✅ Peso ideal (mujer)")
    else:
        if weight < 70 and shoe.weight_capacity == 'light':
            score += 20
            match_details.append("✅ Peso ideal (hombre)")
        elif 70 <= weight <= 90 and shoe.weight_capacity == 'medium':
            score += 20
            match_details.append("✅ Peso ideal (hombre)")
        elif weight > 90 and shoe.weight_capacity == 'heavy':
            score += 20
            match_details.append("✅ Peso ideal (hombre)")
    
    # ✅ FACTOR IMPORTANTE 4: ACTIVIDAD (15 puntos)
    if user_data.get('activity_type') == shoe.best_for_activity:
        score += 15
        match_details.append("✅ Actividad perfecta")
    else:
        match_details.append("⚠️ Actividad diferente")
    
    # ✅ FACTOR SECUNDARIO 5: DISTANCIA (10 puntos)
    user_distance = user_data.get('target_distance', 'training')
    if user_distance == 'ultra' and shoe.distance_capacity == 'ultra':
        score += 10
        match_details.append("✅ Perfecta para ultramaratón")
    elif user_distance == 'marathon' and shoe.distance_capacity == 'long':
        score += 10
        match_details.append("✅ Perfecta para maratón")
    elif _is_distance_compatible(user_distance, shoe.distance_capacity):
        score += 7
        match_details.append("✅ Distancia compatible")
    
    return min(score, 100), match_details


def _is_distance_compatible(user_distance, shoe_distance):
    """Compatibilidad simplificada de distancia"""
    compatibility_map = {
        '5k': ['short', 'medium'],
        '10k': ['short', 'medium'], 
        'half_marathon': ['medium', 'long'],
        'marathon': ['long', 'ultra'],
        'ultra': ['ultra', 'long'],
        'training': ['short', 'medium', 'long']
    }
    return shoe_distance in compatibility_map.get(user_distance, [])


def _is_width_compatible(user_width, shoe_width, gender='other'):
    """Misma función de compatibilidad de ancho"""
    if gender == 'female':
        compatibility_map = {
            'narrow': ['narrow', 'standard'],
            'standard': ['narrow', 'standard'],
            'wide': ['standard', 'wide']
        }
    else:
        compatibility_map = {
            'narrow': ['narrow', 'standard'],
            'standard': ['narrow', 'standard', 'wide'], 
            'wide': ['standard', 'wide']
        }
    return shoe_width in compatibility_map.get(user_width, [])


def _get_safe_weight(weight_input):
    """Conversión segura de peso"""
    try:
        return int(weight_input)
    except (ValueError, TypeError):
        return 70