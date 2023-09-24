from symptoms_extraction import Symptoms as sv
from spacy.matcher import Matcher


class AddMatchers:

    def addIn(self, matcher:Matcher) -> Matcher:

        matcher.add('itching', [sv.itching1])
        matcher.add('itching', [sv.itching2])

        matcher.add('skin_rash', [sv.skinrashes1])
        matcher.add('skin_rash', [sv.skinrashes2])
        matcher.add('skin_rash', [sv.skinrashes3])
        matcher.add('skin_rash', [sv.skinrashes4])

        matcher.add('nodal_skin_eruptions', [sv.nodalskin1])
        matcher.add('nodal_skin_eruptions', [sv.nodalskin2])
        matcher.add('nodal_skin_eruptions', [sv.nodalskin3])

        matcher.add('continuous_sneezing', [sv.sneezing1])
        matcher.add('continuous_sneezing', [sv.sneezing2])

        matcher.add('shivering', [sv.shivering1])

        matcher.add('chills', [sv.chills1])
        matcher.add('chills', [sv.chills2])

        matcher.add('joint_pain', [sv.jointpain1])
        matcher.add('joint_pain', [sv.jointpain2])
        matcher.add('joint_pain', [sv.jointpain3])
        matcher.add('joint_pain', [sv.jointpain4])

        matcher.add('stomach_pain', [sv.stomachpain1])
        matcher.add('stomach_pain', [sv.stomachpain2])
        matcher.add('stomach_pain', [sv.stomachpain3])
        matcher.add('stomach_pain', [sv.stomachpain4])

        matcher.add('acidity', [sv.acidity1])

        matcher.add('ulcers_on_tongue', [sv.toungueulcer1])
        matcher.add('ulcers_on_tongue', [sv.toungueulcer2])
        matcher.add('ulcers_on_tongue', [sv.toungueulcer3])
        matcher.add('ulcers_on_tongue', [sv.toungueulcer4])

        matcher.add('muscle_wasting', [sv.musclewasting1])
        matcher.add('muscle_wasting', [sv.musclewasting2])
        matcher.add('muscle_wasting', [sv.musclewasting3])

        matcher.add('vomiting', [sv.vomiting1])

        matcher.add('burning_micturition', [sv.burningmicturition1])
        matcher.add('burning_micturition', [sv.burningmicturition2])

        matcher.add('spotting_urination', [sv.spottingurination1])

        matcher.add('fatigue', [sv.fatigue1])

        matcher.add('weight_gain', [sv.weightgain1])
        matcher.add('weight_gain', [sv.weightgain2])
        matcher.add('weight_gain', [sv.weightgain3])

        matcher.add('anxiety', [sv.anxiety1])

        matcher.add('cold_hands_and_feets', [sv.cold1])
        matcher.add('cold_hands_and_feets', [sv.cold2])
        matcher.add('cold_hands_and_feets', [sv.cold3])
        matcher.add('cold_hands_and_feets', [sv.cold4])

        matcher.add('mood_swings', [sv.moodswings1])

        matcher.add('weight_loss', [sv.weightloss1])
        matcher.add('weight_loss', [sv.weightloss2])
        matcher.add('weight_loss', [sv.weightloss3])
        matcher.add('weight_loss', [sv.weightloss4])

        matcher.add('restlessness', [sv.restlessness1])

        matcher.add('lethargy', [sv.lethargy1])

        matcher.add('patches_in_throat', [sv.patches1])
        matcher.add('patches_in_throat', [sv.patches2])

        matcher.add('irregular_sugar_level', [sv.irregularsugarlevel1])
        matcher.add('irregular_sugar_level', [sv.irregularsugarlevel2])

        matcher.add('cough', [sv.cough1])

        matcher.add('high_fever', [sv.highfever1])
        matcher.add('high_fever', [sv.highfever2])
        matcher.add('high_fever', [sv.highfever3])

        matcher.add('sunken_eyes', [sv.sunkeneyes1])
        matcher.add('sunken_eyes', [sv.sunkeneyes2])

        matcher.add('breathlessness', [sv.breathlessness1])
        matcher.add('breathlessness', [sv.breathlessness2])

        matcher.add('sweating', [sv.sweating1])

        matcher.add('dehydration', [sv.dehydration1])

        matcher.add('indigestion', [sv.indigestion1])

        matcher.add('headache', [sv.headache1])
        matcher.add('headache', [sv.headache2])
        matcher.add('headache', [sv.headache3])

        matcher.add('yellowish_skin', [sv.yellowishskin1])
        matcher.add('yellowish_skin', [sv.yellowishskin2])

        matcher.add('dark_urine', [sv.darkurine1])
        matcher.add('dark_urine', [sv.darkurine2])

        matcher.add('nausea', [sv.nausea1])

        matcher.add('loss_of_appetite', [sv.lossofappetite1])
        matcher.add('loss_of_appetite', [sv.lossofappetite2])
        matcher.add('loss_of_appetite', [sv.lossofappetite3])

        matcher.add('pain_behind_the_eyes', [sv.painbehindtheeyes1])
        matcher.add('pain_behind_the_eyes', [sv.painbehindtheeyes2])
        matcher.add('pain_behind_the_eyes', [sv.painbehindtheeyes3])

        matcher.add('back_pain', [sv.backpain1])
        matcher.add('back_pain', [sv.backpain2])
        matcher.add('back_pain', [sv.backpain3])

        matcher.add('constipation', [sv.constipation1])

        matcher.add('abdominal_pain', [sv.abdominalpain1])
        matcher.add('abdominal_pain', [sv.abdominalpain2])
        matcher.add('abdominal_pain', [sv.abdominalpain3])

        matcher.add('diarrhoea', [sv.diarrhoea1])

        matcher.add('mild_fever', [sv.mildfever1])
        matcher.add('mild_fever', [sv.mildfever2])

        matcher.add('yellow_urine', [sv.yellowurine1])
        matcher.add('yellow_urine', [sv.yellowurine2])
        matcher.add('yellow_urine', [sv.yellowurine3])
        matcher.add('yellow_urine', [sv.yellowurine4])

        matcher.add('yellowing_of_eyes', [sv.yellowingofeyes1])
        matcher.add('yellowing_of_eyes', [sv.yellowingofeyes2])
        matcher.add('yellowing_of_eyes', [sv.yellowingofeyes3])

        matcher.add('acute_liver_failure', [sv.acuteliverfailure1])
        matcher.add('acute_liver_failure', [sv.acuteliverfailure2])

        matcher.add('fluid_overload', [sv.fluidoverload1])

        matcher.add('swelling_of_stomach', [sv.swellingofstomach1])
        matcher.add('swelling_of_stomach', [sv.swellingofstomach2])

        matcher.add('swelled_lymph_nodes', [sv.swelledlymphnodes1])
        matcher.add('swelled_lymph_nodes', [sv.swelledlymphnodes2])

        matcher.add('malaise', [sv.malaise1])

        matcher.add('blurred_and_distorted_vision', [sv.blurredanddistortedvision1])
        matcher.add('blurred_and_distorted_vision', [sv.blurredanddistortedvision2])
        matcher.add('blurred_and_distorted_vision', [sv.blurredanddistortedvision3])

        matcher.add('phlegm', [sv.phlegm1])

        matcher.add('throat_irritation', [sv.throatirritation1])
        matcher.add('throat_irritation', [sv.throatirritation2])

        matcher.add('redness_of_eyes', [sv.rednessofeyes1])
        matcher.add('redness_of_eyes', [sv.rednessofeyes2])
        matcher.add('redness_of_eyes', [sv.rednessofeyes3])
        matcher.add('redness_of_eyes', [sv.rednessofeyes4])

        matcher.add('sinus_pressure', [sv.sinuspressure1])
        matcher.add('sinus_pressure', [sv.sinuspressure2])

        matcher.add('runny_nose', [sv.runnynose1])
        matcher.add('runny_nose', [sv.runnynose2])

        matcher.add('congestion', [sv.congestion1])

        matcher.add('chest_pain', [sv.chestpain1])
        matcher.add('chest_pain', [sv.chestpain2])

        matcher.add('weakness_in_limbs', [sv.weaknessinlimbs1])
        matcher.add('weakness_in_limbs', [sv.weaknessinlimbs2])
        matcher.add('weakness_in_limbs', [sv.weaknessinlimbs3])

        matcher.add('fast_heart_rate', [sv.fastheartrate1])
        matcher.add('fast_heart_rate', [sv.fastheartrate2])
        matcher.add('fast_heart_rate', [sv.fastheartrate3])

        matcher.add('pain_during_bowel_movements', [sv.painduringbowelmovements1])
        matcher.add('pain_during_bowel_movements', [sv.painduringbowelmovements2])
        matcher.add('pain_during_bowel_movements', [sv.painduringbowelmovements3])

        matcher.add('pain_in_anal_region', [sv.paininanalregion1])
        matcher.add('pain_in_anal_region', [sv.paininanalregion2])

        matcher.add('bloody_stool', [sv.bloodystool1])

        matcher.add('irritation_in_anus', [sv.irritationinanus1])
        matcher.add('irritation_in_anus', [sv.irritationinanus2])
        matcher.add('irritation_in_anus', [sv.irritationinanus3])

        matcher.add('neck_pain', [sv.neckpain1])
        matcher.add('neck_pain', [sv.neckpain2])
        matcher.add('neck_pain', [sv.neckpain3])

        matcher.add('dizziness', [sv.dizziness1])

        matcher.add('cramps', [sv.cramps1])

        matcher.add('bruising', [sv.bruising1])

        matcher.add('obesity', [sv.obesity1])

        matcher.add('swollen_legs', [sv.swollenlegs1])
        matcher.add('swollen_legs', [sv.swollenlegs2])

        matcher.add('swollen_blood_vessels', [sv.swollenbloodvessels1])
        matcher.add('swollen_blood_vessels', [sv.swollenbloodvessels2])

        matcher.add('puffy_face_and_eyes', [sv.puffyfaceandeyes1])
        matcher.add('puffy_face_and_eyes', [sv.puffyfaceandeyes2])
        matcher.add('puffy_face_and_eyes', [sv.puffyfaceandeyes3])

        matcher.add('enlarged_thyroid', [sv.enlargedthyroid1])
        matcher.add('enlarged_thyroid', [sv.enlargedthyroid2])
        matcher.add('enlarged_thyroid', [sv.enlargedthyroid3])

        matcher.add('brittle_nails', [sv.brittlenails1])

        matcher.add('swollen_extremeties', [sv.swollenextremeties1])
        matcher.add('swollen_extremeties', [sv.swollenextremeties2])

        matcher.add('excessive_hunger', [sv.excessivehunger1])
        matcher.add('excessive_hunger', [sv.excessivehunger2])

        matcher.add('extra_marital_contacts', [sv.extramaritalcontacts1])

        matcher.add('drying_and_tingling_lips', [sv.dryingandtinglinglips1])
        matcher.add('drying_and_tingling_lips', [sv.dryingandtinglinglips2])
        matcher.add('drying_and_tingling_lips', [sv.dryingandtinglinglips3])

        matcher.add('slurred_speech', [sv.slurredspeech1])

        matcher.add('knee_pain', [sv.kneepain1])
        matcher.add('knee_pain', [sv.kneepain2])
        matcher.add('knee_pain', [sv.kneepain3])

        matcher.add('hip_joint_pain', [sv.hipjointpain1])
        matcher.add('hip_joint_pain', [sv.hipjointpain2])

        matcher.add('muscle_weakness', [sv.muscleweakness1])
        matcher.add('muscle_weakness', [sv.muscleweakness2])

        matcher.add('stiff_neck', [sv.stiffneck1])
        matcher.add('stiff_neck', [sv.stiffneck2])
        matcher.add('stiff_neck', [sv.stiffneck3])
        matcher.add('stiff_neck', [sv.stiffneck4])

        matcher.add('swelling_joints', [sv.swellingjoints1])
        matcher.add('swelling_joints', [sv.swellingjoints2])

        matcher.add('movement_stiffness', [sv.movementstiffness1])
        matcher.add('movement_stiffness', [sv.movementstiffness2])
        matcher.add('movement_stiffness', [sv.movementstiffness3])

        matcher.add('spinning_movements', [sv.spinningmovements1])

        matcher.add('loss_of_balance', [sv.lossofbalance1])
        matcher.add('loss_of_balance', [sv.lossofbalance2])

        matcher.add('unsteadiness', [sv.unsteadiness1])

        matcher.add('weakness_of_one_body_side', [sv.weaknessofonebodyside1])
        matcher.add('weakness_of_one_body_side', [sv.weaknessofonebodyside2])
        matcher.add('weakness_of_one_body_side', [sv.weaknessofonebodyside3])
        matcher.add('weakness_of_one_body_side', [sv.weaknessofonebodyside4])

        matcher.add('loss_of_smell', [sv.lossofsmell1])
        matcher.add('loss_of_smell', [sv.lossofsmell2])
        matcher.add('loss_of_smell', [sv.lossofsmell3])
        matcher.add('loss_of_smell', [sv.lossofsmell4])

        matcher.add('bladder_discomfort', [sv.bladderdiscomfort1])
        matcher.add('bladder_discomfort', [sv.bladderdiscomfort2])

        matcher.add('foul_smell_of_urine', [sv.foulsmellofurine1])
        matcher.add('foul_smell_of_urine', [sv.foulsmellofurine2])
        matcher.add('foul_smell_of_urine', [sv.foulsmellofurine3])

        matcher.add('continuous_feel_of_urine', [sv.continuousfeelofurine1])

        matcher.add('passage_of_gases', [sv.passageofgases1])
        matcher.add('passage_of_gases', [sv.passageofgases2])

        matcher.add('internal_itching', [sv.internalitching1])
        matcher.add('internal_itching', [sv.internalitching2])

        matcher.add('toxic_look_(typhos)', [sv.toxiclook1])
        matcher.add('toxic_look_(typhos)', [sv.toxiclook2])
        matcher.add('toxic_look_(typhos)', [sv.toxiclook3])

        matcher.add('depression', [sv.depression1])

        matcher.add('irritability', [sv.irritability1])

        matcher.add('muscle_pain', [sv.musclepain1])
        matcher.add('muscle_pain', [sv.musclepain2])
        matcher.add('muscle_pain', [sv.musclepain3])

        matcher.add('altered_sensorium', [sv.alteredsensorium1])

        matcher.add('red_spots_over_body', [sv.redspotsoverbody1])
        matcher.add('red_spots_over_body', [sv.redspotsoverbody2])

        matcher.add('belly_pain', [sv.bellypain1])
        matcher.add('belly_pain', [sv.bellypain2])
        matcher.add('belly_pain', [sv.bellypain3])

        matcher.add('abnormal_menstruation', [sv.abnormalmenstruation1])
        matcher.add('abnormal_menstruation', [sv.abnormalmenstruation2])

        matcher.add('dischromic_patches', [sv.dischromicpatches1])

        matcher.add('watering_from_eyes', [sv.wateringfromeyes1])
        matcher.add('watering_from_eyes', [sv.wateringfromeyes2])
        matcher.add('watering_from_eyes', [sv.wateringfromeyes3])

        matcher.add('increased_appetite', [sv.increasedappetite1])
        matcher.add('increased_appetite', [sv.increasedappetite2])

        matcher.add('polyuria', [sv.polyuria1])

        matcher.add('family_history', [sv.familyhistory1])
        matcher.add('family_history', [sv.familyhistory2])
        matcher.add('family_history', [sv.familyhistory3])

        matcher.add('mucoid_sputum', [sv.mucoidsputum1])

        matcher.add('rusty_sputum', [sv.rustysputum1])

        matcher.add('lack_of_concentration', [sv.lackofconcentration1])
        matcher.add('lack_of_concentration', [sv.lackofconcentration2])
        matcher.add('lack_of_concentration', [sv.lackofconcentration3])
        matcher.add('lack_of_concentration', [sv.lackofconcentration4])

        matcher.add('visual_disturbances', [sv.visualdisturbances1])
        matcher.add('visual_disturbances', [sv.visualdisturbances2])
        matcher.add('visual_disturbances', [sv.visualdisturbances3])

        matcher.add('receiving_blood_transfusion', [sv.receivingbloodtransfusion1])
        matcher.add('receiving_blood_transfusion', [sv.receivingbloodtransfusion2])

        matcher.add('receiving_unsterile_injections', [sv.receivingunsterileinjections1])
        matcher.add('receiving_unsterile_injections', [sv.receivingunsterileinjections2])
        matcher.add('receiving_unsterile_injections', [sv.receivingunsterileinjections3])

        matcher.add('coma', [sv.coma1])

        matcher.add('stomach_bleeding', [sv.stomachbleeding1])
        matcher.add('stomach_bleeding', [sv.stomachbleeding2])
        matcher.add('stomach_bleeding', [sv.stomachbleeding3])
        matcher.add('stomach_bleeding', [sv.stomachbleeding4])

        matcher.add('distention_of_abdomen', [sv.distentionofabdomen1])
        matcher.add('distention_of_abdomen', [sv.distentionofabdomen2])

        matcher.add('history_of_alcohol_consumption', [sv.historyofalcoholconsumption1])
        matcher.add('history_of_alcohol_consumption', [sv.historyofalcoholconsumption2])

        matcher.add('fluid_overload', [sv.fluidoverload1])

        matcher.add('blood_in_sputum', [sv.bloodinsputum1])

        matcher.add('prominent_veins_on_calf', [sv.prominentveinsoncalf1])

        matcher.add('palpitations', [sv.palpitations1])

        matcher.add('painful_walking', [sv.painfulwalking1])
        matcher.add('painful_walking', [sv.painfulwalking2])
        matcher.add('painful_walking', [sv.painfulwalking3])

        matcher.add('pus_filled_pimples', [sv.pusfilledpimples1])
        matcher.add('pus_filled_pimples', [sv.pusfilledpimples2])

        matcher.add('blackheads', [sv.blackheads1])

        matcher.add('scurring', [sv.scurring1])

        matcher.add('skin_peeling', [sv.skinpeeling1])
        matcher.add('skin_peeling', [sv.skinpeeling2])

        matcher.add('silver_like_dusting', [sv.silverlikedusting1])

        matcher.add('small_dents_in_nails', [sv.smalldentsinnails1])
        matcher.add('small_dents_in_nails', [sv.smalldentsinnails2])
        matcher.add('small_dents_in_nails', [sv.smalldentsinnails3])

        matcher.add('inflammatory_nails', [sv.inflammatorynails1])
        matcher.add('inflammatory_nails', [sv.inflammatorynails2])
        matcher.add('inflammatory_nails', [sv.inflammatorynails3])

        matcher.add('blister', [sv.blister1])

        matcher.add('red_sore_around_nose', [sv.redsorearoundnose1])
        matcher.add('red_sore_around_nose', [sv.redsorearoundnose2])

        matcher.add('yellow_crust_ooze', [sv.yellowcrustooze1])
        matcher.add('yellow_crust_ooze', [sv.yellowcrustooze2])

        matcher.add('prognosis', [sv.prognosis1])

        return matcher