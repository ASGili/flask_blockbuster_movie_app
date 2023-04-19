from app import app

from flask import render_template
from models.orders import orders

@app.route('/')
def index():
    return render_template('index.jinja', orders_list = orders)
