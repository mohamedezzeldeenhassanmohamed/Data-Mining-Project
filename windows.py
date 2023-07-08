import tkinter
from tkinter import *
from tkinter import ttk



window = tkinter.Tk()
window.config(bg="#4C5270")
window.geometry("700x500")
window.title("Data Entry Form")

frame = tkinter.Frame(window , width=700, height=500)
frame.pack()

#first frame

#Labels
laptop_info_frame = tkinter.LabelFrame(frame, text="Please Enter Laptop features")
laptop_info_frame.grid(row=0, column=0, padx=20, pady=10)

brand_label = tkinter.Label(laptop_info_frame, text="Brand")
brand_label.grid(row=0, column=0)
processor_brand_label = tkinter.Label(laptop_info_frame, text="Processor Brand")
processor_brand_label.grid(row=0, column=1)
processor_generation_label = tkinter.Label(laptop_info_frame, text="Processor Genertion")
processor_generation_label.grid(row=0, column=2)

ram_type_label = tkinter.Label(laptop_info_frame, text="RAM Type")
ram_type_label.grid(row=2, column=0)
ssd_label = tkinter.Label(laptop_info_frame, text="SSD")
ssd_label.grid(row=2, column=1)
hdd_label = tkinter.Label(laptop_info_frame, text="HDD")
hdd_label.grid(row=2, column=2)

os_label = tkinter.Label(laptop_info_frame, text="OS")
os_label.grid(row=4, column=0)
graphic_label = tkinter.Label(laptop_info_frame, text="Graphic Card")
graphic_label.grid(row=4, column=1)
display_label = tkinter.Label(laptop_info_frame, text="Display Size")
display_label.grid(row=4, column=2)

touch_label = tkinter.Label(laptop_info_frame, text="Touch Screen")
touch_label.grid(row=6, column=0)
moofice_label = tkinter.Label(laptop_info_frame, text="Microsoft Office")
moofice_label.grid(row=6, column=1)
discount_label = tkinter.Label(laptop_info_frame, text="Discount")
discount_label.grid(row=6, column=2)



#Entry
brand_entry = tkinter.Entry(laptop_info_frame)
brand_entry.grid(row=1, column=0)
processor_brand_entry = tkinter.Entry(laptop_info_frame)
processor_brand_entry.grid(row=1, column=1)
processor_generation_entry = tkinter.Entry(laptop_info_frame)
processor_generation_entry.grid(row=1, column=2)

ram_type_entry = tkinter.Entry(laptop_info_frame)
ram_type_entry.grid(row=3, column=0)
ssd_entry = tkinter.Entry(laptop_info_frame)
ssd_entry.grid(row=3, column=1)
hdd_entry = tkinter.Entry(laptop_info_frame)
hdd_entry.grid(row=3, column=2)

os_type_entry = tkinter.Entry(laptop_info_frame)
os_type_entry.grid(row=5, column=0)
graphic_type_entry = tkinter.Entry(laptop_info_frame)
graphic_type_entry.grid(row=5, column=1)
display_type_entry = tkinter.Entry(laptop_info_frame)
display_type_entry.grid(row=5, column=2)

touch_type_entry = tkinter.Entry(laptop_info_frame)
touch_type_entry.grid(row=7, column=0)
moofice_type_entry = tkinter.Entry(laptop_info_frame)
moofice_type_entry.grid(row=7, column=1)
discount_type_entry = tkinter.Entry(laptop_info_frame)
discount_type_entry.grid(row=7, column=2)


for widget in laptop_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

#second frame
algorithm_frame = tkinter.LabelFrame(frame, text="Applying Algorithm")
algorithm_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)

title_label = tkinter.Label(algorithm_frame, text="Choose Algorithm")
title_combobox = ttk.Combobox(algorithm_frame, values=["" , "Linear Regression", "Logistic Regression", "KNN", "SVM" , "Naive Bays" , "Decision Tree"])
title_label.grid(row=0, column=2)
title_combobox.grid(row=1, column=2)

#Button
btn_label = tkinter.Label(frame)
btn_label.grid(row=4, column=0)

def predict():
    print("10000!")
    btn_label.configure(text="Latest Price is 10000!")

button = tkinter.Button(frame, width=10 , text="Predict" , command=predict)
button.grid(row=3, column=0, sticky="news", padx=20, pady=10)

for widget in algorithm_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)





window.mainloop()



