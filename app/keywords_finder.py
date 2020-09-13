from rutermextract import TermExtractor


class KeywordsFinder:

    @staticmethod
    def get_keywords(text):
        """Получает строку, содержащую ключевые фразы переданного текста"""
        keyphrase = ''
        term_extractor = TermExtractor()
        for term in term_extractor(text):
            keyphrase += term.normalized + ' '
        return keyphrase

