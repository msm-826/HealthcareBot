from sklearn import tree
import pandas as pd
import numpy as np
from datas import Datas
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier


class Algorithms:

    dtas = Datas()

    def __init__(self) -> None:

# ---------------------------------------------SET DATA--------------------------------------------------

        self.l1 = self.dtas.get_l1()
        self.l2 = self.dtas.get_l2()
        self.disease = self.dtas.get_disease()

        df=pd.read_csv("Training.csv")

        df.replace({'prognosis':{'Fungal infection':0,'Allergy':1,'GERD':2,'Chronic cholestasis':3,'Drug Reaction':4,
        'Peptic ulcer diseae':5,'AIDS':6,'Diabetes ':7,'Gastroenteritis':8,'Bronchial Asthma':9,'Hypertension ':10,
        'Migraine':11,'Cervical spondylosis':12,
        'Paralysis (brain hemorrhage)':13,'Jaundice':14,'Malaria':15,'Chicken pox':16,'Dengue':17,'Typhoid':18,'hepatitis A':19,
        'Hepatitis B':20,'Hepatitis C':21,'Hepatitis D':22,'Hepatitis E':23,'Alcoholic hepatitis':24,'Tuberculosis':25,
        'Common Cold':26,'Pneumonia':27,'Dimorphic hemmorhoids(piles)':28,'Heart attack':29,'Varicose veins':30,'Hypothyroidism':31,
        'Hyperthyroidism':32,'Hypoglycemia':33,'Osteoarthristis':34,'Arthritis':35,
        '(vertigo) Paroymsal  Positional Vertigo':36,'Acne':37,'Urinary tract infection':38,'Psoriasis':39,
        'Impetigo':40}},inplace=True)

        self.X= df[self.l1]

        self.y = df[["prognosis"]]
        np.ravel(self.y)

        tr=pd.read_csv("Testing.csv")
        tr.replace({'prognosis':{'Fungal infection':0,'Allergy':1,'GERD':2,'Chronic cholestasis':3,'Drug Reaction':4,
        'Peptic ulcer diseae':5,'AIDS':6,'Diabetes ':7,'Gastroenteritis':8,'Bronchial Asthma':9,'Hypertension ':10,
        'Migraine':11,'Cervical spondylosis':12,
        'Paralysis (brain hemorrhage)':13,'Jaundice':14,'Malaria':15,'Chicken pox':16,'Dengue':17,'Typhoid':18,'hepatitis A':19,
        'Hepatitis B':20,'Hepatitis C':21,'Hepatitis D':22,'Hepatitis E':23,'Alcoholic hepatitis':24,'Tuberculosis':25,
        'Common Cold':26,'Pneumonia':27,'Dimorphic hemmorhoids(piles)':28,'Heart attack':29,'Varicose veins':30,'Hypothyroidism':31,
        'Hyperthyroidism':32,'Hypoglycemia':33,'Osteoarthristis':34,'Arthritis':35,
        '(vertigo) Paroymsal  Positional Vertigo':36,'Acne':37,'Urinary tract infection':38,'Psoriasis':39,
        'Impetigo':40}},inplace=True)

        self.X_test= tr[self.l1]
        self.y_test = tr[["prognosis"]]
        np.ravel(self.y_test)
    
    # ---------------------------------------------------------------------------------------
    
    
    # --------------------------------------DECISION TREE---------------------------------
    
    def DecisionTree(self, psymptoms):


        clf3 = tree.DecisionTreeClassifier()   # empty model of the decision tree
        clf3 = clf3.fit(self.X,self.y)

        # y_pred=clf3.predict(self.X_test)
        # print(accuracy_score(self.y_test, y_pred))
        # print(accuracy_score(self.y_test, y_pred,normalize=False))

        for k in range(0,len(self.l1)):
            # print (k)
            for z in psymptoms:
                if(z==self.l1[k]):
                    self.l2[k]=1

        print(self.l2)

        inputtest = [self.l2]
        predict = clf3.predict(inputtest)
        predicted=predict[0]

        h='no'
        for a in range(0,len(self.disease)):
            if(predicted == a):
                h='yes'
                break


        if (h=='yes'):
            return self.disease[a]
        else:
            return "0"

# --------------------------------------------------------------------------------------------


# ---------------------------------------------RANDOM FOREST-------------------------------------

    def randomforest(self, psymptoms):
        clf4 = RandomForestClassifier()
        clf4 = clf4.fit(self.X,np.ravel(self.y))

        # y_pred=clf4.predict(self.X_test)
        # print(accuracy_score(self.y_test, y_pred))
        # print(accuracy_score(self.y_test, y_pred,normalize=False))

        for k in range(0,len(self.l1)):
            for z in psymptoms:
                if(z==self.l1[k]):
                    self.l2[k]=1

        inputtest = [self.l2]
        predict = clf4.predict(inputtest)
        predicted=predict[0]
        # print(predict)

        h='no'
        for a in range(0,len(self.disease)):
            if(predicted == a):
                h='yes'
                break

        if (h=='yes'):
            return self.disease[a]
        else:
            return "0"

# -------------------------------------------------------------------------------------


# -------------------------------------NAIVE BAYES-------------------------------------------

    def NaiveBayes(self, psymptoms):
        from sklearn.naive_bayes import GaussianNB
        gnb = GaussianNB()
        gnb=gnb.fit(self.X,np.ravel(self.y))

        # from sklearn.metrics import accuracy_score
        # y_pred=gnb.predict(self.X_test)
        # print(accuracy_score(self.y_test, y_pred))
        # print(accuracy_score(self.y_test, y_pred,normalize=False))

        for k in range(0,len(self.l1)):
            for z in psymptoms:
                if(z==self.l1[k]):
                    self.l2[k]=1
        

        inputtest = [self.l2]
        # print(inputtest)

        predict_proba = gnb.predict_proba(inputtest)
        print(predict_proba)
        threshold = 0

        for i, probabilities in enumerate(predict_proba):
            print(f"Sample {i+1}: {probabilities}")

        # predicted_items = [class_idx for class_idx, class_prob in enumerate(predict_proba) if class_prob.max() != threshold]

        # print(predicted_items)


        predict = gnb.predict(inputtest)
        predicted=predict[0]

        h='no'
        for a in range(0,len(self.disease)):
            if(predicted == a):
                print(self.disease[a])
                h='yes'
                break

        # if (h=='yes'):
        #     # return self.disease[a]
        #     print(self.disease[a])
        # else:
        #     return "0"


# -----------------------------------------------------------------------------------------------
