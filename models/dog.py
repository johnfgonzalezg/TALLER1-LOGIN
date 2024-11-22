from db import db

class Dog(db.Model):
    """
        Definición de la entidad Dog que representa los datos alojados en la tabla 'dog' de la BD tables del servidor local
            Atributos:
                id(int): Número de identificación (único) del registro de la tabla dog
                name(String(100)): Nombre del perro
                race(String(45)): Raza del perro
                age(Integer): Edad del perro
                weight(Numeric(10,2)): Peso del perro
                id_nursery(Integer): Id que identifica a cual guardería está asociado el perro(llave foránea)
                id_caretaker(Integer): Id que identifica quien es el cuidador del perro(llave foránea)
                nursery(relationship): Atributo que define la relación entre los perros y las guarderías
                caretaker(relationship): Atributo que define la relación entre los perros y los cuidadores
    """
    __tablename__ = 'dog'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    race = db.Column(db.String(45), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    weight = db.Column(db.Numeric(10, 2), nullable=False)
    id_nursery = db.Column(db.Integer, db.ForeignKey('nurseries.id'), nullable=False)
    id_caretaker = db.Column(db.Integer, db.ForeignKey('caretaker.id'), nullable=False)
    nursery = db.relationship('Nursery', back_populates='dogs')
    caretaker = db.relationship('Caretaker', back_populates='dogs')

    def __init__(self, name, race, age, weight, id_nursery, id_caretaker):
        self.name = name
        self.race = race
        self.age = age
        self.weight = weight
        self.id_nursery = id_nursery
        self.id_caretaker = id_caretaker

    # Getters
    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_race(self):
        return self.race

    def get_age(self):
        return self.age

    def get_weight(self):
        return self.weight

    def get_id_nursery(self):
        return self.id_nursery

    def get_id_caretaker(self):
        return self.id_caretaker

    def get_nursery(self):
        return self.nursery

    def get_caretaker(self):
        return self.caretaker

    # Setters
    def set_name(self, name):
        self.name = name

    def set_race(self, race):
        self.race = race

    def set_age(self, age):
        self.age = age

    def set_weight(self, weight):
        self.weight = weight

    def set_id_nursery(self, id_nursery):
        self.id_nursery = id_nursery

    def set_id_caretaker(self, id_caretaker):
        self.id_caretaker = id_caretaker

    def set_nursery(self, nursery):
        self.nursery = nursery

    def set_caretaker(self, caretaker):
        self.caretaker = caretaker

