from flask import Blueprint, render_template, request, flash, jsonify, url_for
from flask_login import login_required, current_user
from .models import Note
from . import db
import json

cat = Blueprint('cat', __name__)


@cat.route('/catalog')
@login_required
def krasiviy_catalog():
    return render_template("catalog.html", user=current_user, path=url_for('static', filename='a.jpg'), css_path=url_for('static', filename='catalog.css'))
