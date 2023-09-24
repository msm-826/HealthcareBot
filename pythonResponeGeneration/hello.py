# x = input("Enter here : ")


# ---------------------------------------------------------------------------


# h=0
# for k in range(len(x)):
#     if h==1:
#         h=0
#         continue
#     if x[k] == ',':
#         x = x[:k]+'\''+x[k]+'\''+x[k+1:]
#         h=1
        
# print(x)

# ------------------------------------------------------------------------------


# while 1:
#     if '_' in x:
#         x = x.replace('_', ' ')
#     else:
#         break

# print(x)


# -----------------------------------------------------------------------------------

# # x = input("Here : ")
# # k = x.split(',')
# # print(k)

# k = ['Fungal infection','Allergy','GERD','Chronic cholestasis','Drug Reaction',
#         'Peptic ulcer diseae','AIDS','Diabetes ','Gastroenteritis','Bronchial Asthma','Hypertension',
#         'Migraine','Cervical spondylosis',
#         'Paralysis (brain hemorrhage)','Jaundice','Malaria','Chicken pox','Dengue','Typhoid','hepatitis A',
#         'Hepatitis B','Hepatitis C','Hepatitis D','Hepatitis E','Alcoholic hepatitis','Tuberculosis',
#         'Common Cold','Pneumonia','piles','Heart attack','Varicose veins','Hypothyroidism',
#         'Hyperthyroidism','Hypoglycemia','Osteoarthristis','Arthritis',
#         'Vertigo','Acne','Urinary tract infection','Psoriasis',
#         'Impetigo']
# l=[]

# for j in k:
#     l.append('What is '+j)
#     l.append('Describe '+j)
#     l.append('Define '+j)
#     l.append('Can you tell me what is '+j)

# print(l)







# ----------------------------------------------------------------------------------------



# import spacy
# from spacy.matcher import Matcher
# nlp = spacy.load("en_core_web_md")
# matcher = Matcher(nlp.vocab)
# # Add match ID "HelloWorld" with no callback and one pattern
# pattern = [{"LOWER": "hello"}, {"IS_PUNCT": True}, {"LOWER": "world"}]
# pattern1 = [{"LOWER": "hello"}, {"LOWER": "world"}]
# matcher.add("HelloWorld", [pattern1])

# doc = nlp("Hello, world! Hello world!")
# matches = matcher(doc)
# for match_id, start, end in matches:
#     string_id = nlp.vocab.strings[match_id]  # Get string representation
#     span = doc[start:end]  # The matched span
#     print(match_id, string_id, start, end, span.text)







# -----------------------------------------------------------------------------------------
# while 1:
#     x = input("HERE :")
#     k = x+ "1 = [{\"LOWER\" : \""+x+"\"}]"
#     print(k)

# ----------------------------------------------------------------------------------------------

# s=1
# while 1:
#     key = input("KEY : ")
#     key = key.replace('_', '')
#     k = []
#     while 1:
#         inp = input("INPUT : ")
#         inp = inp.replace('_', ' ')
#         if inp == '1':
#             s=1
#             break
#         inplist = inp.split(' ')
#         res = key+f"{s}"+" = ["
#         s+=1
#         for i in inplist:
#             res+= "{\"LOWER\" : \""+i+"\"}, "

#         res += "\b\b]"
#         k.append(res)
#     for j in k:
#         print(j)



# ----------------------------------------------------------------------------------------------

