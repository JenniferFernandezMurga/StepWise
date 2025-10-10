def create_sample_shoes():
    """Crea zapatillas de ejemplo deportivas especializadas"""
    sample_shoes = [
        # ==================== ROAD RUNNING - PRONADORES ====================
        {
            'brand': 'Asics',
            'model': 'Gel-Kayano 28',
            'category': 'running', 
            'price': 159.99,
            'image_url': 'https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=400',
            'affiliate_link': '#',
            'width_fit': 'standard',
            'arch_support': 'high',
            'weight_capacity': 'medium',
            'best_for_activity': 'road_running',  # ✅ Actualizado
            'cushioning': 'maximum',
            'footstrike_support': 'pronation',
            'distance_capacity': 'long',
            'carbon_plate': False,
            'best_for_distance': 'marathon'
        },
        {
            'brand': 'Brooks',
            'model': 'Adrenaline GTS 22',
            'category': 'running',
            'price': 139.99,
            'image_url': 'https://images.unsplash.com/photo-1600185365483-26d7a4cc7519?w=400', 
            'affiliate_link': '#',
            'width_fit': 'wide',
            'arch_support': 'high',
            'weight_capacity': 'heavy',
            'best_for_activity': 'road_running',  # ✅ Actualizado
            'cushioning': 'maximum',
            'footstrike_support': 'pronation',
            'distance_capacity': 'medium',
            'carbon_plate': False,
            'best_for_distance': 'half_marathon'
        },
        
        # ==================== ROAD RUNNING - SUPINADORES ====================
        {
            'brand': 'Hoka',
            'model': 'Clifton 8',
            'category': 'running',
            'price': 139.99,
            'image_url': 'https://images.unsplash.com/photo-1606107557195-0e29a4b5b4aa?w=400',
            'affiliate_link': '#',
            'width_fit': 'standard',
            'arch_support': 'neutral',
            'weight_capacity': 'light',
            'best_for_activity': 'road_running',  # ✅ Actualizado
            'cushioning': 'maximum',
            'footstrike_support': 'supination',
            'distance_capacity': 'long',
            'carbon_plate': False,
            'best_for_distance': 'marathon'
        },
        {
            'brand': 'New Balance',
            'model': 'Fresh Foam 1080v12',
            'category': 'running',
            'price': 149.99,
            'image_url': 'https://images.unsplash.com/photo-1605034313761-73ea4a0cfbf3?w=400',
            'affiliate_link': '#', 
            'width_fit': 'standard',
            'arch_support': 'neutral',
            'weight_capacity': 'medium',
            'best_for_activity': 'road_running',  # ✅ Actualizado
            'cushioning': 'maximum',
            'footstrike_support': 'supination',
            'distance_capacity': 'medium',
            'carbon_plate': False,
            'best_for_distance': 'half_marathon'
        },
        
        # ==================== ROAD RUNNING - NEUTRAL ====================
        {
            'brand': 'Nike',
            'model': 'Pegasus 38',
            'category': 'running',
            'price': 119.99,
            'image_url': 'https://images.unsplash.com/photo-1605348532760-6753d2c43329?w=400',
            'affiliate_link': '#',
            'width_fit': 'standard',
            'arch_support': 'neutral',
            'weight_capacity': 'medium',
            'best_for_activity': 'road_running',  # ✅ Actualizado
            'cushioning': 'medium',
            'footstrike_support': 'neutral',
            'distance_capacity': 'medium',
            'carbon_plate': False,
            'best_for_distance': 'training'
        },
        {
            'brand': 'Adidas',
            'model': 'Ultraboost 22',
            'category': 'running',
            'price': 149.99,
            'image_url': 'https://images.unsplash.com/photo-1549298916-b41d501d3772?w=400',
            'affiliate_link': '#',
            'width_fit': 'standard',
            'arch_support': 'neutral',
            'weight_capacity': 'light',
            'best_for_activity': 'road_running',  # ✅ Actualizado
            'cushioning': 'maximum', 
            'footstrike_support': 'neutral',
            'distance_capacity': 'medium',
            'carbon_plate': False,
            'best_for_distance': '10k'
        },
        
        # ==================== TRAIL RUNNING ====================
        {
            'brand': 'Salomon',
            'model': 'Speedcross 6',
            'category': 'running',
            'price': 139.99,
            'image_url': 'https://images.unsplash.com/photo-1544966503-7cc5ac882d5b?w=400',
            'affiliate_link': '#',
            'width_fit': 'standard',
            'arch_support': 'neutral',
            'weight_capacity': 'medium',
            'best_for_activity': 'trail_running',  # ✅ Específico trail
            'cushioning': 'medium',
            'footstrike_support': 'neutral',
            'distance_capacity': 'ultra',
            'carbon_plate': False,
            'best_for_distance': 'ultra'
        },
        {
            'brand': 'La Sportiva',
            'model': 'Bushido II',
            'category': 'running',
            'price': 149.99,
            'image_url': 'https://images.unsplash.com/photo-1544966503-7cc5ac882d5b?w=400',
            'affiliate_link': '#',
            'width_fit': 'narrow',
            'arch_support': 'neutral',
            'weight_capacity': 'light',
            'best_for_activity': 'trail_running',  # ✅ Específico trail
            'cushioning': 'minimal',
            'footstrike_support': 'neutral',
            'distance_capacity': 'short',
            'carbon_plate': False,
            'best_for_distance': '10k'
        },
        
        # ==================== COMPETICIÓN ROAD ====================
        {
            'brand': 'Nike',
            'model': 'Vaporfly Next% 3',
            'category': 'running',
            'price': 259.99,
            'image_url': 'https://images.unsplash.com/photo-1608231387042-66d1773070a5?w=400',
            'affiliate_link': '#',
            'width_fit': 'narrow',
            'arch_support': 'neutral',
            'weight_capacity': 'light',
            'best_for_activity': 'road_running',  # ✅ Competición road
            'cushioning': 'maximum',
            'footstrike_support': 'neutral',
            'distance_capacity': 'long',
            'carbon_plate': True,
            'best_for_distance': 'marathon'
        },
        
        # ==================== GYM ====================
        {
            'brand': 'Nike',
            'model': 'Metcon 7',
            'category': 'gym',
            'price': 129.99,
            'image_url': 'https://images.unsplash.com/photo-1595950653106-6c9ebd614d3a?w=400',
            'affiliate_link': '#',
            'width_fit': 'standard',
            'arch_support': 'neutral',
            'weight_capacity': 'heavy',
            'best_for_activity': 'gym',
            'cushioning': 'minimal',
            'footstrike_support': 'neutral',
            'distance_capacity': 'short',
            'carbon_plate': False,
            'best_for_distance': 'training'
        },
        {
            'brand': 'Reebok',
            'model': 'Nano X2',
            'category': 'gym',
            'price': 134.99,
            'image_url': 'https://images.unsplash.com/photo-1584735175097-719d848f8449?w=400',
            'affiliate_link': '#',
            'width_fit': 'wide',
            'arch_support': 'low',
            'weight_capacity': 'heavy', 
            'best_for_activity': 'gym',
            'cushioning': 'minimal',
            'footstrike_support': 'neutral',
            'distance_capacity': 'short',
            'carbon_plate': False,
            'best_for_distance': 'training'
        }
    ]
    return sample_shoes