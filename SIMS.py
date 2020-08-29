# *************** Show All Function *************** #
def showall():
    dbstr = 'select *from students'
    cur.execute(dbstr)
    data = cur.fetchall()
    std_table.delete(*std_table.get_children())
    for i in data:
        items = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
        std_table.insert('', END, values=items)


# *************** Add Function *************** #
def add():
    def addbtn():
        id = idVAR.get()
        name = nameVAR.get()
        dob = dobVAR.get()
        gender = genderVAR.get()
        mobileNo = mobileNoVAR.get()
        email = emailVAR.get()
        address = addressVAR.get()
        addeddate = time.strftime("%d.%m.%Y")
        addedtime = time.strftime("%I:%M:%S %p")
        if id != '' and name != '' and dob != '' and gender != '' and mobileNo != '' and email != '' and address != '':
            ask = messagebox.askyesno("New Record", "Do you want to add a new record?")
            if ask > 0:
                try:
                    dbstr = 'insert into students values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                    cur.execute(dbstr, (id, addeddate, addedtime, name, dob, gender, mobileNo, email, address))
                    con.commit()
                    res = messagebox.askyesno('Saved', "{}'s Record inserted successfully.".format(name), parent=addroot)
                    if (res == True):
                        idVAR.set('')
                        nameVAR.set('')
                        mobileNoVAR.set('')
                        emailVAR.set('')
                        addressVAR.set('')
                        genderVAR.set('')
                        dobVAR.set('')
                    addroot.destroy()
                except:
                    messagebox.showerror('Error', 'Something went wrong.', parent=addroot)
                showall()
        else:
            messagebox.showerror("Error !", "All fields are required !")
            return


    # *************** Add Toplevel Frame *************** #
    addroot = Toplevel(master=DEFrame)
    addroot.grab_set()
    addroot.geometry('370x480+20+170')
    addroot.title('Add Student')
    addroot.iconbitmap('sims.ico')
    addroot.resizable(0, 0)

    # -------------- AddStudent Labels -------------- #
    idlabel = Label(addroot, text='Id', font=('open sans', 14, 'bold'), relief=FLAT, width=10, anchor='w')
    idlabel.place(x=10, y=10)

    namelabel = Label(addroot, text='Name', font=('open sans', 14, 'bold'), relief=FLAT, width=10, anchor='w')
    namelabel.place(x=10, y=70)

    doblabel = Label(addroot, text='D.O.B', font=('open sans', 14, 'bold'), relief=FLAT, width=10, anchor='w')
    doblabel.place(x=10, y=130)

    genderlabel = Label(addroot, text='Gender', font=('open sans', 14, 'bold'), relief=FLAT, width=10, anchor='w')
    genderlabel.place(x=10, y=190)

    mobilelabel = Label(addroot, text='Mobile No', font=('open sans', 14, 'bold'), relief=FLAT, width=10, anchor='w')
    mobilelabel.place(x=10, y=250)

    emaillabel = Label(addroot, text='Email', font=('open sans', 14, 'bold'), relief=FLAT, width=10, anchor='w')
    emaillabel.place(x=10, y=310)

    addresslabel = Label(addroot, text='Address', font=('open sans', 14, 'bold'), relief=FLAT, width=10, anchor='w')
    addresslabel.place(x=10, y=370)

    # -------------- AddStudent Entries -------------- #
    idVAR = StringVar()
    nameVAR = StringVar()
    mobileNoVAR = StringVar()
    emailVAR = StringVar()
    addressVAR = StringVar()
    genderVAR = StringVar()
    dobVAR = StringVar()

    identry = Entry(addroot, font=('calibri', 14, 'bold'), bd=3, textvariable=idVAR)
    identry.place(x=150, y=10)

    nameentry = Entry(addroot, font=('calibri', 14, 'bold'), bd=3, textvariable=nameVAR)
    nameentry.place(x=150, y=70)

    dobentry = Entry(addroot, font=('calibri', 14, 'bold'), bd=3, textvariable=dobVAR)
    dobentry.place(x=150, y=130)

    genderentry = Entry(addroot, font=('calibri', 14, 'bold'), bd=3, textvariable=genderVAR)
    genderentry.place(x=150, y=190)

    mobileentry = Entry(addroot, font=('calibri', 14, 'bold'), bd=3, textvariable=mobileNoVAR)
    mobileentry.place(x=150, y=250)

    emailentry = Entry(addroot, font=('calibri', 14, 'bold'), bd=3, textvariable=emailVAR)
    emailentry.place(x=150, y=310)

    addressentry = Entry(addroot, font=('calibri', 14, 'bold'), bd=3, textvariable=addressVAR)
    addressentry.place(x=150, y=370)

    # -------------- AddStudent (Submit) Button -------------- #
    submitbtn = Button(addroot, text='Submit', font=('open sans', 12, 'bold'), bg="#BFC9CA", bd=2, width=15,
                       command=addbtn)
    submitbtn.place(x=110, y=425)

    addroot.mainloop()