# 'itching','skin rash','nodal skin eruptions','continuous sneezing','shivering','chills','joint pain','stomach pain','acidity','ulcers on tongue','muscle wasting','vomiting','burning micturition','spotting  urination','fatigue','weight gain','anxiety','cold hands and feets','mood swings','weight loss','restlessness','lethargy','patches in throat','irregular sugar level','cough','high fever','sunken eyes','breathlessness','sweating','dehydration','indigestion','headache','yellowish skin','dark urine','nausea','loss of appetite','pain behind the eyes','back pain','constipation','abdominal pain','diarrhoea','mild fever','yellow urine','yellowing of eyes','acute liver failure','fluid overload','swelling of stomach','swelled lymph nodes','malaise','blurred and distorted vision','phlegm','throat irritation','redness of eyes','sinus pressure','runny nose','congestion','chest pain','weakness in limbs','fast heart rate','pain during bowel movements','pain in anal region','bloody stool','irritation in anus','neck pain','dizziness','cramps','bruising','obesity','swollen legs','swollen blood vessels','puffy face and eyes','enlarged thyroid','brittle nails','swollen extremeties','excessive hunger','extra marital contacts','drying and tingling lips','slurred speech','knee pain','hip joint pain','muscle weakness','stiff neck','swelling joints','movement stiffness','spinning movements','loss of balance','unsteadiness','weakness of one body side','loss of smell','bladder discomfort','foul smell of urine','continuous feel of urine','passage of gases','internal itching','toxic look (typhos)','depression','irritability','muscle pain','altered sensorium','red spots over body','belly pain','abnormal menstruation','dischromic  patches','watering from eyes','increased appetite','polyuria','family history','mucoid sputum','rusty sputum','lack of concentration','visual disturbances','receiving blood transfusion','receiving unsterile injections','coma','stomach bleeding','distention of abdomen','history of alcohol consumption','fluid overload','blood in sputum','prominent veins on calf','palpitations','painful walking','pus filled pimples','blackheads','scurring','skin peeling','silver like dusting','small dents in nails','inflammatory nails,blister','red sore around nose','yellow crust ooze','prognosis'

# itching,skin rash,nodal skin eruptions,continuous sneezing,shivering,chills,joint pain,stomach pain,acidity,ulcers on tongue,muscle wasting,vomiting,burning micturition,spotting  urination,fatigue,weight gain,anxiety,cold hands and feets,mood swings,weight loss,restlessness,lethargy,patches in throat,irregular sugar level,cough,high fever,sunken eyes,breathlessness,sweating,dehydration,indigestion,headache,yellowish skin,dark urine,nausea,loss of appetite,pain behind the eyes,back pain,constipation,abdominal pain,diarrhoea,mild fever,yellow urine,yellowing of eyes,acute liver failure,fluid overload,swelling of stomach,swelled lymph nodes,malaise,blurred and distorted vision,phlegm,throat irritation,redness of eyes,sinus pressure,runny nose,congestion,chest pain,weakness in limbs,fast heart rate,pain during bowel movements,pain in anal region,bloody stool,irritation in anus,neck pain,dizziness,cramps,bruising,obesity,swollen legs,swollen blood vessels,puffy face and eyes,enlarged thyroid,brittle nails,swollen extremeties,excessive hunger,extra marital contacts,drying and tingling lips,slurred speech,knee pain,hip joint pain,muscle weakness,stiff neck,swelling joints,movement stiffness,spinning movements,loss of balance,unsteadiness,weakness of one body side,loss of smell,bladder discomfort,foul smell of urine,continuous feel of urine,passage of gases,internal itching,toxic look (typhos),depression,irritability,muscle pain,altered sensorium,red spots over body,belly pain,abnormal menstruation,dischromic  patches,watering from eyes,increased appetite,polyuria,family history,mucoid sputum,rusty sputum,lack of concentration,visual disturbances,receiving blood transfusion,receiving unsterile injections,coma,stomach bleeding,distention of abdomen,history of alcohol consumption,fluid overload,blood in sputum,prominent veins on calf,palpitations,painful walking,pus filled pimples,blackheads,scurring,skin peeling,silver like dusting,small dents in nails,inflammatory nails,blister,red sore around nose,yellow crust ooze,prognosis


# symptoms_x = ['itching','skin rash','nodal skin eruptions','continuous sneezing','shivering','chills','joint pain','stomach pain','acidity','ulcers on tongue','muscle wasting','vomiting','burning micturition','spotting  urination','fatigue','weight gain','anxiety','cold hands and feets','mood swings','weight loss','restlessness','lethargy','patches in throat','irregular sugar level','cough','high fever','sunken eyes','breathlessness','sweating','dehydration','indigestion','headache','yellowish skin','dark urine','nausea','loss of appetite','pain behind the eyes','back pain','constipation','abdominal pain','diarrhoea','mild fever','yellow urine','yellowing of eyes','acute liver failure','fluid overload','swelling of stomach','swelled lymph nodes','malaise','blurred and distorted vision','phlegm','throat irritation','redness of eyes','sinus pressure','runny nose','congestion','chest pain','weakness in limbs','fast heart rate','pain during bowel movements','pain in anal region','bloody stool','irritation in anus','neck pain','dizziness','cramps','bruising','obesity','swollen legs','swollen blood vessels','puffy face and eyes','enlarged thyroid','brittle nails','swollen extremeties','excessive hunger','extra marital contacts','drying and tingling lips','slurred speech','knee pain','hip joint pain','muscle weakness','stiff neck','swelling joints','movement stiffness','spinning movements','loss of balance','unsteadiness','weakness of one body side','loss of smell','bladder discomfort','foul smell of urine','continuous feel of urine','passage of gases','internal itching','toxic look (typhos)','depression','irritability','muscle pain','altered sensorium','red spots over body','belly pain','abnormal menstruation','dischromic  patches','watering from eyes','increased appetite','polyuria','family history','mucoid sputum','rusty sputum','lack of concentration','visual disturbances','receiving blood transfusion','receiving unsterile injections','coma','stomach bleeding','distention of abdomen','history of alcohol consumption','fluid overload','blood in sputum','prominent veins on calf','palpitations','painful walking','pus filled pimples','blackheads','scurring','skin peeling','silver like dusting','small dents in nails','inflammatory nails,blister','red sore around nose','yellow crust ooze','prognosis']





