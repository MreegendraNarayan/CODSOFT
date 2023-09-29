import tkinter as tk
from tkinter import messagebox

contacts = {}
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()
    if name:
        contacts[name] = {'Phone': phone, 'Email': email, 'Address': address}
        update_contact_list()
        clear_fields()
    else:
        messagebox.showwarning("Warning", "Please enter a name.")

def view_contacts():
    contact_list.delete(0, tk.END)
    for name, info in contacts.items():
        contact_list.insert(tk.END, f"Name: {name}, Phone: {info['Phone']}")

def search_contact():
    search_term = search_entry.get().lower()
    contact_list.delete(0, tk.END)
    for name, info in contacts.items():
        if search_term in name.lower() or search_term in info['Phone']:
            contact_list.insert(tk.END, f"Name: {name}, Phone: {info['Phone']}")

def update_contact():
    selected_contact = contact_list.curselection()
    if selected_contact:
        selected_contact = selected_contact[0]
        contact_info = contact_list.get(selected_contact)
        name = contact_info.split(',')[0].split(': ')[1]
        if name in contacts:
            update_window = tk.Toplevel(root)
            update_window.title("Update Contact")
           
            name_label = tk.Label(update_window, text="Name:")
            name_label.grid(row=0, column=0)
            name_entry_update = tk.Entry(update_window)
            name_entry_update.grid(row=0, column=1)
            name_entry_update.insert(tk.END, name)
           
            phone_label = tk.Label(update_window, text="Phone:")
            phone_label.grid(row=1, column=0)
            phone_entry_update = tk.Entry(update_window)
            phone_entry_update.grid(row=1, column=1)
            phone_entry_update.insert(tk.END, contacts[name]['Phone'])
           
            email_label = tk.Label(update_window, text="Email:")
            email_label.grid(row=2, column=0)
            email_entry_update = tk.Entry(update_window)
            email_entry_update.grid(row=2, column=1)
            email_entry_update.insert(tk.END, contacts[name]['Email'])
           
            address_label = tk.Label(update_window, text="Address:")
            address_label.grid(row=3, column=0)
            address_entry_update = tk.Entry(update_window)
            address_entry_update.grid(row=3, column=1)
            address_entry_update.insert(tk.END, contacts[name]['Address'])
           
            def save_update():
                updated_name = name_entry_update.get()
                updated_phone = phone_entry_update.get()
                updated_email = email_entry_update.get()
                updated_address = address_entry_update.get()
                contacts.pop(name)
                contacts[updated_name] = {'Phone': updated_phone, 'Email': updated_email, 'Address': updated_address}
                update_contact_list()
                update_window.destroy()
               
            update_button = tk.Button(update_window, text="Update", command=save_update)
            update_button.grid(row=4, columnspan=2)
        else:
            messagebox.showwarning("Warning", "Contact not found.")
    else:
        messagebox.showwarning("Warning", "Please select a contact to update.")

def delete_contact():
    selected_contact = contact_list.curselection()
    if selected_contact:
        selected_contact = selected_contact[0]
        contact_info = contact_list.get(selected_contact)
        name = contact_info.split(',')[0].split(': ')[1]
        response = messagebox.askyesno("Confirm Deletion", f"Do you want to delete {name}?")
        if response == tk.YES:
            contacts.pop(name)
            update_contact_list()
    else:
        messagebox.showwarning("Warning", "Please select a contact to delete.")

def clear_fields():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

def update_contact_list():
    view_contacts()
    clear_fields()
root = tk.Tk()
root.title("Contact Manager")

input_frame = tk.Frame(root)
input_frame.grid(row=0, column=0, padx=10, pady=10)

contact_frame = tk.Frame(root)
contact_frame.grid(row=0, column=1, padx=10, pady=10)

name_label = tk.Label(input_frame, text="Name:")
name_label.grid(row=0, column=0, sticky="w")
name_entry = tk.Entry(input_frame)
name_entry.grid(row=0, column=1, padx=5, pady=5)

phone_label = tk.Label(input_frame, text="Phone:")
phone_label.grid(row=1, column=0, sticky="w")
phone_entry = tk.Entry(input_frame)
phone_entry.grid(row=1, column=1, padx=5, pady=5)

email_label = tk.Label(input_frame, text="Email:")
email_label.grid(row=2, column=0, sticky="w")
email_entry = tk.Entry(input_frame)
email_entry.grid(row=2, column=1, padx=5, pady=5)

address_label = tk.Label(input_frame, text="Address:")
address_label.grid(row=3, column=0, sticky="w")
address_entry = tk.Entry(input_frame)
address_entry.grid(row=3, column=1, padx=5, pady=5)

add_button = tk.Button(input_frame, text="Add Contact", command=add_contact)
add_button.grid(row=4, columnspan=2, pady=10)

view_button = tk.Button(input_frame, text="View Contacts", command=view_contacts)
view_button.grid(row=5, columnspan=2, pady=10)

search_label = tk.Label(contact_frame, text="Search:")
search_label.grid(row=0, column=0, padx=5, pady=5)
search_entry = tk.Entry(contact_frame)
search_entry.grid(row=0, column=1, padx=5, pady=5)
search_button = tk.Button(contact_frame, text="Search", command=search_contact)
search_button.grid(row=0, column=2, padx=5, pady=5)

contact_list = tk.Listbox(contact_frame, width=40, height=15)
contact_list.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

update_button = tk.Button(contact_frame, text="Update", command=update_contact)
update_button.grid(row=2, column=0, padx=5, pady=5)

delete_button = tk.Button(contact_frame, text="Delete", command=delete_contact)
delete_button.grid(row=2,column=1,padx=5,pady=5)

root.mainloop()