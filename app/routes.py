import base64
import os

from flask import render_template, request
from app import app
from app.hash_creator import HashCreator
from app.keywords_finder import KeywordsFinder
from app.overlay_text import OverlayText
from app.services.adkeyphrase_service import AdkeyphraseService
from app.yandex_images_finder import download_images


@app.route('/', methods=['post', 'get'])
@app.route('/index', methods=['post', 'get'])
def index():
    adtext = ''
    if request.method == 'POST':
        adtext = request.form.get('adtext')  # запрос к данным формы

        rootPath = app.instance_path + "\\..\\app"
        imagePath = rootPath + "\\images\\"


        keyphrase = KeywordsFinder.get_keywords(adtext)

        if len(keyphrase) == 0:
            keyphrase = adtext

        hash = HashCreator.get_hash(keyphrase)
        imagePath += hash + "\\"

        for c in os.listdir(imagePath):
            os.remove(os.path.join(imagePath, c))

        download_images(keyphrase, imagePath)

        if not AdkeyphraseService.is_existing(keyphrase):
            AdkeyphraseService.record(adtext, keyphrase)

        list_files = os.listdir(imagePath)[:4]

        images_list = []

        for file in list_files:
            OverlayText.put_text_on_pic(adtext, imagePath + file)
            with open(imagePath + file, "rb") as img_file:
                encoded = base64.b64encode(img_file.read())
                imageString = encoded.decode('utf-8')
                ext = os.path.splitext(imagePath + file)[1][1:]
                images_list.append({"imageString": imageString, "ext": ext})

        return render_template('index.html', images_list=images_list)
    else:
        return render_template("index.html")