# *************** Search Function *************** #
def search():
    def searchbtn():
        id = idVAR.get()
        name = nameVAR.get()
        dob = dobVAR.get()
        gender = genderVAR.get()
        mobile = mobileNoVAR.get()
        email = emailVAR.get()
        address = addressVAR.get()
        if id != '' or name != '' or dob != '' or gender != '' or mobile != '' or email != '' or address != '':
            if (id != ''):
                dbstr = 'select *from students where id=%s'
                cur.execute(dbstr, (id))
                data = cur.fetchall()
                std_table.delete(*std_table.get_children())
                for i in data:
                    items = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                    std_table.insert('', END, values=items)
                messagebox.showinfo("Done!", "Search Completed Successfully.")
                searchroot.destroy()
            elif (name != ''):
                dbstr = 'select *from students where name=%s'
                cur.execute(dbstr, (name))
                data = cur.fetchall()
                std_table.delete(*std_table.get_children())
                for i in data:
                    items = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                    std_table.insert('', END, values=items)
                messagebox.showinfo("Done!", "Search Completed Successfully.")
                searchroot.destroy()
            elif (dob != ''):
                dbstr = 'select *from students where dob=%s'
                cur.execute(dbstr, (dob))
                data = cur.fetchall()
                std_table.delete(*std_table.get_children())
                for i in data:
                    items = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                    std_table.insert('', END, values=items)
                messagebox.showinfo("Done!", "Search Completed Successfully.")
                searchroot.destroy()
            elif (gender != ''):
                dbstr = 'select *from students where gender=%s'
                cur.execute(dbstr, (gender))
                data = cur.fetchall()
                std_table.delete(*std_table.get_children())
                for i in data:
                    items = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                    std_table.insert('', END, values=items)
                messagebox.showinfo("Done!", "Search Completed Successfully.")
                searchroot.destroy()
            elif (mobile != ''):
                dbstr = 'select *from students where mobile=%s'
                cur.execute(dbstr, (mobile))
                data = cur.fetchall()
                std_table.delete(*std_table.get_children())
                for i in data:
                    items = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                    std_table.insert('', END, values=items)
                messagebox.showinfo("Done!", "Search Completed Successfully.")
                searchroot.destroy()
            elif (email != ''):
                dbstr = 'select *from students where email=%s'
                cur.execute(dbstr, (email))
                data = cur.fetchall()
                std_table.delete(*std_table.get_children())
                for i in data:
                    items = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                    std_table.insert('', END, values=items)
                messagebox.showinfo("Done!", "Search Completed Successfully.")
                searchroot.destroy()
            elif (address != ''):
                dbstr = 'select *from students where address=%s'
                cur.execute(dbstr, (address))
                data = cur.fetchall()
                std_table.delete(*std_table.get_children())
                for i in data:
                    items = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                    std_table.insert('', END, values=items)
                messagebox.showinfo("Done!", "Search Completed Successfully.")
                searchroot.destroy()
            else:
                searchroot.destroy()
                showall()
        else:
            messagebox.showerror('ERROR', 'Please select at least one filter to see results.')

    # *************** Search Toplevel Frame *************** #
    searchroot = Toplevel(master=DEFrame)
    searchroot.grab_set()
    searchroot.geometry('370x480+20+170')
    searchroot.title('Search Student')
    searchroot.iconbitmap('sims.ico')
    searchroot.resizable(0, 0)

    # -------------- SearchStudent Labels -------------- #
    idlabel = Label(searchroot, text='Id', font=('open sans', 14, 'bold'), relief=FLAT, width=10, anchor='w')
    idlabel.place(x=10, y=10)

    datelabel = Label(searchroot, text='Date', font=('open sans', 14, 'bold'), relief=FLAT, width=10, anchor='w')
    datelabel.place(x=10, y=70)

    namelabel = Label(searchroot, text='Name', font=('open sans', 14, 'bold'), relief=FLAT, width=10, anchor='w')
    namelabel.place(x=10, y=70)

    doblabel = Label(searchroot, text='D.O.B', font=('open sans', 14, 'bold'), relief=FLAT, width=10, anchor='w')
    doblabel.place(x=10, y=130)

    genderlabel = Label(searchroot, text='Gender', font=('open sans', 14, 'bold'), relief=FLAT, width=10, anchor='w')
    genderlabel.place(x=10, y=190)

    mobilelabel = Label(searchroot, text='Mobile', font=('open sans', 14, 'bold'), relief=FLAT, width=10, anchor='w')
    mobilelabel.place(x=10, y=250)

    emaillabel = Label(searchroot, text='Email', font=('open sans', 14, 'bold'), relief=FLAT, width=10, anchor='w')
    emaillabel.place(x=10, y=310)

    addresslabel = Label(searchroot, text='Address', font=('open sans', 14, 'bold'), relief=FLAT, width=10, anchor='w')
    addresslabel.place(x=10, y=370)

    # -------------- SearchStudent Entries -------------- #
    idVAR = StringVar()
    nameVAR = StringVar()
    dobVAR = StringVar()
    genderVAR = StringVar()
    mobileNoVAR = StringVar()
    emailVAR = StringVar()
    addressVAR = StringVar()

    identry = Entry(searchroot, font=('calibri', 14, 'bold'), bd=3, textvariable=idVAR)
    identry.place(x=150, y=10)

    nameentry = Entry(searchroot, font=('calibri', 14, 'bold'), bd=3, textvariable=nameVAR)
    nameentry.place(x=150, y=70)

    dobentry = Entry(searchroot, font=('calibri', 14, 'bold'), bd=3, textvariable=dobVAR)
    dobentry.place(x=150, y=130)

    genderentry = Entry(searchroot, font=('calibri', 14, 'bold'), bd=3, textvariable=genderVAR)
    genderentry.place(x=150, y=190)

    mobileentry = Entry(searchroot, font=('calibri', 14, 'bold'), bd=3, textvariable=mobileNoVAR)
    mobileentry.place(x=150, y=250)

    emailentry = Entry(searchroot, font=('calibri', 14, 'bold'), bd=3, textvariable=emailVAR)
    emailentry.place(x=150, y=310)

    addressentry = Entry(searchroot, font=('calibri', 14, 'bold'), bd=3, textvariable=addressVAR)
    addressentry.place(x=150, y=370)


    # -------------- SearchStudent (Submit) Button) -------------- #
    submitbtn = Button(searchroot, text='Search', font=('open sans', 12, 'bold'), bg="#BFC9CA", bd=2, width=15,
                       command=searchbtn)
    submitbtn.place(x=110, y=425)

    searchroot.mainloop()


