from tkinter import *
def Train():
    """GUI"""
    import tkinter as tk
    import numpy as np
    import pandas as pd
    from collections import defaultdict
    from sklearn.decomposition import PCA
    from sklearn.preprocessing import LabelEncoder

    root = tk.Tk()

    root.geometry("800x850+250+5")
    root.title("Water Quality Prediction")
    root.configure(background="skyblue")
    
    ph = tk.IntVar()
    Hardness = tk.IntVar()
    Solids = tk.IntVar()
    Chloramines = tk.IntVar()
    Sulfate = tk.IntVar()
    Organic_carbon = tk.IntVar()
    Potability= tk.IntVar()
   # Conductivity = tk.IntVar()
    #Trihalomethanes = tk.IntVar()
    #Turbidity= tk.IntVar()
    #Potability= tk.IntVar()
    
    #===================================================================================================================
    def Detect():
        e1= ph.get()
        print(e1)
        e2= Hardness.get()
        print(e2)
        e3= Solids.get()
        print(e3)
        e4= Chloramines.get()
        print(e4)
        e5= Sulfate.get()
        print(e5)
        e6= Organic_carbon.get()
        print(e6)
        e7= Potability.get()
        print(e7)
       # e6= Conductivity.get()
       # print(e6)
       
       # e8= Trihalomethanes.get()
       # print(e8)
       # e9= Turbidity.get()
       # print(e9)
       # e10= Potability.get()
       # print(e10)
       
        
        
        #########################################################################################
        from joblib import dump , load
        a1=load('C:\Users\admin\Desktop\22SS142 Water Quality\100%WQ (1)\100%WQ')
        v= a1.predict([[e1,e2,e3,e4,e5,e6,e7]])
        print(v)
        if v[0]==0:
            print("Water Quality Bad")
            yes = tk.Label(root,text="Water Quality Bad",background="green",foreground="white",font=('times', 20, ' bold '),width=15)
            yes.place(x=300,y=500)
                     
        elif v[0]==1:
            print("Water Quality Good")
            no = tk.Label(root, text="Water Quality Good", background="green", foreground="white",font=('times', 20, ' bold '),width=15)
            no.place(x=300, y=500)
        
            


    l1=tk.Label(root,text="ph",background="olive",font=('times', 20, ' bold '),width=15)
    l1.place(x=5,y=5)
    ph=tk.Entry(root,bd=2,width=20,font=("TkDefaultFont", 20),textvar=ph)
    ph.place(x=400,y=1)

    l2=tk.Label(root,text="Hardness",background="olive",font=('times', 20, ' bold '),width=15)
    l2.place(x=5,y=50)
    Hardness=tk.Entry(root,bd=2,width=20,font=("TkDefaultFont", 20),textvar=Hardness)
    Hardness.place(x=400,y=50)

    l3=tk.Label(root,text="Solids",background="olive",font=('times', 20, ' bold '),width=15)
    l3.place(x=5,y=100)
    Solids=tk.Entry(root,bd=2,width=20,font=("TkDefaultFont", 20),textvar=Solids)
    Solids.place(x=400,y=100)
    
    l4=tk.Label(root,text="Chloramines",background="olive",font=('times', 20, ' bold '),width=15)
    l4.place(x=5,y=150)
    Chloramines=tk.Entry(root,bd=2,width=20,font=("TkDefaultFont", 20),textvar=Chloramines)
    Chloramines.place(x=400,y=150)

    l5=tk.Label(root,text="Sulfate",background="olive",font=('times', 20, ' bold '),width=15)
    l5.place(x=5,y=200)
    Sulfate=tk.Entry(root,bd=2,width=20,font=("TkDefaultFont", 20),textvar=Sulfate)
    Sulfate.place(x=400,y=200)
    
    l6=tk.Label(root,text="Organic_carbon",background="olive",font=('times', 20, ' bold '),width=15)
    l6.place(x=5,y=250)
    Organic_carbon=tk.Entry(root,bd=2,width=20,font=("TkDefaultFont", 20),textvar=Organic_carbon)
    Organic_carbon.place(x=400,y=250)
    
    l7=tk.Label(root,text="Potability",background="olive",font=('times', 20, ' bold '),width=15)
    l7.place(x=5,y=300)
    Potability=tk.Entry(root,bd=2,width=20,font=("TkDefaultFont", 20),textvar=Potability)
    Potability.place(x=400,y=300)
    
    
    
    button1 = tk.Button(root,text="Submit",command=Detect,font=('times', 20, ' bold '),width=10)
    button1.place(x=300,y=400)

    #l6=tk.Label(root,text="Conductivity",background="olive",font=('times', 20, ' bold '),width=15)
    #l6.place(x=5,y=250)
    #Conductivity=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=Conductivity)
    #Conductivity.place(x=400,y=250)

    #l7=tk.Label(root,text="Organic_carbon",background="olive",font=('times', 20, ' bold '),width=15)
    #l7.place(x=5,y=300)
    #Organic_carbon=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=Organic_carbon)
    #Organic_carbon.place(x=400,y=300)

   # l8=tk.Label(root,text="Trihalomethanes",background="olive",font=('times', 20, ' bold '),width=15)
    #l8.place(x=5,y=350)
    #Trihalomethanes=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=Trihalomethanes)
    #Trihalomethanes.place(x=400,y=350)

   # l9=tk.Label(root,text="Turbidity",background="olive",font=('times', 20, ' bold '),width=17)
   # l9.place(x=5,y=400)
   # Turbidity=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=Turbidity)
    #Turbidity.place(x=400,y=400)
    

    

   # l10=tk.Label(root,text="Potability",background="olive",font=('times', 20, ' bold '),width=10)
   # l10.place(x=5,y=450)
   # Potability=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=Potability)
    #Potability.place(x=400,y=450)
   # l11=tk.Label(root,text="ParentAnsweringSurvey",background="olive",font=('times', 20, ' bold '),width=20)
    #l11.place(x=5,y=500)
   # ParentAnsweringSurvey.place(x=400,y=500)

    #l12=tk.Label(root,text="ParentsShoolSatisfaction",background="olive",font=('times', 20, ' bold '),width=20)
   # l12.place(x=5,y=550)
   # ParentsShoolSatisfaction=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=ParentsShoolSatisfaction)
   # ParentsShoolSatisfaction.place(x=400,y=550)

  # l13=tk.Label(root,text="StudentAbsenceDays",background="olive",font=('times', 20, ' bold '),width=17)
  # l13.place(x=5,y=600)
   # StudentAbsenceDays=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=StudentAbsenceDays)
   # StudentAbsenceDays.place(x=400,y=600)

    

    root.mainloop()

Train()