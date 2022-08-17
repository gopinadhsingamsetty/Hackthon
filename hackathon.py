import tkinter 
from tkinter import *
import numpy as np
import pandas as pd
from PIL import Image,ImageTk

#List of the symptoms is listed here in list l1.

l1=['back_pain','constipation','abdominal_pain','diarrhoea','mild_fever','yellow_urine',
'yellowing_of_eyes','acute_liver_failure','fluid_overload','swelling_of_stomach',
'swelled_lymph_nodes','malaise','blurred_and_distorted_vision','phlegm','throat_irritation',
'redness_of_eyes','sinus_pressure','runny_nose','congestion','chest_pain','weakness_in_limbs',
'fast_heart_rate','pain_during_bowel_movements','pain_in_anal_region','bloody_stool',
'irritation_in_anus','neck_pain','dizziness','cramps','bruising','obesity','swollen_legs',
'swollen_blood_vessels','puffy_face_and_eyes','enlarged_thyroid','brittle_nails',
'swollen_extremeties','excessive_hunger','extra_marital_contacts','drying_and_tingling_lips',
'slurred_speech','knee_pain','hip_joint_pain','muscle_weakness','stiff_neck','swelling_joints',
'movement_stiffness','spinning_movements','loss_of_balance','unsteadiness',
'weakness_of_one_body_side','loss_of_smell','bladder_discomfort','foul_smell_of urine',
'continuous_feel_of_urine','passage_of_gases','internal_itching','toxic_look_(typhos)',
'depression','irritability','muscle_pain','altered_sensorium','red_spots_over_body','belly_pain',
'abnormal_menstruation','dischromic _patches','watering_from_eyes','increased_appetite','polyuria','family_history','mucoid_sputum',
'rusty_sputum','lack_of_concentration','visual_disturbances','receiving_blood_transfusion',
'receiving_unsterile_injections','coma','stomach_bleeding','distention_of_abdomen',
'history_of_alcohol_consumption','fluid_overload','blood_in_sputum','prominent_veins_on_calf',
'palpitations','painful_walking','pus_filled_pimples','blackheads','scurring','skin_peeling',
'silver_like_dusting','small_dents_in_nails','inflammatory_nails','blister','red_sore_around_nose',
'yellow_crust_ooze']

#List of Diseases is listed in list disease.

disease=['Fungal infection','Allergy','GERD','Chronic cholestasis','Drug Reaction',
'Peptic ulcer diseae','AIDS','Diabetes','Gastroenteritis','Bronchial Asthma','Hypertension',
' Migraine','Cervical spondylosis',
'Paralysis (brain hemorrhage)','Jaundice','Malaria','Chicken pox','Dengue','Typhoid','hepatitis A',
'Hepatitis B','Hepatitis C','Hepatitis D','Hepatitis E','Alcoholic hepatitis','Tuberculosis',
'Common Cold','Pneumonia','Dimorphic hemmorhoids(piles)',
'Heartattack','Varicoseveins','Hypothyroidism','Hyperthyroidism','Hypoglycemia','Osteoarthristis',
'Arthritis','(vertigo) Paroymsal  Positional Vertigo','Acne','Urinary tract infection','Psoriasis',
'Impetigo']

l2=[]

for i in range(0,len(l1)):
    l2.append(0)
df=pd.read_csv("Prototype.csv")
#Replace the values in the imported file by pandas by the inbuilt function replace in pandas.
df.replace({'prognosis':{'Fungal infection':0,'Allergy':1,'GERD':2,'Chronic cholestasis':3,'Drug Reaction':4,
'Peptic ulcer diseae':5,'AIDS':6,'Diabetes ':7,'Gastroenteritis':8,'Bronchial Asthma':9,'Hypertension ':10,
'Migraine':11,'Cervical spondylosis':12,
'Paralysis (brain hemorrhage)':13,'Jaundice':14,'Malaria':15,'Chicken pox':16,'Dengue':17,'Typhoid':18,'hepatitis A':19,
'Hepatitis B':20,'Hepatitis C':21,'Hepatitis D':22,'Hepatitis E':23,'Alcoholic hepatitis':24,'Tuberculosis':25,
'Common Cold':26,'Pneumonia':27,'Dimorphic hemmorhoids(piles)':28,'Heart attack':29,'Varicose veins':30,'Hypothyroidism':31,
'Hyperthyroidism':32,'Hypoglycemia':33,'Osteoarthristis':34,'Arthritis':35,
'(vertigo) Paroymsal  Positional Vertigo':36,'Acne':37,'Urinary tract infection':38,'Psoriasis':39,
'Impetigo':40}},inplace=True)

