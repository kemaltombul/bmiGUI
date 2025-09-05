import tkinter

window = tkinter.Tk()
window.title("whats my BMI")
window.geometry("300x300")

####
def calculate():
    try:
        weight = int(weightInput.get())
        height = int(heightInput.get())
        bmi = weight / (height/100) ** 2
        if bmi < 18.5:
            massageText.config(text="you are under weight",bg="red")
        elif 18.5 <= bmi < 25:
            massageText.config(text="you are normal weight", bg="green")
        elif 25 <= bmi < 30:
            massageText.config(text="you are over weight", bg="orange")
        elif 30 <= bmi:
            massageText.config(text="you are OBESE",bg="red")
    except ValueError:
        weight = weightInput.get()
        height = heightInput.get()

        if weight=="" or height =="":
            massageText.config(text="please enter your weight and height",bg="red")
        else:
            massageText.config(text="please enter a numeric value",bg="red")
###
###
weighText = tkinter.Label(window, text="enter weight(kg)")
heighText = tkinter.Label(window, text="enter height(cm)")
massageText = tkinter.Label(window, text="")
weightInput = tkinter.Entry()
heightInput = tkinter.Entry()
calculateButton = tkinter.Button(window, text="calculate", command=calculate)
###
###
weighText.pack()
weightInput.pack()
heighText.pack()
heightInput.pack()
calculateButton.pack()
massageText.pack()
###

window.mainloop()


