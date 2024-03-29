from tkinter import *
root =  Tk()

root.title("Fibonacci")
root.geometry("400x400")

label_series = Label(root, text = "Fibonacci series : ")
input1 = Entry(root)
label_spiral = Label(root)

def Fibonacci():
    num = int(input.get())
    sum2 = 0 
    first_no = 0
    second_no = 1 
    sum = 0 
    counter = 1 
    while ( counter <= num):
        sum2 = sum2 + sum
        counter += 1 
        first_no = second_no
        second_no = sum
        sum = first_no + second_no
        label_series["text"] += str(sum2) + " "
        label_spiral["text"] = "Fibonacci series : " + str(sum2)
        
btn = Button(root, text = "Show in fibonacci series", command = Fibonacci, bg = 'white')
input1.pack()
btn.pack()
label_series.pack()
label_spiral.pack()