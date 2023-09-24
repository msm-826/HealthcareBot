from operationFinder import OperationFinder
import spacy
# from symptoms_collection import Collections
# from algorithms import Algorithms
# from findSymptoms import FindSymptoms
from getDatas import GetData
from gpt import GetGPT
from outData import DataOut


class Main:

    gpt = GetGPT()
    getdt = GetData()

    dt2 = DataOut()

    def __init__(self) -> None:
        self.nlp = spacy.load('en_core_web_lg')
        self.str2 = ""
        self.resu = "none"
        self.symptom = []
        self.lastQuery = ""
        self.nw = ""


    def main(self, str1):
        self.str1 = str1
        # str1 = input("Enter the Message : ")
        
        operation = OperationFinder(self.nlp)
        res1 = operation.opertationalfinder(str1)
        # print(res1)
        if res1 == "symptom":
            m.symptomsCalled(str1)
        elif res1 == "contact":
            m.contactCalled(str1)
        elif res1 == "queries":
            m.queriesCalled(self.nlp)
        elif res1 == "help":
            m.helpCalled()
        elif res1 == "positive":
            m.positiveCalled()
        elif res1 == "negative":
            m.negativeCalled()
        elif res1 == "greetings":
            m.greetingsCalled()
        elif res1 == "disease":
            self.nw = "disease"
            print(self.nw)
            m.diseaseCalled(str1)
        elif res1 == "descript":
            self.nw = "descript"
            m.descriptCalled(str1)
        elif res1 == "more":
            m.moreCalled()
        else:
            self.resu = "Sorry Nothing Obtained."

        return m.resu



    def symptomsCalled(self, st):
        k = self.gpt.getResult(st + ", Can you tell me the disease from the symptoms?")
        self.resu = k
        # cl = Collections(nlp)
        # h = cl.getCollections(st)
        # h=h+self.symptom
        # if(len(h) > 2):
        #     resultDisease = m.resultComparing(h)
        #     # print(h)
        #     # print("\nIt may be "+resultDisease)
        #     self.symptom = []
        #     self.resu = "There are many chances. It may be "+resultDisease
        
        # elif(len(h) == 0):
        #     # print("Please enter symptoms.")
        #     self.resu = "Please enter symptoms."

        # else:
        #     self.str2 = "symptomscalled"
        #     self.symptom = self.symptom+h
        #     # print("Do you have any other symptoms?")
        #     self.resu = "Do you have any other symptoms?"

    def contactCalled(self, str1):
        self.str2 = "contactcalled"
        cntct = self.getdt.retrieve_min_similarity(str1)
        # print("CALLING DOCTOR...........")
        self.resu = "contactxyz"+cntct

    def queriesCalled(self, nlp):
        # print("Oh! May I call the doctor?")
        self.resu = self.dt2.getMayCall()
        self.str2 = "querycalled1"

    def helpCalled(self):
        self.str2 = "helpcalled"
        # print("How may I help you sir?")
        self.resu = self.dt2.getHowHelp()


    # def resultComparing(self, symptoms):
    #     alg = Algorithms()
    #     disease = ["", "", ""]
    #     disease[0] = alg.DecisionTree(symptoms) 
    #     disease[1] = alg.randomforest(symptoms)
    #     disease[2] = alg.NaiveBayes(symptoms)
    #     # print("\n")
    #     print(disease)

    #     if disease.count(disease[0]) > 1:
    #         return disease[0]
    #     else:
    #         return disease[1]
        
    def askSymptoms(self):
        # print("your symptooms : ")
        self.resu = "Please provide your symptoms"

    def positiveCalled(self):
        if self.str2 == "symptomscalled":
            # print("Please describe those.")
            self.resu = "Please describe those."

        elif self.str2 == "contactcalled":
            pass

        elif self.str2 =="querycalled1":
            m.contactCalled()
            
        elif self.str2 =="querycalled2":
            # print("Enter your symptoms:")
            self.resu = "Enter your symptoms:"

        elif self.str2 =="helpcalled":
            pass

        else:
            # print("I don't get it")
            self.resu = self.dt2.getMore()
        

    def negativeCalled(self):
        if self.str2 == "symptomscalled":
            # print("Showing remedies!!")
            self.resu = "Showing remedies!!"

        elif self.str2 == "contactcalled":
            pass

        elif self.str2 =="querycalled1":
            # print("OK Do you want to check for the disease with your symptoms")
            self.resu = "OK Do you want to check for the disease with your symptoms"

        elif self.str2 =="querycalled2":
            # print("OK. Let me know if anything required.")
            self.resu = "OK. Let me know if anything required."

        elif self.str2 =="helpcalled":
            pass

        else:
            # print("I don't get it")
            self.resu = self.dt2.getMore()

    def greetingsCalled(self):
        # print("I don't get it")
        self.resu = self.dt2.getGreetings()

    def diseaseCalled(self, str):
        dcs = self.getdt.symptoms(str)
        self.nw = "disease"
        
        self.lastQuery = self.getdt.find_similar_word(str)

        if dcs == 0:
            k = self.gpt.getResult(str + ", Can you list its symptoms")
            self.resu = k
        else:
            res = "The common Symptoms are "
            for j in range(len(dcs)-1):
                k = dcs[j].replace("_", " ")
                res+=k+", "
            last = dcs[len(dcs)-1].replace("_", " ")
            res+= "and " + last
            self.resu = res

    def descriptCalled(self, str1):
        dscrpt = self.getdt.description(str1)
        self.nw = "descript"
        self.lastQuery = self.getdt.find_similar_word(str1)
        if dscrpt == 0:
            k = self.gpt.getResult(str1 + ", Can you describe the disease")
            self.resu = k
        else:
            self.resu = dscrpt

    def moreCalled(self):

        # print(self.nw)
        if self.lastQuery == "none":
            k = self.gpt.getResult("State more about "+self.lastQuery)
            self.resu = k

        else:
            if self.nw == "disease":
                k = self.gpt.getResult("What are the symptoms of "+self.lastQuery)
                self.resu = k
            elif self.nw == "descript":
                print(self.lastQuery)
                k = self.gpt.getResult("Describe more about "+self.lastQuery)
                self.resu = k
            else:
                self.resu = self.dt2.getMore
        

        

m = Main()
