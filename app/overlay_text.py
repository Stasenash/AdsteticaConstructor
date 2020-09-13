import textwrap

from PIL import Image, ImageDraw, ImageFont
from colorthief import ColorThief

from app import app


class OverlayText:

    @staticmethod
    def _img_is_white(img_path):
        """Определяет доминантные цвета на картинке, возвращает какому цвету (белому, черному) более принадлежит
        изображение """

        # медленно работает, пришлось не использовать
        color_thief = ColorThief(img_path)
        r, g, b = color_thief.get_color(quality=1)
        return r >= 150 or g >= 150 or b >= 150

    @staticmethod
    def put_text_on_pic(text, img_path):
        """Записывает исходный текст на картинку"""
        size = 80
        rootPath = app.instance_path + "\\..\\app"
        font = ImageFont.truetype(rootPath + '\\static\\Montserrat.ttf', size=size)

        text_position = (50, 800)

        text_color = (255, 255, 255)
        text = textwrap.fill(text, width=20)

        img = Image.open(img_path)

        draw = ImageDraw.Draw(img)
        draw.text(text_position, text, text_color, font)

        img.save(img_path)