X= df[l1]

y = df[["prognosis"]]
np.ravel(y)      #returns 1-D array 

tr=pd.read_csv("Prototype-1.csv")

tr.replace({'prognosis':{'Fungal infection':0,'Allergy':1,'GERD':2,'Chronic cholestasis':3,'Drug Reaction':4,
'Peptic ulcer diseae':5,'AIDS':6,'Diabetes ':7,'Gastroenteritis':8,'Bronchial Asthma':9,'Hypertension ':10,
'Migraine':11,'Cervical spondylosis':12,
'Paralysis (brain hemorrhage)':13,'Jaundice':14,'Malaria':15,'Chicken pox':16,'Dengue':17,'Typhoid':18,'hepatitis A':19,
'Hepatitis B':20,'Hepatitis C':21,'Hepatitis D':22,'Hepatitis E':23,'Alcoholic hepatitis':24,'Tuberculosis':25,
'Common Cold':26,'Pneumonia':27,'Dimorphic hemmorhoids(piles)':28,'Heart attack':29,'Varicose veins':30,'Hypothyroidism':31,
'Hyperthyroidism':32,'Hypoglycemia':33,'Osteoarthristis':34,'Arthritis':35,
'(vertigo) Paroymsal  Positional Vertigo':36,'Acne':37,'Urinary tract infection':38,'Psoriasis':39,
'Impetigo':40}},inplace=True)
X_test= tr[l1]
y_test = tr[["prognosis"]]

np.ravel(y_test)
def DecisionTree():
    from sklearn import tree
    clf3 = tree.DecisionTreeClassifier() 
    clf3 = clf3.fit(X,y)
    
    from sklearn.metrics import accuracy_score
    y_pred=clf3.predict(X_test)
    print(accuracy_score(y_test, y_pred))
    print(accuracy_score(y_test, y_pred,normalize=False))

    psymptoms = [Symptom1.get(),Symptom2.get(),Symptom3.get(),Symptom4.get(),Symptom5.get()]

    for k in range(0,len(l1)):
        for z in psymptoms:
            if(z==l1[k]):
                l2[k]=1

    inputtest = [l2]
    predict = clf3.predict(inputtest)
    predicted=predict[0]

    h='no'
    for a in range(0,len(disease)):
        if(predicted == a):
            h='yes'
            break


    if(h=='yes'):
        t1.delete("1.0", END)
        t1.insert(END, disease[a])
    else:
        t1.delete("1.0", END)
        t1.insert(END, "Not Found")


# GUI stuff..............................................................................
        
root =Tk()
root.geometry("1800x800")
#root.attributes('-fullscreen', True)
root.configure(background='black')
image1 = Image.open("hackthon.png")
test = ImageTk.PhotoImage(image1)

label1 = tkinter.Label(image=test)
label1.image = test

# Position image
label1.place(x=0, y=0)


Symptom1 = StringVar()
Symptom1.set("Select symptom1")

Symptom2 = StringVar()
Symptom2.set("Select symptom2")

Symptom3 = StringVar()
Symptom3.set("Select symptom3")

Symptom4 = StringVar()
Symptom4.set("Select symptom4")

Symptom5 = StringVar()
Symptom5.set("Select symptom5")

Name = StringVar()
    
Name1Lb = Label(root,text="", fg="White", bg="Black")
Name1Lb.config(font=("Times",30,"bold italic"))
Name1Lb.grid(row=1, column=1, pady=20, sticky=W)

S11Lb = Label(root, text="", fg="White", bg="Black")
S11Lb.config(font=("Times",15,"bold italic"))
S11Lb.grid(row=2, column=1, pady=10, sticky=W)

