#Create main window
root = tk.Tk()
root.title("Login Form")
root.geometry("500x200")

#create username label and entry
username_label = tk.label(root, text= "Username:")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()

#create password label and entry
password_label = tk.label(root, text="Password: ")
password_label.pack()
password.entry = tk.entry(root, show= "*")
password_entry.pack()

#create submit button
submit_button = tk.Button(root, text= "Submit", command=submit)
submit_button.pack()

#Run the main event loop
root.mainloop()