from tkinter import *

#window
window = Tk()
window.title("BMI Calculator")
window.minsize(width = 200, height = 200)
window.config(padx = 20, pady = 50)

#entry & label
heightLabel = Label(text = "Enter Your Height (cm)")
heightLabel.pack()

heightEntry = Entry(width = 12)
heightEntry.pack()

weightLabel = Label(text = "Enter Your Weight (kg)")
weightLabel.pack()

weightEntry = Entry(width = 12)
weightEntry.pack()

resultLabel = None

def bmi_calculation():
    global resultLabel
    
    if resultLabel:
        resultLabel.destroy()
    
    try:
        x = int(weightEntry.get())
        y = int(heightEntry.get())
        bmi = x / ((y / 100) * (y / 100))

        result_func(bmi)
    except ValueError:
        resultLabel = Label(text= "Please enter valid numbers.")
        resultLabel.pack()


#button
calculateButton = Button(text = "Calculate", command = bmi_calculation)
calculateButton.pack()

def result_func(bmi):
    global resultLabel

    if resultLabel:
        resultLabel.destroy()

    if bmi < 16.0:
        resultLabel = Label(text=f"Your BMI is {bmi: .1f}. You are severely underweight.")
        resultLabel.pack()
    elif 16.0 <= bmi < 18.4:
        resultLabel = Label(text=f"Your BMI is {bmi: .1f}. You are underweight.")
        resultLabel.pack()
    elif 18.4 <= bmi < 24.9:
        resultLabel = Label(text=f"Your BMI is {bmi: .1f}. You are normal.")
        resultLabel.pack()
    elif 24.9 <= bmi < 29.9:
        resultLabel = Label(text=f"Your BMI is {bmi: .1f}. You are overweight.")
        resultLabel.pack()
    elif 29.9 <= bmi < 34.9:
        resultLabel = Label(text=f"Your BMI is {bmi: .1f}. You are moderately obese.")
        resultLabel.pack()
    elif 34.9 <= bmi < 39.9:
        resultLabel = Label(text=f"Your BMI is {bmi: .1f}. You are severely obese.")
        resultLabel.pack()
    else:
        resultLabel = Label(text=f"Your BMI is {bmi: .1f}. You are morbidly obese.")
        resultLabel.pack()


window.mainloop()
