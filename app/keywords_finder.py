from rutermextract import TermExtractor


class KeywordsFinder:

    @staticmethod
    def get_keywords(text):
        keyphrase = ''
        term_extractor = TermExtractor()
        for term in term_extractor(text):
            keyphrase += term.normalized + ' '
        return keyphrase