# *************** Delete Function *************** #
def delete():
    row = std_table.focus()
    content = std_table.item(row)
    # print(content)
    id_location = content['values'][0]
    name_location = content['values'][3]
    ask = messagebox.askyesno("Delete", "Do you want to delete {}'s record?".format(name_location))
    if ask > 0:
        dbstr = 'delete from students where id=%s'
        cur.execute(dbstr, (id_location))
        con.commit()
        messagebox.showinfo('Deleted', "{}'s Record Deleted Successfully.".format(name_location))
        showall()
    else:
        return


# *************** Update Function *************** #
def update():
    def updatebtn():
        id = idVAR.get()
        name = nameVAR.get()
        dob = dobVAR.get()
        gender = genderVAR.get()
        mobile = mobileVAR.get()
        email = emailVAR.get()
        address = addressVAR.get()
        if id == '' or name == '' or dob == '' or gender == '' or mobile == '' or email == '' or address == '':
            messagebox.showerror('ERROR', 'Please select a record to update.')
        else:
            ask = messagebox.askyesno("Update", "Do you want to update {}'s record?".format(name))
            if ask > 0:
                dbstr = 'update students set name=%s, dob=%s, gender=%s, mobile=%s, email=%s, address=%s where id=%s'
                cur.execute(dbstr, (name, dob, gender, mobile, email, address, id))
                con.commit()
                messagebox.showinfo('Updated', "{}'s Record Updated Successfully.".format(name), parent=updateroot)
                updateroot.destroy()
                showall()
            else:
                return


    # *************** Update Toplevel Frame *************** #
    updateroot = Toplevel(master=DEFrame)
    updateroot.grab_set()
    updateroot.geometry('370x480+20+170')
    updateroot.title('Update Student')
    updateroot.iconbitmap('sims.ico')
    updateroot.resizable(0, 0)

    # -------------- UpdateStudent Labels -------------- #
    idlabel = Label(updateroot, text='Id', font=('open sans', 14, 'bold'), relief=FLAT, width=10, anchor='w')
    idlabel.place(x=10, y=10)

    namelabel = Label(updateroot, text='Name', font=('open sans', 14, 'bold'), relief=FLAT, width=10, anchor='w')
    namelabel.place(x=10, y=70)

    doblabel = Label(updateroot, text='D.O.B', font=('open sans', 14, 'bold'), relief=FLAT, width=10, anchor='w')
    doblabel.place(x=10, y=130)

    genderlabel = Label(updateroot, text='Gender', font=('open sans', 14, 'bold'), relief=FLAT, width=10, anchor='w')
    genderlabel.place(x=10, y=190)

    mobilelabel = Label(updateroot, text='Mobile', font=('open sans', 14, 'bold'), relief=FLAT, width=10, anchor='w')
    mobilelabel.place(x=10, y=250)

    emaillabel = Label(updateroot, text='Email', font=('open sans', 14, 'bold'), relief=FLAT, width=10, anchor='w')
    emaillabel.place(x=10, y=310)

    addresslabel = Label(updateroot, text='Address', font=('open sans', 14, 'bold'), relief=FLAT, width=10, anchor='w')
    addresslabel.place(x=10, y=370)


    # -------------- UpdateStudent Entries -------------- #
    idVAR = StringVar()
    nameVAR = StringVar()
    dobVAR = StringVar()
    genderVAR = StringVar()
    mobileVAR = StringVar()
    emailVAR = StringVar()
    addressVAR = StringVar()

    identry = Entry(updateroot, font=('calibri', 14, 'bold'), bd=3, textvariable=idVAR)
    identry.place(x=150, y=10)

    nameentry = Entry(updateroot, font=('calibri', 14, 'bold'), bd=3, textvariable=nameVAR)
    nameentry.place(x=150, y=70)

    dobentry = Entry(updateroot, font=('calibri', 14, 'bold'), bd=3, textvariable=dobVAR)
    dobentry.place(x=150, y=130)

    genderentry = Entry(updateroot, font=('calibri', 14, 'bold'), bd=3, textvariable=genderVAR)
    genderentry.place(x=150, y=190)

    mobileentry = Entry(updateroot, font=('calibri', 14, 'bold'), bd=3, textvariable=mobileVAR)
    mobileentry.place(x=150, y=250)

    emailentry = Entry(updateroot, font=('calibri', 14, 'bold'), bd=3, textvariable=emailVAR)
    emailentry.place(x=150, y=310)

    addressentry = Entry(updateroot, font=('calibri', 14, 'bold'), bd=3, textvariable=addressVAR)
    addressentry.place(x=150, y=370)

    # -------------- UpdateStudent (Submit) Buttons-------------- #
    submitbtn = Button(updateroot, text='Update', font=('open sans', 12, 'bold'), bg="#BFC9CA", bd=2, width=15,
                       command=updatebtn)
    submitbtn.place(x=110, y=425)

    # -------------- Focus & Fetch -------------- #
    row = std_table.focus()
    content = std_table.item(row)
    pos = content['values']
    if (len(pos) != 0):
        idVAR.set(pos[0])
        nameVAR.set(pos[3])
        dobVAR.set(pos[4])
        genderVAR.set(pos[5])
        mobileVAR.set(pos[6])
        emailVAR.set(pos[7])
        addressVAR.set(pos[8])

    updateroot.mainloop()


