from db import db


class Nursery(db.Model):
    """
        Definición de la entidad Nursery que representa los datos alojados en la tabla 'nurseries' de la BD tables del servidor local
            Atributos:
                id(int): Número de identificación (único) del registro de la tabla nurseries
                name(String(100)): Nombre de la guardería
                direction(String(100)): Dirección de ubicación de la guardería
                phone(String(100)): Número telefónico de la guardería
                caretakers(relationship): variable que define la relación entre las guarderías y los cuidadores
                dogs(relationship): variable que define la relación entre las guarderías y los perros
    """
    __tablename__ = 'nurseries'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    direction = db.Column(db.String(100), nullable = False)
    phone = db.Column(db.String(20), nullable = False)
    caretakers = db.relationship('Caretaker', back_populates = 'nursery')
    dogs = db.relationship('Dog', back_populates = 'nursery')

    def __init__(self, name, direction, phone): 
        self.name = name 
        self.direction = direction 
        self.phone = phone 
    
    # Getters 
    def get_id(self): 
        return self.id 
    
    def get_name(self): 
        return self.name 
    
    def get_direction(self): 
        return self.direction 
    
    def get_phone(self): 
        return self.phone 
    
    def get_caretakers(self): 
        return self.caretakers 
    
    def get_dogs(self): 
        return self.dogs 
    # Setters 
    def set_name(self, name): 
        self.name = name 
    
    def set_direction(self, direction): 
        self.direction = direction 
        
    def set_phone(self, phone): 
        self.phone = phone 
    
    def set_caretakers(self, caretakers): 
        self.caretakers = caretakers 
    
    def set_dogs(self, dogs): 
        self.dogs = dogs
        