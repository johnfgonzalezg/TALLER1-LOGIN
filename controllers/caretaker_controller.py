from flask import Blueprint, render_template, request, redirect, url_for
from db import db
from models.caretaker import Caretaker

caretaker_bp = Blueprint('caretaker', __name__)

@caretaker_bp.route('/', methods=['GET'], endpoint='index')
def index():
    caretakers = Caretaker.query.all()
    return render_template('caretaker/index.html', caretakers=caretakers)

@caretaker_bp.route('/caretakers', methods=['GET'])
def list_caretakers():
    caretakers = Caretaker.query.all()
    return render_template('caretaker/caretaker_list.html', caretakers=caretakers)

@caretaker_bp.route('/caretaker/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        id_nursery = request.form['id_nursery']
        caretaker = Caretaker(name=name, phone=phone, id_nursery=id_nursery)
        db.session.add(caretaker)
        db.session.commit()
        return redirect(url_for('caretaker.index'))
    return render_template('caretaker/create.html')

@caretaker_bp.route('/caretaker/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    caretaker = Caretaker.query.get_or_404(id)
    if request.method == 'POST':
        caretaker.name = request.form['name']
        caretaker.phone = request.form['phone']
        caretaker.id_nursery = request.form['id_nursery']
        db.session.commit()
        return redirect(url_for('caretaker.index'))
    return render_template('caretaker/edit.html', caretaker=caretaker)

@caretaker_bp.route('/caretaker/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    caretaker = Caretaker.query.get_or_404(id)
    db.session.delete(caretaker)
    db.session.commit()
    return redirect(url_for('caretaker.index'))