# *************** Export Function *************** #
def export():
    file_location = filedialog.asksaveasfilename()
    data = std_table.get_children()
    id, addeddate, addedtime, name, dob, gender, mobile, email, address = [], [], [], [], [], [], [], [], []
    for i in data:
        content = std_table.item(i)
        pos = content['values']
        id.append(pos[0]), addeddate.append(pos[1]), addedtime.append(pos[2]), name.append(pos[3]), dob.append(pos[4]), gender.append(pos[5]), mobile.append(pos[6]), email.append(pos[7]), address.append(pos[8])
    headings = ['Id', 'Added Date', 'Added Time', 'Name', 'D.O.B', 'Gender', 'Mobile', 'Email', 'Address']
    df = pandas.DataFrame(list(zip(id, addeddate, addedtime, name, dob, gender, mobile, email, address)), columns=headings)
    paths = r'{}.csv'.format(file_location)
    df.to_csv(paths, index=False)
    messagebox.showinfo('EXPORTED', "Student's Information are Saved at {}".format(paths))


# *************** Exit Function *************** #
def exitstudent():
    ask = messagebox.askyesno("Exit", "Are you sure?")
    if ask > 0:
        root.destroy()


# *************** Connect To Database *************** #
def connectdb():
    def submitdb():
        global con, cur
        host = hostnameVAR.get()
        user = usernameVAR.get()
        password = passwordVAR.get()
        if host == '' or user == '' or password == '':
            messagebox.showerror('ERROR', 'All fields are required !', parent=dbroot)
        else:
            try:
                con = pymysql.connect(host=host, user=user, password=password)
                cur = con.cursor()
            except:
                messagebox.showerror('ERROR', 'Incorrect Database Details.', parent=dbroot)
                return
            try:
                dbstr = 'create database sims'
                cur.execute(dbstr)
                dbstr = 'use sims'
                cur.execute(dbstr)
                dbstr = 'create table students(id int(10), date varchar(20), time varchar(20), name varchar(30), dob varchar(20), gender varchar(20), mobile varchar(20), email varchar(30), address varchar(100))'
                cur.execute(dbstr)
                dbstr = 'alter table students modify column id int not null'
                cur.execute(dbstr)
                dbstr = 'alter table students modify column id int primary key'
                cur.execute(dbstr)
                messagebox.showinfo('Database', 'Database Created Successfully. \nYou are connected to the Database.', parent=dbroot)
            except:
                dbstr = 'use sims'
                cur.execute(dbstr)
                messagebox.showinfo('Database', 'You are connected to the Database.', parent=dbroot)
            dbroot.destroy()

    # *************** ConnectToDatabase Toplevel Frame *************** #
    dbroot = Toplevel()
    dbroot.title('Connect to Database')
    dbroot.grab_set()  # To grab this window on screen
    dbroot.geometry('390x180+935+150')
    dbroot.iconbitmap('sims.ico')
    dbroot.resizable(0, 0)

    # -------------- Connectdb Labels -------------- #
    hostlabel = Label(dbroot, text="Hostname", font=('open sans', 14, 'bold'), relief=FLAT, width=10, anchor='w')
    hostlabel.place(x=10, y=10)

    userlabel = Label(dbroot, text="Username", font=('open sans', 14, 'bold'), relief=FLAT, width=10, anchor='w')
    userlabel.place(x=10, y=50)

    passwordlabel = Label(dbroot, text="Password", font=('open sans', 14, 'bold'), relief=FLAT, width=10, anchor='w')
    passwordlabel.place(x=10, y=90)

    # -------------- Connectdb Entry -------------- #
    hostnameVAR = StringVar()
    usernameVAR = StringVar()
    passwordVAR = StringVar()

    hostentry = Entry(dbroot, font=('calibri', 14, 'bold'), bd=3, textvariable=hostnameVAR)
    hostentry.place(x=150, y=10)

    userentry = Entry(dbroot, font=('calibri', 14, 'bold'), bd=3, textvariable=usernameVAR)
    userentry.place(x=150, y=50)

    passwordentry = Entry(dbroot, font=('calibri', 14, 'bold'), bd=3, show="*", textvariable=passwordVAR)
    passwordentry.place(x=150, y=90)

    # -------------- Connectdb button -------------- #
    submitbutton = Button(dbroot, text='Connect', font=('open sans', 12, 'bold'), bg="#BFC9CA", bd=2, width=10,
                          command=submitdb)
    submitbutton.place(x=135, y=130)

    dbroot.mainloop()


