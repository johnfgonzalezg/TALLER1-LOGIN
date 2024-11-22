from flask import Blueprint, render_template, request, redirect, url_for
from db import db
from models.dog import Dog
from models.caretaker import Caretaker

dog_bp = Blueprint('dog', __name__)


@dog_bp.route('/', methods=['GET'], endpoint='index')
def index():
    dogs = Dog.query.all()
    return render_template('dog/index.html', dogs=dogs)


@dog_bp.route('/dogs', methods=['GET'])
def list_dogs():
    dogs = Dog.query.all()
    return render_template('dog/dog_list.html', dogs=dogs)

@dog_bp.route('/dog/add', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        name = request.form['name']
        race = request.form['race']
        age = request.form['age']
        weight = request.form['weight']
        id_nursery = request.form['id_nursery']
        id_caretaker = request.form['id_caretaker']
        dog = Dog(name=name, race=race, age=age, weight=weight, id_nursery=id_nursery, id_caretaker=id_caretaker)
        db.session.add(dog)
        db.session.commit()
        return redirect(url_for('dog.index'))
    caretakers = Caretaker.query.all()
    return render_template('dog/create.html', caretakers=caretakers)

@dog_bp.route('/dog/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    dog = Dog.query.get_or_404(id)
    if request.method == 'POST':
        dog.name = request.form['name']
        dog.race = request.form['race']
        dog.age = request.form['age']
        dog.weight = request.form['weight']
        dog.id_nursery = request.form['id_nursery']
        dog.id_caretaker = request.form['id_caretaker']
        db.session.commit()
        return redirect(url_for('dog.index'))
    caretakers = Caretaker.query.all()
    return render_template('dog/edit.html', dog=dog, caretakers=caretakers)

@dog_bp.route('/dog/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    dog = Dog.query.get_or_404(id)
    db.session.delete(dog)
    db.session.commit()
    return redirect(url_for('dog.index'))

@dog_bp.route('/dogs_named_lassie', methods=['GET'])
def get_dogs_named_lassie():
    dogs = Dog.query.filter_by(name='Lassie').all()
    return render_template('dogs_named_lassie.html', dogs=dogs)

@dog_bp.route('/dog/assign_mario_to_small_dogs', methods=['POST'])
def assign_mario_to_small_dogs():
    mario = Caretaker.query.filter(Caretaker.name.like('%Mario%')).first()
    if mario:
        # Actualizar los perros pequeños para que sean asignados a Mario
        Dog.query.filter(Dog.weight < 3.0).update({'id_caretaker': mario.id})
        db.session.commit()
        # Volver a obtener la lista de perros después de la asignación
        dogs = Dog.query.filter_by(id_caretaker=mario.id).all()
        return render_template('dogs_assigned_to_mario.html', dogs=dogs, caretaker=mario)
    return "No se encontró a Mario.", 404

@dog_bp.route('/dog/dogs_assigned_to_mario', methods=['GET'])
def get_dogs_assigned_to_mario():
    mario = Caretaker.query.filter(Caretaker.name.like('%Mario%')).first()
    if mario:
        dogs = Dog.query.filter_by(id_caretaker=mario.id).all()
        return render_template('dogs_assigned_to_mario.html', dogs=dogs, caretaker=mario)
    return "No se encontró a Mario.", 404
