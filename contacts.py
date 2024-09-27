from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry('700x750')
root.title('Contact Book')
root.config(bg = '#A0C49D')

contactlist = [
    ['Shriya Soni ', '369854712'],
    ['Mahek Sorathiya', '521155222'],
    ['Deekshita Trivedi', '78945614'],
    ['Parikshit Talaviya', '58745246'],
    ['Vaibhav Soni', '5846975'],
    ['Priyansh Soni', '5647892'],
    ['Sur Vaghasiya', '89685320'],
    ['Sameer Sukhadiya', '98564785'],
    ['Parth Sharma','85967412'],
    ['Saket Soni ','369854712'],
    ['Vikita Sorathiya', '521155222'],
    ['Aarushi Trivedi', '78945614'],
    ['Nishant Talaviya', '58745246'],
    ['Aaryan Soni', '5846975'],
    ['Riya Soni', '5647892'],
    ['Yashvi Vaghasiya', '89685320'],
    ['Sangeeta Sukhadiya', '98564785'],
    ['Diksha Sharma','85967412'],
    ['Raj Talaviya', '58745246'],
    ['Ashok Soni', '5846975'],
    ['Preet Soni', '5647892'],
    ['Vasant Vaghasiya', '89685320'],
    ['Nilesha Soni', '98564785'],
    ['Mahendra Sharma', '85967412']
]

Name = StringVar()
Number = StringVar()

frame = Frame(root)
frame.pack(side=RIGHT)

scroll = Scrollbar(frame, orient=VERTICAL)
select = Listbox(frame, yscrollcommand=scroll.set, font=('Times new roman', 16),bg="#C4D7B2", width=25, height=30, borderwidth=3, relief="groove")
scroll.config(command=select.yview)
scroll.pack(side=RIGHT, fill=Y)

select.pack(side=LEFT, fill=BOTH, expand=1)

def Selected():
	print("hello",len(select.curselection()))
	if len(select.curselection())==0:
		messagebox.showerror("Error", "Please Select the Name")
	else:
		return int(select.curselection()[0])
      
def AddContact():
    if Name.get()!="" and Number.get()!="":
        contactlist.append([Name.get() ,Number.get()])
        print(contactlist)
        Select_set()
        EntryReset()
        messagebox.showinfo("Confirmation", "Successfully Add New Contact")
    else:
        messagebox.showerror("Error","Please fill the information")
    Select_set()

def UpdateDetail():
	if Name.get() and Number.get():
		contactlist[Selected()] = [Name.get(), Number.get()]
		messagebox.showinfo("Confirmation", "Successfully Update Contact")
		EntryReset()
		Select_set()
	elif not(Name.get()) and not(Number.get()) and not(len(select.curselection())==0):
		messagebox.showerror("Error", "Please fill the information")
	else:
		if len(select.curselection())==0:
			messagebox.showerror("Error", "Please Select the Name and \n press Load button")
		else:
			message1 = """To Load the all information of \n 
						  selected row press Load button\n.
						  """   
			messagebox.showerror("Error", message1)
                  
def EntryReset():
	Name.set('')
	Number.set('')
      
def Delete_Entry():
    if len(select.curselection())!=0:
        result=messagebox.askyesno('Confirmation','You Want to Delete Contact\n Which you selected')
        if result==True:
            del contactlist[Selected()]
            Select_set()
    else:
        messagebox.showerror("Error", 'Please select the Contact')

def VIEW():
    NAME, PHONE = contactlist[Selected()]
    Name.set(NAME)
    Number.set(PHONE)

def EXIT():
    root.destroy()

def Select_set():
    contactlist.sort()
    select.delete(0,END)
    for name,phone in contactlist :
        select.insert (END, name)
        
Select_set()
def perform_search():
    query = search.get()
    select.delete(0, "end")
    for name, phone in contactlist:
        if query.lower() in name.lower():
            select.insert("end", name)

Label(root, text='Name', font=("Times new roman", 22, "bold"),bg='#E1ECC8').place(x=30, y=20)
Entry(root, textvariable=Name, width=30).place(x=200, y=30)

Label(root, text='Contact No.', font=("Times new roman", 22, "bold"),bg='#E1ECC8').place(x=30, y=70)
Entry(root, textvariable=Number, width=30).place(x=200, y=80)

Entry(root,  width=30 ).place(x=200, y=140)

Button(root, text="Search", font='Helvetica 18 bold',bg='#E1ECC8',command=perform_search,padx=15).place(x=30, y=130)
Button(root,text=" NEW ", font='Helvetica 18 bold',bg='#E1ECC8', command = AddContact, padx=20). place(x= 30, y=190)
Button(root,text="EDIT", font='Helvetica 18 bold',bg='#E1ECC8',command = UpdateDetail, padx=27).place(x= 230, y=190)
Button(root,text="DELETE", font='Helvetica 18 bold',bg='#E1ECC8',command = Delete_Entry, padx=7).place(x= 30, y=250)
Button(root,text="VIEW", font='Helvetica 18 bold',bg='#E1ECC8', command = VIEW,padx=24).place(x= 30, y=310)
Button(root,text="RESET", font='Helvetica 18 bold',bg='#E1ECC8',command=EntryReset,padx=15).place(x= 230, y=250)
Button(root,text="EXIT", font='Helvetica 18 bold',bg='#E1ECC8', command = EXIT,padx=28).place(x= 230, y=310)
root.mainloop()