# *************** Clock *************** #
def set_clock():
    date_string = time.strftime("%d.%m.%Y")
    time_string = time.strftime("%I:%M:%S %p")
    clock.config(text='DATE: ' + date_string + "\n" + "TIME: " + time_string)
    clock.after(200, set_clock)


# *************** Intro Slider *************** #
colors = ['black', 'white', 'black', 'black']
def intro_slider():
    fg = random.choice(colors)
    SliderLabel.config(fg=fg)
    SliderLabel.after(2, intro_slider)


def intro_label():
    global count, text
    if count >= len(str):
        count = 0
        text = ''
        SliderLabel.config(text=text)
    else:
        text = text + str[count]
        SliderLabel.config(text=text)
        count += 1
    SliderLabel.after(200, intro_label)


# *************** Initially *************** #
from tkinter import *
from tkinter import Toplevel, messagebox, filedialog
from tkinter.ttk import Treeview
from tkinter import ttk
import pandas
import pymysql
import time
import random

root = Tk()
root.title('Student Information Management System')
root.geometry("1350x700+0+0")
root.iconbitmap('sims.ico')
root.resizable(0, 0)

# *************** Data Entry Frame *************** #
DEFrame = Frame(root, relief=GROOVE, borderwidth=5)
DEFrame.place(x=10, y=80, width=390, height=580)

