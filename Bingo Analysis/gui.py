import random
import tkinter as tk
from tkinter import Button, Label, Entry, Canvas, Frame, Scrollbar, VERTICAL, LEFT, Y, RIGHT, SUNKEN, messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import Bingo  # Import the core Bingo code
import pandas as pd
from turtle import RawTurtle
import turtle

def quit_application():
    root.destroy()

def on_configure(canvas):
    canvas.configure(scrollregion=canvas.bbox('all'))

def validate_positive_int(entry, field_name, min_value, max_value):
    value_str = entry.get()

    # Check if the input is not empty and is numeric
    if value_str.isdigit():
        value = int(value_str)

        # Check if the value is within the specified range
        if min_value <= value <= max_value:
            return value
        else:
            messagebox.showerror("Error", f"{field_name} should be between {min_value} and {max_value}. Please enter a valid positive integer.")
    else:
        messagebox.showerror("Error", f"Please enter a valid positive integer for {field_name}.")

    return None


def clear_entry_fields():
    num_simulations_entry.delete(0, 'end')
    num_cards_per_simulation_entry.delete(0, 'end')

root = tk.Tk()
root.title("Bingo Simulation")
root.geometry("800x800")
root.configure(bg='lightblue')

global_cards = []  # Initialize an empty list to store global cards

def Standarddevplot(num_simulations, num_cards_per_simulation):
    cards = Bingo.plot_graph(num_simulations, num_cards_per_simulation)
    return cards

def Histogramplot():
    Hist_plot = Bingo.Histogramplot()
    return Hist_plot
    # Create a new window to display the graph


def display_initial_cards():
    # Read the generated cards from the CSV file
    cards_df = pd.read_csv('generated_cards.csv')

    # Use the correct column name to access the cards
    global_cards = cards_df['Bingo Cards'].apply(eval).tolist()

    # Create a new window to display initial cards with a scrollable frame
    initial_cards_window = tk.Toplevel(root)
    initial_cards_window.title("Initial Bingo Cards")

    canvas_frame = Frame(initial_cards_window)
    canvas_frame.pack(side=LEFT)

    canvas = Canvas(canvas_frame, width=1200, height=800)
    canvas.pack(side=LEFT, fill=Y)

    scrollbar = Scrollbar(canvas_frame, orient=VERTICAL, command=canvas.yview, width = 20)
    scrollbar.pack(side=RIGHT, fill=Y)

    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.bind('<Configure>', lambda event, canvas=canvas: on_configure(canvas))

    frame = Frame(canvas)
    canvas.create_window((0, 0), window=frame, anchor='nw')

    cards_per_row = 10
    row_height = 150  # Adjust the row height to ensure visibility of the bottom two rows
    card_spacing = 30

    for i, card in enumerate(global_cards):
        column_num = i % cards_per_row
        row_num = i // cards_per_row

        frame_column = column_num * (2 + card_spacing)  # Adding horizontal spacing
        frame_row = row_num * (row_height + card_spacing)  # Adding vertical spacing

        # Add thicker lines around the edge of each player's card
        label = Label(frame, text=f"Player {i + 1}")
        label.grid(row=frame_row + 1, column=frame_column + 1, pady=5, padx=5)

        for row_index, row in enumerate(card):
            row_label = Label(frame, text=' | '.join(map(lambda x: str(x).rjust(2), row)))
            row_label.grid(row=frame_row + row_index * 2 + 3, column=frame_column + 1, pady=2, padx=5)

    initial_cards_window.after(100, lambda: canvas.update_idletasks())
    initial_cards_window.after(200, lambda: canvas.configure(scrollregion=canvas.bbox('all')))


colors = ['blue', 'red', 'yellow', 'orange', 'purple', 'magenta', 'pink', 'lime',
          'green', 'gold', 'silver', 'violet']

def fireworks_animation(t):

    x = random.randint(-200,200)
    y = random.randint(-200,200)
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.color(random.choice(colors))
    d = random.randint(20,100)

    for i in range(36):
        t.forward(d)
        t.backward(d)
        t.right(10)

def start_simulation():
    num_simulations = validate_positive_int(num_simulations_entry, "Number of Simulations", 1, 110)
    num_cards_per_simulation = validate_positive_int(num_cards_per_simulation_entry, "Number of Cards per simulation", 3, 60)

    if num_simulations is not None and num_cards_per_simulation is not None:
        print(f"Number of simulations: {num_simulations}")
        print(f"Number of cards per simulation: {num_cards_per_simulation}")

        # Run Bingo game simulations
        Bingo.main(num_cards_per_simulation, num_simulations)

        display_initial_cards_button = Button(frame, text="Display Initial Cards", command=display_initial_cards,  fg= "white", bg="grey")
        display_initial_cards_button.pack()

        make_graph_button = Button(frame, text="Display Bingo vs Turn Graph", command=lambda: Standarddevplot(num_simulations, num_cards_per_simulation), fg= "white", bg="grey")
        make_graph_button.pack()

        make_hist_button = Button(frame, text="Display Histogram", command=Histogramplot, fg= "white", bg="grey")
        make_hist_button.pack()

        # Tkinter canvas for fireworks
        canvas_for_fireworks = Canvas(frame, width=800, height=500, bg='black')
        canvas_for_fireworks.pack()

        # Turtle canvas for fireworks
        turtle_screen = turtle.TurtleScreen(canvas_for_fireworks)
        turtle_screen.bgcolor('black')

        myturtle = RawTurtle(turtle_screen)
        myturtle.speed(0)
        myturtle.hideturtle()

        for i in range(5):
            fireworks_animation(myturtle)

        myturtle.penup()
        myturtle.goto(0, 100)
        myturtle.color('white')  # Change this to a color that contrasts with the black background
        myturtle.write("Simulation Complete!", align="center", font=("Verdana", 24, "normal"))

        clear_entry_fields()

frame = tk.Frame(root)
frame = tk.Frame(root, bg='light blue')
frame.pack()

num_cards_per_simulation_label = Label(frame, text="Number of Bingo Cards per simulation: (+ve integer, 3-60)",  fg= "white", bg="grey")
num_cards_per_simulation_label.pack()

num_cards_per_simulation_entry = Entry(frame)
num_cards_per_simulation_entry.pack()

num_simulations_label = Label(frame, text="Number of Simulations: (+ve integer, 1-110)",  fg= "white", bg="grey")
num_simulations_label.pack()

num_simulations_entry = Entry(frame)
num_simulations_entry.pack()

start_button = Button(frame, text="Start Simulation", command=start_simulation,  fg= "white", bg="grey")
start_button.pack()

quit_button = Button(frame, text="Quit", command=quit_application,  fg= "white", bg="grey")
quit_button.pack()

root.mainloop()
