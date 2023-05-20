import os
import pandas as pd
import numpy as np
from tkinter import *
from tkinter import filedialog
import tkinter.font as font
from functools import partial
from pyresparser import ResumeParser
from sklearn import datasets, linear_model


class train_model:

    def train(self):
        data = pd.read_csv('training_dataset.csv')
        array = data.values

        for i in range(len(array)):
            if array[i][0] == "Male":
                array[i][0] = 1
            else:
                array[i][0] = 0

        df = pd.DataFrame(array)

        maindf = df[[0, 1, 2, 3, 4, 5, 6]]
        mainarray = maindf.values

        temp = df[7]
        train_y = temp.values

        self.mul_lr = linear_model.LogisticRegression(multi_class='multinomial', solver='newton-cg', max_iter=1000)
        self.mul_lr.fit(mainarray, train_y)

    def test(self, test_data):
        try:
            test_predict = list()
            for i in test_data:
                test_predict.append(int(i))
            y_pred = self.mul_lr.predict([test_predict])
            return y_pred
        except:
            print("All Factors For Finding Personality Not Entered!")


def check_type(data):
    if type(data) == str or type(data) == str:
        return str(data).title()
    if type(data) == list or type(data) == tuple:
        str_list = ""
        for i, item in enumerate(data):
            str_list += item + ", "
        return str_list
    else:
        return str(data)


def prediction_result(top, aplcnt_name, cv_path, personality_values):
    "after applying a job"
    top.withdraw()
    applicant_data = {"Candidate Name": aplcnt_name.get(), "CV Location": cv_path}

    age = personality_values[1]

    print("\n############# Candidate Entered Data #############\n")
    print(applicant_data, personality_values)

    personality = model.test(personality_values)
    print("\n############# Predicted Personality #############\n")
    print(personality)
    data = ResumeParser(cv_path).get_extracted_data()

    try:
        del data['name']
        if len(data['mobile_number']) < 10:
            del data['mobile_number']
    except:
        pass

    print("\n############# Resume Parsed Data #############\n")

    for key in data.keys():
        if data[key] is not None:
            print('{} : {}'.format(key, data[key]))

    result = Tk()
    #  result.geometry('700x550')
    result.overrideredirect(False)
    result.geometry("{0}x{1}+0+0".format(result.winfo_screenwidth(), result.winfo_screenheight()))
    result.configure(background='White')
    result.title("Predicted Personality")

    # Title
    titleFont = font.Font(family='Arial', size=40, weight='bold')
    Label(result, text="Result - Personality Prediction", foreground='green', bg='white', font=titleFont, pady=10,
          anchor=CENTER).pack(fill=BOTH)

    Label(result, text=str('{} : {}'.format("Name:", aplcnt_name.get())).title(), foreground='black', bg='white',
          anchor='w').pack(fill=BOTH)
    Label(result, text=str('{} : {}'.format("Age:", age)), foreground='black', bg='white', anchor='w').pack(fill=BOTH)
    for key in data.keys():
        if data[key] is not None:
            Label(result, text=str('{} : {}'.format(check_type(key.title()), check_type(data[key]))),
                  foreground='black', bg='white', anchor='w', width=60).pack(fill=BOTH)
    Label(result, text=str("perdicted personality: " + personality).title(), foreground='black', bg='white',
          anchor='w').pack(fill=BOTH)

    quitBtn = Button(result, text="Exit", command=lambda: result.destroy()).pack()

    terms_mean = """
#Open to Experience: It involves various dimensions, like imagination, sensitivity, attentiveness, preference to variety, and curiosity.  
#Conscientiousness: This trait is used to describe the carefulness and diligence of the person. It is the quality that describes how organized and efficient a person is.
#Extraversion: It is the trait that describes how the best candidates can interact with people that is how good are his/her social skills.
#Agreeableness: It is a quality that analyses the individual behavior based on the generosity, sympathy, cooperativeness and ability to adjust with people.  
#Neuroticism: This trait usually describes a person to have mood swings and has extreme expressive power.
  """

    Label(result, text=terms_mean, foreground='green', bg='white', anchor='w', justify=LEFT).pack(fill=BOTH)

    result.mainloop()


