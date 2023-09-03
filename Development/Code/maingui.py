from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb
import os
from PIL import ImageTk,Image










# Create the main application window
main_gui = tb.Window(themename="superhero")
main_gui.geometry("2560x1600")
main_gui.title("Exercise Planner")

# Load and display the exercise image
image = Image.open("image.png")
resized_image = image.resize((400, 500))
tk_image = ImageTk.PhotoImage(resized_image)
label = Label(main_gui, image=tk_image)
label.place(x=1, y=1)

# Create the first Treeview widget (tree) and define columns for the Treeview widgets
columns = ("Exercise", "Sets", "Reps")
tree = tb.Treeview(main_gui, columns=columns, show="headings", height=10)
tree.place(x=410, y=30)

tree.heading("Exercise", text="Exercise")
tree.heading("Sets", text="Sets")
tree.heading("Reps", text="Reps")

def triceps_add():
    """
    Clears all the items from the tree view and adds predefined items.

    :param None
    :return: None
    """
    tree.delete(*tree.get_children())  

    items_to_add = [
        ("Press Down", "3", "10"),
        ("Shoulder Press", "4", "10"),
        ("Closed Grip Bench Press", "2", "8")
    ]

    for item in items_to_add:
        tree.insert("", "end", values=item)

def biceps_add():
    """
    Clears all existing items in the tree.
    Adds the following items to the tree:
        - "Hammer Curl" with 3 sets of 10 reps
        - "Incline Bicep Curl" with 3 sets of 12 reps
        - "Barbell Curl" with 3 sets of 8 reps
    """
    tree.delete(*tree.get_children())  

    items_to_add = [
        ("Hammer Curl", "3", "10"),
        ("Incline Bicep Curl", "3", "12"),
        ("Barbell Curl", "3", "8")
    ]

    for item in items_to_add:
        tree.insert("", "end", values=item)

def legs_add():
    """
    Deletes all the items in the treeview widget.
    
    Adds a list of items to the treeview widget.
    The list is in the form of a tuple with three elements:
    - The name of the exercise.
    - The number of sets.
    - The number of reps.
    
    Parameters:
        None
        
    Returns:
        None
    """
    tree.delete(*tree.get_children())  

    items_to_add = [
        ("Back Squats", "3", "10"),
        ("Calf Raises", "3", "15"),
        ("Hip Thrusts", "3", "8")
    ]

    for item in items_to_add:
        tree.insert("", "end", values=item)

def back_add():
    """
    Clears all the items in the tree and adds new items to it.

    Parameters:
    None

    Returns:
    None
    """
    tree.delete(*tree.get_children())  

    items_to_add = [
        ("Lat pulldown", "3", "10"),
        ("Deadlift", "3", "6"),
        ("Barbell Row", "3", "8")
    ]

    for item in items_to_add:
        tree.insert("", "end", values=item)

def abs_add():
    """
    Clears all the items in the tree.
    Adds a list of items to the tree.
    """
    tree.delete(*tree.get_children())  

    items_to_add = [
        ("Knee to Elbow Crunch", "3", "10"),
        ("Sit Ups", "3", "10"),
        ("Elbow Plank", "3", "10")
    ]

    for item in items_to_add:
        tree.insert("", "end", values=item)

def chest_add():
    """
    Clears the contents of the treeview widget and adds a set of predefined items to it.

    Parameters:
        None

    Returns:
        None
    """
    tree.delete(*tree.get_children())  

    items_to_add = [
        ("Bench Press", "3", "10"),
        ("Inclined Press", "3", "10"),
        ("Chest Dips", "2", "8")
    ]

    for item in items_to_add:
        tree.insert("", "end", values=item)

def shoulders_add():
    """
    Clear the existing items in the tree.

    Add new items to the tree with the following values:
        - "Shoulder Press" with 3 sets and 10 reps
        - "Seated Raises" with 3 sets and 10 reps
        - "Lateral Raise" with 3 sets and 10 reps
    """
    tree.delete(*tree.get_children())  

    items_to_add = [
        ("Shoulder Press", "3", "10"),
        ("Seated Raises", "3", "10"),
        ("Lateral Raise", "3", "10")
    ]

    for item in items_to_add:
        tree.insert("", "end", values=item)

# Create buttons to add exercises and associate them with corresponding functions
triceps = tb.Button(bootstyle="success", text="Triceps", command=triceps_add)
triceps.place(x=0, y=550)
biceps = tb.Button(bootstyle="success", text="Biceps", command=biceps_add)
biceps.place(x=80, y=550)
legs = tb.Button(bootstyle="success", text="Legs", command=legs_add)
legs.place(x=155, y=550)
back = tb.Button(bootstyle="success", text="Back", command=back_add)
back.place(x=220, y=550)
abs = tb.Button(bootstyle="success", text="Abs", command=abs_add)
abs.place(x=285, y=550)
chest = tb.Button(bootstyle="success", text="Chest", command=chest_add)
chest.place(x=345, y=550)
shoulders = tb.Button(bootstyle="success", text="Shoulders", command=shoulders_add)
shoulders.place(x=415, y=550)

# Create the second Treeview widget (tree2) and define columns for the Treeview widgets
tree2 = tb.Treeview(main_gui, columns=columns, show="headings", height=10)
tree2.place(x=800, y=400)

tree2.heading("Exercise", text="Exercise")
tree2.heading("Sets", text="Sets")
tree2.heading("Reps", text="Reps")

def add_selected_item():
    """
    A function that adds the selected item from a treeview widget to another treeview widget.

    Returns:
    None

    Parameters:
    None
    """
    selected_item = tree.selection()
    if selected_item:
        values = tree.item(selected_item, "values")
        tree2.insert("", "end", values=values)

# Create a button to add selected exercises
add_button = tb.Button(main_gui, text="Add Selected Item", command=add_selected_item)
add_button.place(x=630, y=250)

calendar = tb.DateEntry(main_gui)
calendar.place(x=1200, y=10)

def clear_items():
    """
    Clear all items in the treeview widget.
    """
    tree2.delete(*tree2.get_children())

# Create a DateEntry widget for selecting a date
clear_button = tb.Button(main_gui, text="Clear Items", command=clear_items)
clear_button.place(x=1310, y=610)

# Create labels to indicate the purpose of Treeviews and other sections
tb.Label(text="Listed Exercises").place(x=640, y=5)
tb.Label(text="Today's Exercises").place(x=1050, y=375)

# Create a Meter widget to visualize completion progress
meter = tb.Meter(
    metersize=180,
    padding=5,
    amountused=0,
    metertype="semi",
    subtext="Percent Completed",
    interactive=True,
)
meter.place(x=1050, y=600)





main_gui.mainloop()