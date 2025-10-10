import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app import create_app, db
from app.models import Shoe
from app.services.sample_data import create_sample_shoes

def populate_database():
    app = create_app()
    
    with app.app_context():
        # Limpiar tabla existente
        db.drop_all()
        db.create_all()
        
        # Crear zapatillas de ejemplo
        sample_shoes = create_sample_shoes()
        
        for shoe_data in sample_shoes:
            shoe = Shoe(**shoe_data)
            db.session.add(shoe)
        
        db.session.commit()
        print(f"✅ Base de datos poblada con {len(sample_shoes)} zapatillas")

if __name__ == '__main__':
    populate_database()