frontlabel = Label(DEFrame, text="Administration Panel", width=30, font=('open sans', 25, 'bold'))
frontlabel.pack(side=TOP, expand=True)

showallbtn = Button(DEFrame, text='Show All', width=20, font=('verdana', 15), bd=3, bg="#7DCEA0", fg="black",
                    relief='flat', command=showall)
showallbtn.pack(side=TOP, expand=True)

addbtn = Button(DEFrame, text='Add New Student', width=20, font=('verdana', 15), bd=3, bg="#BFC9CA", fg="black",
                relief='flat', command=add)
addbtn.pack(side=TOP, expand=True)

searchbtn = Button(DEFrame, text='Search', width=20, font=('verdana', 15), bd=3, bg="#BFC9CA", fg="black",
                   relief='flat', command=search)
searchbtn.pack(side=TOP, expand=True)

deletebtn = Button(DEFrame, text='Delete', width=20, font=('verdana', 15), bd=3, bg="#BFC9CA", fg="black",
                   relief='flat', command=delete)
deletebtn.pack(side=TOP, expand=True)

updatebtn = Button(DEFrame, text='Update', width=20, font=('verdana', 15), bd=3, bg="#BFC9CA", fg="black",
                   relief='flat', command=update)
updatebtn.pack(side=TOP, expand=True)

