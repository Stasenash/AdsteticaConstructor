from PIL import Image, ImageDraw, ImageFont
import textwrap
import os
from colorthief import ColorThief

from app import app


class OverlayText:

    @staticmethod
    def _img_is_white(img_path):
        color_thief = ColorThief(img_path)
        r, g, b = color_thief.get_color(quality=1)
        return r >= 150 or g >= 150 or b >= 150

    @staticmethod
    def put_text_on_pic(text, img_path):
        # TODO разные размеры текста в зависимости от кол-ва слов

        size = 80
        rootPath = app.instance_path + "\\..\\app"
        font = ImageFont.truetype(rootPath + '\\static\\Montserrat.ttf', size=size)

        # определяете положение текста на картинке
        text_position = (40, 640)

        # цвет текста, RGB
        text_color = (255, 255, 255)
        # if OverlayText._img_is_white(img_path):
        #     text_color = (0, 0, 0)

        # собственно, сам текст
        text = textwrap.fill(text, width=20)

        # загружаете фоновое изображение
        img = Image.open(img_path)

        # определяете объект для рисования
        draw = ImageDraw.Draw(img)

        # добавляем текст
        draw.text(text_position, text, text_color, font)

        # сохраняем новое изображение
        img.save(img_path)
