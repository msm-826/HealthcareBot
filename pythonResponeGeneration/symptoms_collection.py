from spacy.matcher import Matcher
from addMatchers import AddMatchers

class Collections:

    def __init__(self, nlp) -> None:
        addmatcher = AddMatchers()
        self.nlp = nlp
        self.matcher = Matcher(self.nlp.vocab)
        self.matcher = addmatcher.addIn(self.matcher)

    def getCollections(self, query):
        doc = self.nlp(query)
        matches = self.matcher(doc)
        k = []
        for match_id, start, end in matches:
            k.append(self.nlp.vocab.strings[match_id])

        return k


