from flask import Blueprint, render_template, request, redirect, url_for
from db import db
from models.nursery import Nursery
from models.caretaker import Caretaker
from models.dog import Dog

nursery_bp = Blueprint('nursery', __name__)

@nursery_bp.route('/', methods=['GET'], endpoint='index')
def index():
    nurseries = Nursery.query.all()
    return render_template('nursery/index.html', nurseries=nurseries)

@nursery_bp.route('/create', methods=['GET', 'POST'], endpoint='create')
def create():
    if request.method == 'POST':
        name = request.form['name']
        direction = request.form['direction']
        phone = request.form['phone']
        nursery = Nursery(name=name, direction=direction, phone=phone)
        db.session.add(nursery)
        db.session.commit()
        return redirect(url_for('nursery.index'))
    return render_template('nursery/create.html')

@nursery_bp.route('/edit/<int:id>', methods=['GET', 'POST'], endpoint='edit')
def edit(id):
    nursery = Nursery.query.get_or_404(id)
    if request.method == 'POST':
        nursery.name = request.form['name']
        nursery.direction = request.form['direction']
        nursery.phone = request.form['phone']
        db.session.commit()
        return redirect(url_for('nursery.index'))
    return render_template('nursery/edit.html', nursery=nursery)

@nursery_bp.route('/delete/<int:id>', methods=['POST'], endpoint='delete')
def delete(id):
    nursery = Nursery.query.get_or_404(id)
    db.session.delete(nursery)
    db.session.commit()
    return redirect(url_for('nursery.index'))


@nursery_bp.route('/nursery/la_favorita', methods=['GET'])
def get_la_favorita_details():
    nursery = Nursery.query.filter_by(name='La Favorita').first()
    if nursery:
        caretakers = Caretaker.query.filter_by(id_nursery=nursery.id).all()
        dogs = Dog.query.filter_by(id_nursery=nursery.id).all()
        return render_template('la_favorita_details.html', nursery=nursery, caretakers=caretakers, dogs=dogs)
    else:
        return "No se encontró la guardería 'La Favorita'.", 404