from tkinter import *
from tkinter import ttk

# create a window
root = Tk()

# run a window
root.geometry("400x400")
root.title("Color Code Calculator v1.0")
root.resizable(False, False)

# tab control
tabControl = ttk.Notebook(root)

tab1 = Frame(tabControl)
tab2 = Frame(tabControl)
tab3 = Frame(tabControl)
tab4 = Frame(tabControl)

tabControl.add(tab1, text="4 Band")
tabControl.add(tab2, text="5 Band")
tabControl.add(tab4, text="About")
tabControl.pack(expand=1, fill="both")

# Combo box control
n = StringVar()
colors = ttk.Combobox(tab1, width=15, textvariable=n)

colors["values"] = (
    " Black",
    " Brown",
    " Red",
    " Orange",
    " Yellow",
    " Green",
    " Blue",
    " Violet",
    " Grey",
    " White",
    " Gold",
    " Silver",
    " None",
)

colors.grid(column=1, row=5)
colors.current()

# about label
Label(
    tab4, text="Color Code Calculator v1.0 \n Developed by Paminda Kalpa Wickramasinghe"
).grid(column=0, row=0, padx=70, pady=150)

# labelframe = LabelFrame(tab4, text="This is a LabelFrame",bg="red")
# labelframe.pack(fill="both", expand="yes")

# quit button
Button(root, text="Quit me", command=root.destroy).grid(column=1, row=0)
root.mainloop()
