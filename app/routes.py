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
    if request.method == 'POST':
        adtext = request.form.get('adtext')  # запрос к данным формы

        root_path = app.instance_path + "\\..\\app"
        image_path = root_path + "\\images\\"

        keyphrase = KeywordsFinder.get_keywords(adtext)

        if len(keyphrase) == 0:
            keyphrase = adtext

        phrase_hash = HashCreator.get_hash(keyphrase)
        image_path += phrase_hash + "\\"

        if os.path.exists(image_path):
            for c in os.listdir(image_path):
                os.remove(os.path.join(image_path, c))

        download_images(keyphrase, image_path)

        if not AdkeyphraseService.is_existing(keyphrase):
            AdkeyphraseService.record(adtext, keyphrase)

        list_files = os.listdir(image_path)[:4]

        images_list = []

        for file in list_files:
            OverlayText.put_text_on_pic(adtext, image_path + file)
            with open(image_path + file, "rb") as img_file:
                encoded = base64.b64encode(img_file.read())
                image_string = encoded.decode('utf-8')
                ext = os.path.splitext(image_path + file)[1][1:]
                images_list.append({"imageString": image_string, "ext": ext})

        return render_template('index.html', images_list=images_list)
    else:
        return render_template("index.html")