def perdict_person():
    """Predict Personality"""

    # Closing The Previous Window
    root.withdraw()

    # Creating new window
    top = Toplevel()
    top.geometry('700x500')
    top.configure(background='black')
    top.title("Submit Your Information")

    # Title
    titleFont = font.Font(family='Kanit', size=20, weight='bold')
    lab = Label(top, text="Personality Prediction Via CV", foreground='White', bg='black', font=titleFont, pady=10).pack()

    # Job_Form
    job_list = ('Select Job', '101-Developer at Google', '102-Saller At Amazon', '103-Data Engineer at META')
    job = StringVar(top)
    job.set(job_list[0])
    l4 = Label(top, text="Upload Resume - ", foreground='white', bg='Blue').place(x=70, y=220)
    l1 = Label(top, text="Applicant Name - ", foreground='white', bg='Blue').place(x=70, y=130)
    l2 = Label(top, text="Age - ", foreground='white', bg='blue').place(x=70, y=160)
    l3 = Label(top, text="Gender - ", foreground='white', bg='blue').place(x=70, y=190)
    l5 = Label(top, text="Enjoy New Experience or thing(Openness) - ", foreground='white', bg='blue').place(x=70,
                                                                                                             y=250)
    l6 = Label(top, text="How Offen You Feel Negativity(Neuroticism) - ", foreground='white', bg='blue').place(x=70,
                                                                                                                y=280)
    l7 = Label(top, text="How outgoing and social interaction you like(Extraversion) - ", foreground='white',
               bg='blue').place(x=70, y=310)
    l8 = Label(top, text="How much would you like work with your peers(Agreeableness) - ", foreground='white',
               bg='blue').place(x=70, y=340)
    l9 = Label(top, text="Wishing to do one's work well and thoroughly(Conscientiousness) - ", foreground='white',
               bg='blue').place(x=70, y=370)
    cv = Button(top, text="Select CV", command=lambda: OpenFile(cv))
    cv.place(x=450, y=220, width=180)
    sName = Entry(top)
    sName.place(x=450, y=130, width=180)
    age = Entry(top)
    age.place(x=450, y=160, width=180)
    gender = IntVar()
    R1 = Radiobutton(top, text="Male", variable=gender, value=1, padx=7)
    R1.place(x=450, y=190)
    R2 = Radiobutton(top, text="Female", variable=gender, value=0, padx=3)
    R2.place(x=540, y=190)

    openness = Entry(top)
    openness.insert(0, '1-10')
    openness.place(x=450, y=250, width=180)
    neuroticism = Entry(top)
    neuroticism.insert(0, '1-10')
    neuroticism.place(x=450, y=280, width=180)
    conscientiousness = Entry(top)
    conscientiousness.insert(0, '1-10')
    conscientiousness.place(x=450, y=310, width=180)
    agreeableness = Entry(top)
    agreeableness.insert(0, '1-10')
    agreeableness.place(x=450, y=340, width=180)
    extraversion = Entry(top)
    extraversion.insert(0, '1-10')
    extraversion.place(x=450, y=370, width=180)

    submitBtn = Button(top, padx=2, pady=0, text="Submit", bd=0, foreground='blue', bg='white', font=(15))
    submitBtn.config(command=lambda: prediction_result(top, sName, loc, (
    gender.get(), age.get(), openness.get(), neuroticism.get(), conscientiousness.get(), agreeableness.get(),
    extraversion.get())))
    submitBtn.place(x=350, y=400, width=220)

    top.mainloop()


def OpenFile(b4):
    global loc;
    name = filedialog.askopenfilename(initialdir="A:\RESUMES\MY RESUME FS.pdf",
                                      filetypes=(("Document", "*.docx*"), ("PDF", "*.pdf*"), ('All files', '*')),
                                      title="Choose a file."
                                      )
    try:
        filename = os.path.basename(name)
        loc = name
    except:
        filename = name
        loc = name
    b4.config(text=filename)
    return


if __name__ == "__main__":
    model = train_model()
    model.train()

    root = Tk()
    root.geometry('700x500')
    root.configure(background='black')
    root.title("Personality Prediction System Via CV")
    titleFont = font.Font(family='Secular One', size=25, weight='bold')
    homeBtnFont = font.Font(size=12, weight='bold')
    lab = Label(root, text="Personality Prediction System Via Cv", bg='black', foreground='Blue', font=titleFont,
                pady=30).pack()
    b2 = Button(root, padx=4, pady=4, width=30, text="CLICK HERE", bg='blue', foreground='white', bd=1,
                font=homeBtnFont, command=perdict_person).place(relx=0.5, rely=0.5, anchor=CENTER)
    root.mainloop()