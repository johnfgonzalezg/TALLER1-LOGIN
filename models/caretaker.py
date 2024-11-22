from db import db

class Caretaker(db.Model):
    """
        Definición de la entidad Caretaker que representa los datos alojados en la tabla 'caretaker' de la BD tables del servidor local
            Atributos:
                id(Integer): Número de identificación (único) del registro de la tabla caretaker
                name(String(100)): Nombre del cuidador
                phone(String(100)): Número telefónico del cuidador
                id_nursery(Integer): Número que define la guardería a la que pertenece el cuidador(Llave foránea)
                dogs(relationship): Atributo que define la relación entre los perros y los cuidadores
    """
    __tablename__ = 'caretaker'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    id_nursery = db.Column(db.Integer, db.ForeignKey('nurseries.id'), nullable=False)
    nursery = db.relationship('Nursery', back_populates='caretakers')
    dogs = db.relationship('Dog', back_populates='caretaker')

    def __init__(self, name, phone, id_nursery):
        self.name = name
        self.phone = phone
        self.id_nursery = id_nursery

    # Getters
    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_phone(self):
        return self
