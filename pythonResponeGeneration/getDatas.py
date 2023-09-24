from findSymptoms import FindSymptoms
import spacy
import pandas as pd

class GetData:

    fnd = FindSymptoms()
    nlp = spacy.load("en_core_web_lg")

    def __init__(self) -> None:
        self.dt = pd.read_csv("Testing.csv")
        self.dt2 = pd.read_csv("Disease_Description.csv")
        self.data = self.dt["prognosis"]
        self.target_array = []
        for i in self.data:
            self.target_array.append(i)

    def symptoms(self, sentence):
        

        # sentence = "Iam having an allergy"
        similar_word = self.find_similar_word(sentence)
        if similar_word == "none":
            return 0
        else:
            res = self.fnd.findingSymptoms(similar_word, self.dt)
            return res
        

    def description(self, sentence):

        similar_word = self.find_similar_word(sentence)
        if similar_word == "none":
            return 0
        else:
            selected_rows = self.dt2[self.dt2["Disease"] == similar_word ].iloc[0].values
            selected_rows.tolist
            # return res
            return selected_rows[1]


    def find_similar_word(self, sentence):
        sentence_tokens = self.nlp(sentence)
        sim = 0.000
        k = ""
        for target_word in self.target_array:
            target_token = self.nlp(target_word)
            similarities = [target_token.similarity(token) for token in sentence_tokens]
            
            if max(similarities) > sim:
                sim = max(similarities)
                k = target_word

            if max(similarities) > 0.8:
                return target_word
        if(sim > 0.7):
            return k
        else:
            return "none"
        
    def retrieve_min_similarity(self, sentence):
        target_token = self.nlp("call")
        sentence_tokens = self.nlp(sentence)

        min_similarity = 1.0
        least_similar_element = None

        for token in sentence_tokens:
            similarity = target_token.similarity(token)
            
            if similarity < min_similarity:
                min_similarity = similarity
                least_similar_element = token.text
        
        return least_similar_element
