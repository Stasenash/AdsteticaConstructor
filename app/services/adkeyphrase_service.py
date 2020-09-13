from app import mysql
from app.hash_creator import HashCreator


class AdkeyphraseService:
    """Класс, записывающий и получающий информацию посредством базы данных"""

    @staticmethod
    def record(text, phrase):
        """Делает запись текста и ключевой фразы в базу по хешу ключевой фразы"""

        conn = mysql.connect()
        cursor = conn.cursor()
        hash = HashCreator.get_hash(phrase)
        sql = "INSERT INTO adkeyphrase(hash, ad_text, ad_keyphrase) VALUES(%s, %s, %s)"
        data = (hash, text, phrase)
        cursor.execute(sql, data)
        data = cursor.fetchall()

        if len(data) == 0:
            conn.commit()

    @staticmethod
    def is_existing(phrase):
        """Проверяет существование записи в базе по хэшу"""

        conn = mysql.connect()
        cursor = conn.cursor()
        sql = "SELECT * FROM adkeyphrase WHERE hash = %s"
        hash = HashCreator.get_hash(phrase)
        cursor.execute(sql, hash)
        data = cursor.fetchone()
        return data is not None

