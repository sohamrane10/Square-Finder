# Square-Finder
# Description
This is a simple Python-based GUI application created using Tkinter. The application allows users to input a number, and upon clicking the "Find Square" button, it calculates and displays the square of the entered number. If the input is invalid (non-numeric), the app gracefully handles the error by showing an appropriate message.

# Features
- Graphical User Interface (GUI): Created using the Tkinter library, making it simple and user-friendly.
- Real-time square calculation: The user enters a number, and the square is calculated and displayed instantly.
- Error Handling: If a non-numeric value is entered, the app shows a helpful error message instead of crashing.
- Responsive Design: The app uses the Arial font in bold with adjustable sizes, and the layout is neatly spaced for better user experience.

# How to Use
Run the Python script.
Enter any number in the input field.
Click on the "Find Square" button.
The square of the entered number will be displayed below the button.
If a non-numeric value is entered, an error message will appear.

# Code Explanation
- Tkinter Library: The GUI is built using the Tkinter library, which is included with Python. Tkinter provides an easy way to create windows, buttons, input fields, and labels.

# Components:
- Entry: Allows the user to input a number.
- Label: Displays static text like "Enter Number" and dynamic output such as the square or error message.
- Button: Clicking this button triggers the function to calculate the square.

# Error Handling:
A try-except block is used to catch invalid inputs, such as non-numeric values. If the input is not a valid number, an error message is shown to the user instead of causing the program to crash.

# Installation
Install Python (if not already installed): Python Download
Install Tkinter (comes pre-installed with Python on most systems).
Download the square_finder.py file.
Run the script:
bash
Copy code
# python square_finder.py
