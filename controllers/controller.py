from flask import Blueprint, render_template, redirect, url_for
from db import db
from models.nursery import Nursery
from models.caretaker import Caretaker
from models.dog import Dog


dog_bp = Blueprint('dog', __name__)




nursery_bp = Blueprint('nursery', __name__)


