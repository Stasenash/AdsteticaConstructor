import hashlib


class HashCreator:

    @staticmethod
    def get_hash(phrase):
        phrase = phrase.encode('utf-8')
        hash = hashlib.sha1(phrase).hexdigest()
        return hash