# -----------------------------------------------------------------------------------------------------------

# from algorithms import Algorithms

# al = Algorithms()
# st = ["abdominal_pain", "fatigue", "dark_urine"]
# dct = al.DecisionTree(st)
# ncb = al.NaiveBayes(st)
# rndfrst = al.randomforest(st)

# print(dct, ncb, rndfrst)


# -----------------------------------------------------------------------------------------------------------
# import spacy
# from spacy.matcher import Matcher
# from symptoms_extraction import Symptoms as sv
# from addMatchers import AddMatchers

# nlp = spacy.load("en_core_web_lg")
# doc = nlp("Upcoming iPhone X release date leaked as Apple reveals pre-orders")

# matcher = Matcher(nlp.vocab)

# adm = AddMatchers()

# x = adm.addIn(matcher)

# matches = x(doc)
# for match_id, strat, end in matches:    
#     print("Matches:", nlp.vocab.strings[match_id])


# -----------------------------------------------------------------------------------------------------------------

# str = input("KEY : ")
# knw = str.split(',')

# k=[]

# for x in knw:
#     strcpy = x.replace('_', '')
#     print(x)
#     no = int(input("NUMBER : "))
#     for i in range(no):
#         str2 = "matcher.add(\'"+x+"\', [sv."+strcpy+f"{i+1}"+"])"
#         k.append(str2)

# for j in k:
#     print(j)



# no = int(input("NUMBER : "))
# strcpy = str.replace('_', '')
# k=[]
# for i in range(no):
#     str2 = "matcher.add(\'"+str+"\', ["+strcpy+f"{i+1}"+"])"
#     k.append(str2)
# for j in k:
#     print(k[0])


# ------------------------------------------------------------------------------------------------------------------

# itching,skin_rash,nodal_skin_eruptions,continuous_sneezing,shivering,chills,joint_pain,stomach_pain,acidity,ulcers_on_tongue,muscle_wasting,vomiting,burning_micturition,spotting_ urination,fatigue,weight_gain,anxiety,cold_hands_and_feets,mood_swings,weight_loss,restlessness,lethargy,patches_in_throat,irregular_sugar_level,cough,high_fever,sunken_eyes,breathlessness,sweating,dehydration,indigestion,headache,yellowish_skin,dark_urine,nausea,loss_of_appetite,pain_behind_the_eyes,back_pain,constipation,abdominal_pain,diarrhoea,mild_fever,yellow_urine,yellowing_of_eyes,acute_liver_failure,fluid_overload,swelling_of_stomach,swelled_lymph_nodes,malaise,blurred_and_distorted_vision,phlegm,throat_irritation,redness_of_eyes,sinus_pressure,runny_nose,congestion,chest_pain,weakness_in_limbs,fast_heart_rate,pain_during_bowel_movements,pain_in_anal_region,bloody_stool,irritation_in_anus,neck_pain,dizziness,cramps,bruising,obesity,swollen_legs,swollen_blood_vessels,puffy_face_and_eyes,enlarged_thyroid,brittle_nails,swollen_extremeties,excessive_hunger,extra_marital_contacts,drying_and_tingling_lips,slurred_speech,knee_pain,hip_joint_pain,muscle_weakness,stiff_neck,swelling_joints,movement_stiffness,spinning_movements,loss_of_balance,unsteadiness,weakness_of_one_body_side,loss_of_smell,bladder_discomfort,foul_smell_of urine,continuous_feel_of_urine,passage_of_gases,internal_itching,toxic_look_(typhos),depression,irritability,muscle_pain,altered_sensorium,red_spots_over_body,belly_pain,abnormal_menstruation,dischromic _patches,watering_from_eyes,increased_appetite,polyuria,family_history,mucoid_sputum,rusty_sputum,lack_of_concentration,visual_disturbances,receiving_blood_transfusion,receiving_unsterile_injections,coma,stomach_bleeding,distention_of_abdomen,history_of_alcohol_consumption,fluid_overload,blood_in_sputum,prominent_veins_on_calf,palpitations,painful_walking,pus_filled_pimples,blackheads,scurring,skin_peeling,silver_like_dusting,small_dents_in_nails,inflammatory_nails,blister,red_sore_around_nose,yellow_crust_ooze,prognosis

