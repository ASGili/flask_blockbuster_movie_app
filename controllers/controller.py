from app import app

from flask import render_template
from models.orders import orders

@app.route('/orders')
def index():
    return render_template('index.html', orders_list = orders)

@app.route('/orders/<index>')
def order_ind(index):
    i = int(index) 
    return render_template('order.html', order=orders[i],index=i)