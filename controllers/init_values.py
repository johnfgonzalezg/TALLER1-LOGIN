from db import db
from models.nursery import Nursery
from models.caretaker import Caretaker
from models.dog import Dog
from models.user import User


# Inicializa la aplicación
def insert_initial_values(app) -> None:
    with app.app_context():
        # Crear datos de prueba para Nursery
        nursery1 = Nursery(name="La Favorita", direction="123 Calle Principal", phone="555-1234")
        nursery2 = Nursery(name="Perro Feliz", direction="456 Avenida Secundaria", phone="555-5678")
        db.session.add(nursery1)
        db.session.add(nursery2)
        db.session.flush()
        # Crear datos de prueba para Caretaker
        caretaker1 = Caretaker(name="Juan Pérez", phone="555-8765", id_nursery=nursery1.id)
        caretaker2 = Caretaker(name="María López", phone="555-4321", id_nursery=nursery2.id)
        db.session.add(caretaker1)
        db.session.add(caretaker2)
        db.session.flush()

        # Crear datos de prueba para Dog
        dog1 = Dog(name="Lassie", race="Collie", age=3, weight=20.5, id_nursery=nursery1.id, id_caretaker=caretaker1.id)
        dog2 = Dog(name="Max", race="Labrador", age=2, weight=25.0, id_nursery=nursery2.id, id_caretaker=caretaker2.id)
        dog3 = Dog(name="Bella", race="Beagle", age=4, weight=10.0, id_nursery=nursery1.id, id_caretaker=caretaker1.id)
        db.session.add(dog1)
        db.session.add(dog2)
        db.session.add(dog3)
        db.session.flush()
        # Crear datos de prueba para User
        user1 = User(username="admin", password="admin123", is_admin=True)
        user2 = User(username="user1", password="password", is_admin=False)
        user3 = User(username="user2", password="password", is_admin=False)
        db.session.add(user1)
        db.session.add(user2)
        db.session.add(user3)

        # Confirma todos los cambios
        db.session.commit()