exportbtn = Button(DEFrame, text='Export Data', width=20, font=('verdana', 15), bd=3, bg="#BFC9CA", fg="black",
                   relief='flat', command=export)
exportbtn.pack(side=TOP, expand=True)

exitbtn = Button(DEFrame, text='Exit', width=20, font=('verdana', 15), bd=3, bg="#BFC9CA", fg="black", relief='flat',
                 command=exitstudent)
exitbtn.pack(side=TOP, expand=True)


# *************** Show Data Frame *************** #
ShowDataFrame = Frame(root, relief=GROOVE, borderwidth=5)
ShowDataFrame.place(x=410, y=80, width=940, height=580)

style = ttk.Style()
style.configure('Treeview.Heading', font=('arial', 12, 'bold'), justify='center')
style.configure('Treeview', font=('arial', 12), justify='center')
scroll_x = Scrollbar(ShowDataFrame, orient=HORIZONTAL)
scroll_y = Scrollbar(ShowDataFrame, orient=VERTICAL)
std_table = Treeview(ShowDataFrame, columns=(
'Id', 'Added Date', 'Added Time', 'Name', 'D.O.B', 'Gender', 'Mobile No', 'Email', 'Address'),
                     yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
scroll_x.pack(side=BOTTOM, fill=X)
scroll_y.pack(side=RIGHT, fill=Y)
scroll_x.config(command=std_table.xview)
scroll_y.config(command=std_table.yview)
std_table.heading('Id', text='Id')
std_table.heading('Added Date', text='Added Date')
std_table.heading('Added Time', text='Added Time')
std_table.heading('Name', text='Name')
std_table.heading('D.O.B', text='D.O.B')
std_table.heading('Gender', text='Gender')
std_table.heading('Mobile No', text='Mobile No')
std_table.heading('Email', text='Email')
std_table.heading('Address', text='Address')
std_table['show'] = 'headings'
std_table.column('Id', width=70)
std_table.column('Added Date', width=100)
std_table.column('Added Time', width=100)
std_table.column('Name', width=150)
std_table.column('D.O.B', width=90)
std_table.column('Gender', width=80)
std_table.column('Mobile No', width=100)
std_table.column('Email', width=230)
std_table.column('Address', width=230)
std_table.pack(fill=BOTH, expand=1)

# *************** Clock *************** #
clock = Label(root, font=('open sans', 9, 'bold'), relief=RIDGE, borderwidth=2, width=20, bg='lightgrey')
clock.place(x=0, y=10)
set_clock()

# *************** Slider *************** #
str = 'Welcome to STUDENT INFORMATION MANAGEMENT SYSTEM'
count = 0
text = ''

SliderLabel = Label(root, text=str, font=('open sans', 18, 'bold'), relief=SOLID, borderwidth=3, width=55,
                    bg='lightgrey')
SliderLabel.place(x=240, y=10)
intro_label()
intro_slider()

# *************** Connect Database Button *************** #
connectbutton = Button(root, text='Connect to Database', width=18, font=('open sans', 13, 'bold'), relief=RIDGE,
                       borderwidth=2, bg='lightgrey', command=connectdb)
connectbutton.place(x=1140, y=10)

root.mainloop()
