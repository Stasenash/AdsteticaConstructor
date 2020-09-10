from flask import render_template, request
from app import app

@app.route('/', methods=['post', 'get'])
@app.route('/index', methods=['post', 'get'])
def index():
    adtext = ''
    if request.method == 'POST':
        adtext = request.form.get('adtext')  # запрос к данным формы
    return render_template('index.html')