# -------------------------------------------------------------------------------------------------------------------

# import spacy
# from symptoms_collection import Collections

# nlp = spacy.load("en_core_web_lg")

# cl = Collections(nlp)
# cl.getCollections("Iam having a headache")

# -------------------------------------------------------------------------------------------
# from posNeg import ExpFinder
# import spacy


# nlp = spacy.load("en_core_web_lg")
# exp = ExpFinder(nlp)

# print(exp.expFind("That car is red"))

# ---------------------------------------------------------------------------------

# class Hello:

#     def hellCaller(self, str):
#         print(str)

# -------------------------------------------------------==============================================----------------------------------------------
from main import Main

m = Main()
while 1:
    k = m.main(input("Enter the string :"))
    print(k)

# -------------------------------------------------=================================----------------------------------------------------------------=====

# k = input("Enter here : ")

# z = k.split(',')
# print(z)
# print(len(z))

# ------------------------------------------------------------------------------------------

# n = ['Fungal infection','Allergy','GERD','Chronic cholestasis','Drug Reaction',
#                 'Peptic ulcer diseae','AIDS','Diabetes','Gastroenteritis','Bronchial Asthma','Hypertension',
#                 ' Migraine','Cervical spondylosis',
#                 'Paralysis (brain hemorrhage)','Jaundice','Malaria','Chicken pox','Dengue','Typhoid','hepatitis A',
#         'Hepatitis B','Hepatitis C','Hepatitis D','Hepatitis E','Alcoholic hepatitis','Tuberculosis',
#         'Common Cold','Pneumonia','Dimorphic hemmorhoids(piles)',
#         'Heartattack','Varicoseveins','Hypothyroidism','Hyperthyroidism','Hypoglycemia','Osteoarthristis',
#         'Arthritis','(vertigo) Paroymsal  Positional Vertigo','Acne','Urinary tract infection','Psoriasis',
#         'Impetigo']

# x = []

# for i in n:
#     x.append('What are the symptoms of '+i)
#     x.append('Show me the symptoms of '+i)
#     x.append('Can you tell me the symptoms of '+i)

# print(x)


# ------------------------------------------------------------------------------------------

# from algorithms import Algorithms

# a = Algorithms()

# a.NaiveBayes(["chills", "headache", "high_fever", "itching"])

# -------------------------------------------------------------------------------------

# from findSymptoms import FindSymptoms

# find = FindSymptoms()

# x = ['fungal infection', 'allergy', 'gerd', 'chronic cholestasis', 'drug reaction', 'peptic ulcer diseae', 'aids', 'diabetes', 'gastroenteritis', 'bronchial asthma', 'hypertension', 'migraine', 'cervical spondylosis', 'paralysis', 'jaundice', 'malaria', 'chicken pox', 'dengue', 'typhoid', 'hepatitis a', 'hepatitis b', 'hepatitis c', 'hepatitis d', 'hepatitis e', 'alcoholic hepatitis', 'tuberculosis', 'common cold', 'pneumonia', 'piles', 'heart attack', 'varicose veins', 'hypothyroidism', 'hyperthyroidism', 'hypoglycemia', 'osteoarthristis', 'arthritis', 'vertigo', 'acne', 'urinary tract infection', 'psoriasis', 'impetigo']


# h = input("Enter Here: ").lower()
# if h in x:
#     find.findingSymptoms(h)
# else:
#     print("NO")


# # -----------------------------------------------------------------------------------------
# # x={'hello':'hi'}
# # print(x.i)

