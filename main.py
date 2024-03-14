# Import the tkinter module to create the GUI
from tkinter import *


# Function to convert miles to kilometers
def miles_to_km():
	# Get the value entered in the miles_input Entry widget and convert it to a float
	miles = float(miles_input.get())

	# Convert miles to kilometers using the conversion factor (1 mile = 1.609 km) and round the result
	km = round(miles * 1.609)

	# Update the text of the kilometer_result_label with the calculated value
	kilometer_result_label.config(text=f"{km}")


# Create the main window
window = Tk()
window.title("Miles to Kilometer Converter")
window.config(padx=20, pady=20)

# Create an Entry widget for entering miles
miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)

# Create a Label widget to display the text "Miles"
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

# Create a Label widget to display the text "Is equal to"
is_equal_label = Label(text="Is equal to")
is_equal_label.grid(column=0, row=1)

# Create a Label widget to display the calculated kilometers
kilometer_result_label = Label(text="0")
kilometer_result_label.grid(column=1, row=1)

# Create a Label widget to display the text "Km"
kilometer_label = Label(text="Km")
kilometer_label.grid(column=2, row=1)

# Create a Button widget for triggering the miles_to_km function
calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)

# Start the main event loop to run the GUI
window.mainloop()

