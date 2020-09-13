import hashlib


class HashCreator:

    @staticmethod
    def get_hash(phrase):
        """Получает шестнадцатиричный хэш для фразы"""

        phrase = phrase.encode('utf-8')
        hash = hashlib.sha1(phrase).hexdigest()
        return hash