S22Lb = Label(root, text="", fg="White", bg="Black")
S22Lb.config(font=("Times",15,"bold italic"))
S22Lb.grid(row=3, column=1, pady=10, sticky=W)

S33Lb = Label(root, text="", fg="White",bg="Black")
S33Lb.config(font=("Times",15,"bold italic"))
S33Lb.grid(row=4, column=1, pady=10, sticky=W)

S44Lb = Label(root, text="", fg="White", bg="Black")
S44Lb.config(font=("Times",15,"bold italic"))
S44Lb.grid(row=5, column=1, pady=10, sticky=W)

    
NameLb = Label(root, text="         Name of the Patient", fg="White", bg="Black")
NameLb.config(font=("Times",20,"bold italic"))
NameLb.grid(row=6, column=1, pady=20, sticky=W)

S1Lb = Label(root, text="         Enter Symptom 1", fg="White", bg="Black")
S1Lb.config(font=("Times",20,"bold italic"))
S1Lb.grid(row=7, column=1, pady=10, sticky=W)

S2Lb = Label(root, text="         Enter Symptom 2", fg="White", bg="Black")
S2Lb.config(font=("Times",20,"bold italic"))
S2Lb.grid(row=8, column=1, pady=10, sticky=W)

S3Lb = Label(root, text="         Enter Symptom 3", fg="White",bg="Black")
S3Lb.config(font=("Times",20,"bold italic"))
S3Lb.grid(row=9, column=1, pady=10, sticky=W)

S4Lb = Label(root, text="         Enter Symptom 4", fg="White", bg="Black")
S4Lb.config(font=("Times",20,"bold italic"))
S4Lb.grid(row=10, column=1, pady=10, sticky=W)

S5Lb = Label(root, text="         Enter Symptom 5", fg="White", bg="Black")
S5Lb.config(font=("Times",20,"bold italic"))
S5Lb.grid(row=11, column=1, pady=10, sticky=W)

S6Lb = Label(root, text="               ", fg="White", bg="Black")
S6Lb.config(font=("Times",15,"bold italic"))
S6Lb.grid(row=13, column=1, pady=10, sticky=W)

lrLb = Label(root, text="   PREDICTED DISEASE", fg="red", bg="black")
lrLb.config(font=("Times",20,"bold italic"))
lrLb.grid(row=16, column=1, pady=10,sticky=W)

S7Lb = Label(root, text="               ", fg="White", bg="Black")
S7Lb.config(font=("Times",15,"bold italic"))
S7Lb.grid(row=17, column=1, pady=10, sticky=W)

OPTIONS = sorted(l1)

NameEn = Entry(root, textvariable=Name,width=23)
NameEn.grid(row=6, column=5,ipady=8)

S1 = OptionMenu(root, Symptom1,*OPTIONS)
S1.grid(row=7, column=5)
S1.config(bg="black",fg="white")
S1["menu"].config(bg="black",fg="white")

S2 = OptionMenu(root, Symptom2,*OPTIONS)
S2.grid(row=8, column=5)
S2.config(bg="black",fg="white")
S2["menu"].config(bg="black",fg="white")

S3 = OptionMenu(root, Symptom3,*OPTIONS)
S3.grid(row=9, column=5)
S3.config(bg="black",fg="white")
S3["menu"].config(bg="black",fg="white")

S4 = OptionMenu(root, Symptom4,*OPTIONS)
S4.grid(row=10, column=5)
S4.config(bg="black",fg="white")
S4["menu"].config(bg="black",fg="white")

S5 = OptionMenu(root, Symptom5,*OPTIONS)
S5.grid(row=11, column=5)
S5.config(bg="black",fg="white")
S5["menu"].config(bg="black",fg="white")

dst = Button(root, text="PREDICT", command=DecisionTree,fg="Red",bg="Black")
dst.config(font=("Times",20,"bold"))
dst.grid(row=12, column=3,padx=10)

t1 = Text(root, height=1, width=40,bg="White",fg="black")
t1.config(font=("arial",20,"bold italic"))
t1.grid(row=16, column=5, padx=10)

root.mainloop()