import os

from flask import render_template, request
from app import app
from app.keywords_finder import KeywordsFinder
from app.overlay_text import OverlayText


@app.route('/', methods=['post', 'get'])
@app.route('/index', methods=['post', 'get'])
def index():
    adtext = ''
    if request.method == 'POST':
        adtext = request.form.get('adtext')  # запрос к данным формы
        keyphrase = ' '.join(KeywordsFinder.get_keywords(adtext))
        # TODO скачиваем картинки по ключ. словам
        path = "images/"
        list_files = os.listdir(path)
        images_list = []
        for file in list_files:
            OverlayText.put_text_on_pic(adtext, path + '/' + file)
            images_list.append(path + '/' + file)
        return render_template('index.html', images_list)
    else:
        return render_template("index.html")