# -------------------------------------------------------------------------------------------
# import spacy

# x = ['fungal infection', 'allergy', 'gerd', 'chronic cholestasis', 'drug reaction', 'peptic ulcer diseae', 'aids', 'diabetes', 'gastroenteritis', 'bronchial asthma', 'hypertension', 'migraine', 'cervical spondylosis', 'paralysis', 'jaundice', 'malaria', 'chicken pox', 'dengue', 'typhoid', 'hepatitis a', 'hepatitis b', 'hepatitis c', 'hepatitis d', 'hepatitis e', 'alcoholic hepatitis', 'tuberculosis', 'common cold', 'pneumonia', 'piles', 'heart attack', 'varicose veins', 'hypothyroidism', 'hyperthyroidism', 'hypoglycemia', 'osteoarthristis', 'arthritis', 'vertigo', 'acne', 'urinary tract infection', 'psoriasis', 'impetigo']


# # Load the pre-trained word embeddings model
# nlp = spacy.load("en_core_web_lg")

# # Check if two words are synonyms
# def are_synonyms(word1):
#     token1 = nlp(word1)
#     for word2 in x:
#         # print(word2)
#         token2 = nlp(word2)
#         similarity = token1.similarity(token2)
        
#         if similarity > 0.6:
#             print(token2)
#             return True
#     else:
#         return False
    
#     # Adjust the similarity threshold based on your requirements
#     # print(similarity)
#     # if similarity > 0.6:
#     #     return True
#     # else:
#     #     return False

# # Example usage
# word1 = "heart attack"
# # word2 = "fungal infection"
# if are_synonyms(word1):
#     print(f"{word1} and are synonyms.")
# else:
#     print(f"{word1} and are not synonyms.")

# -------------------------------------------------------------------------------
# import spacy
# from findSymptoms import FindSymptoms

# fnd = FindSymptoms()

# nlp = spacy.load("en_core_web_lg")

# def find_similar_word(target_array, sentence):
#     sentence_tokens = nlp(sentence)
#     sim = 0.000
#     k = ""
#     for target_word in target_array:
#         target_token = nlp(target_word)
#         similarities = [target_token.similarity(token) for token in sentence_tokens]
        
#         if max(similarities) > sim:
#             sim = max(similarities)
#             k = target_word

#         if max(similarities) > 0.8:
#             return target_word
#     if(sim > 0.55):
#         return k
#     else:
#         return "none"

# import pandas as pd

# dt = pd.read_csv("Testing.csv")

# data = dt["prognosis"]

# # Example usage
# target_array = []
# for i in data:
#     target_array.append(i)
# sentence = "Iam having an allergy"
# similar_word = find_similar_word(target_array, sentence)
# if similar_word == "none":
#     print("NONE")
# else:
#     res = fnd.findingSymptoms(similar_word)
#     print(res)

# -------------------------------------------------------------------------------

# import pandas as pd

# dt = pd.read_csv("Testing.csv")

# data = dt["prognosis"]
# k = []
# for i in data:
#     k.append(i)

# -------------------------------------------------------------------

# from getDatas import GetData

# gt = GetData()

# print(gt.symptoms(input("Enter your disease here : ")))


# -----------------------------------------------------------------------------------------------
# from getDatas import GetData

# getdt = GetData()

# --------------------------------------------------------------------------------------

# from outData import DataOut

# dt2 = DataOut()

# print(dt2.getMayCall())
# print(dt2.getHowHelp())

# -----------------------------------------------------------------------------------

# import spacy

# # Load the pre-trained word embeddings model
# nlp = spacy.load("en_core_web_md")

# # Retrieve element from a sentence with maximum similarity
# def retrieve_min_similarity(target_element, sentence):
#     target_token = nlp(target_element)
#     sentence_tokens = nlp(sentence)

#     min_similarity = 1.0
#     most_similar_element = None

#     for token in sentence_tokens:
#         similarity = target_token.similarity(token)
        
#         if similarity < min_similarity:
#             min_similarity = similarity
#             most_similar_element = token.text
    
#     return most_similar_element

# # Example usage
# target_element = "call"
# sentence = "please contact emergency service to dhanish"

# most_similar = retrieve_max_similarity(target_element, sentence)
# print(f"The element with maximum similarity to '{target_element}' in the sentence is '{most_similar}'.")
