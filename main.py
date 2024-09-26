import tkinter as tk

def on_entry_click(event):
    """Function to handle placeholder text behavior"""
    if entry.get() == 'type here':
        entry.delete(0, "end")  # Clear the placeholder
        entry.config(fg='black')  # Change text color

def on_focusout(event):
    """Function to restore placeholder if entry is empty"""
    if entry.get() == '':
        entry.insert(0, 'type here')  # Restore the placeholder
        entry.config(fg='grey')  # Change text color back to grey

# Create the main window
root = tk.Tk()
root.title("Text Box Example")

# Create an entry (text box) widget
entry = tk.Entry(root, fg='grey')
entry.insert(0, 'type here')  # Add placeholder text
entry.bind('<FocusIn>', on_entry_click)  # Clear placeholder on focus
entry.bind('<FocusOut>', on_focusout)  # Restore placeholder on focus out
entry.pack(padx=20, pady=20)

# Run the main event loop
root.mainloop()
