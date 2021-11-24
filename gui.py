import tkinter
from tkinter import Tk, Label, Button
from tkinter.ttk import Entry
from bookdataset import bookdataset


class programGUI:
    def __init__(self, master, Admin_user, Admin_password):
        self.master = master
        self.Admin_user = Admin_user
        self.Admin_password = Admin_password
        master.title("CMPS 151 Student Book Review")

        self.Login_button = Button(master, text="login", command=self.Login)
        self.Login_button.grid()

        self.AddU_button = Button(master, text="Add User", command=self.AddU, state =tkinter.DISABLED)
        self.AddU_button.grid(row=0, column=1)
        

        self.SearchU_button = Button(master, text="Search Users", command=self.SearchU, state =tkinter.DISABLED)
        self.SearchU_button.grid(row=0, column=2)

        self.AddB_button = Button(master, text="Add Book", command=self.AddBook, state =tkinter.DISABLED)
        self.AddB_button.grid(row=0, column=3)

        self.SearchB_button = Button(master, text="Search Book", command=self.SearchB, state =tkinter.DISABLED)
        self.SearchB_button.grid(row=0, column=4)

        self.SortB_button = Button(master, text="Sort Books", command=self.SortB, state =tkinter.DISABLED)
        self.SortB_button.grid(row=0, column=5)

        self.Quit_button = Button(master, text="Quit", command=master.quit)
        self.Quit_button.grid(row=0, column=6)
    def SortB(self):
        self.sortSelection= tkinter.StringVar()
        self.ISBNsort= tkinter.Radiobutton(self.master, text="ISBN", variable=self.sortSelection, value="1")
        self.ISBNsort.grid(row=1,column=0)
        self.ISBNsort.deselect()

        self.TitleSort = tkinter.Radiobutton(self.master, text="Title", variable=self.sortSelection, value="2")
        self.TitleSort.grid(row=1, column=1)
        self.TitleSort.deselect()

        self.Authorsort = tkinter.Radiobutton(self.master, text="Author" , variable=self.sortSelection, value="3")
        self.Authorsort.grid(row=1, column=2)
        self.Authorsort.deselect()

        self.Yearsort = tkinter.Radiobutton(self.master, text="Year", variable=self.sortSelection, value="4")
        self.Yearsort.grid(row=1, column=3)
        self.Yearsort.deselect()

        self.Publishersort = tkinter.Radiobutton(self.master, text="Publisher", variable=self.sortSelection, value="5")
        self.Publishersort.grid(row=1, column=4)
        self.Publishersort.deselect()

        self.Ratingsort = tkinter.Radiobutton(self.master, text="Rating", variable=self.sortSelection, value="6")
        self.Ratingsort.grid(row=1, column=5)
        self.Ratingsort.deselect()

        self.Ratingcountsort = tkinter.Radiobutton(self.master, text="Rating Count", variable=self.sortSelection, value="7")
        self.Ratingcountsort.grid(row=1, column=6)
        self.Ratingcountsort.deselect()

        self.sortButton = Button(self.master, text="Sort", command=self.sortBooks)
        self.sortButton.grid(row=2, column=2)
        self.cancelsort = Button(self.master, text="cancel", command=self.clearsort)
        self.cancelsort.grid(row=2, column=3)
    def sortBooks(self):
        selection = self.sortSelection.get()
        programOBJ.sort_books(selection)
    def clearsort(self):
        self.sortButton.grid_forget()
        self.cancelsort.grid_forget()
        self.Authorsort.grid_forget()
        self.TitleSort.grid_forget()
        self.Yearsort.grid_forget()
        self.ISBNsort.grid_forget()
        self.Publishersort.grid_forget()
        self.Ratingcountsort.grid_forget()
        self.Ratingsort.grid_forget()
    def SearchB(self):
        self.ISBNLable = Label(self.master, text="ISBN")
        self.ISBNLable.grid(row=1, column=2)
        self.ISBN = tkinter.StringVar()
        self.ISBNEntry = Entry(self.master, textvariable=self.ISBN)
        self.ISBNEntry.grid(row=1, column=3)

        self.TitleLabel = Label(self.master, text="Title")
        self.TitleLabel.grid(row=2, column=2)
        self.Title = tkinter.StringVar()
        self.TitleEntry = Entry(self.master, textvariable=self.Title)
        self.TitleEntry.grid(row=2, column=3)

        self.AuthorLabel = Label(self.master, text="Author")
        self.AuthorLabel.grid(row=3, column=2)
        self.Author = tkinter.StringVar()
        self.AuthorEntry = Entry(self.master, textvariable=self.Author)
        self.AuthorEntry.grid(row=3, column=3)

        self.YearLabel = Label(self.master, text="Year")
        self.YearLabel.grid(row=4, column=2)
        self.Year = tkinter.StringVar()
        self.YearEntry = Entry(self.master, textvariable=self.Year)
        self.YearEntry.grid(row=4, column=3)

        self.PublisherLabel = Label(self.master, text="Publisher")
        self.PublisherLabel.grid(row=5, column=2)
        self.Publisher = tkinter.StringVar()
        self.PublisherEntry = Entry(self.master, textvariable=self.Publisher)
        self.PublisherEntry.grid(row=5, column=3)

        self.SearchingBook = Button(self.master, text="search", command=self.searchB)
        self.SearchingBook.grid(row=6, column=2)
        self.cancelBookSearch = Button(self.master, text="cancel", command=self.clearSearchB)
        self.cancelBookSearch.grid(row=6, column=3)
    def searchB(self):
        if self.ISBN.get():
            ISBN = self.ID.get()
        else: ISBN = ''
        if self.Title.get():
            Title = self.Title.get()
        else: Title= ''
        if self.Author.get():
            Author = self.Author.get()
        else: Author=''
        if self.Year.get():
            Year = self.Year.get()
        else: Year = ''
        if self.Publisher.get():
            Publisher = self.Publisher.get()
        else: Publisher = ''
        programOBJ.search_books(ISBN, Title, Author, Year, Publisher)
        self.ISBNEntry.delete(0, "end")
        self.TitleEntry.delete(0, "end")
        self.AuthorEntry.delete(0, "end")
        self.YearEntry.delete(0, "end")
        self.PublisherEntry.delete(0,"end")
    def clearSearchB(self):
        self.ISBNLable.grid_forget()
        self.ISBNEntry.grid_forget()
        self.AuthorLabel.grid_forget()
        self.AuthorEntry.grid_forget()
        self.TitleLabel.grid_forget()
        self.TitleEntry.grid_forget()
        self.YearEntry.grid_forget()
        self.YearLabel.grid_forget()
        self.cancelBookSearch.grid_forget()
        self.PublisherLabel.grid_forget()
        self.PublisherEntry.grid_forget()
        self.SearchingBook.grid_forget()
    def AddBook(self):
        self.ISBNLable = Label(self.master, text="ISBN")
        self.ISBNLable.grid(row=1, column=2)
        self.ISBN = tkinter.StringVar()
        self.ISBNEntry = Entry(self.master, textvariable=self.ISBN)
        self.ISBNEntry.grid(row=1, column=3)

        self.TitleLabel = Label(self.master, text="Title")
        self.TitleLabel.grid(row=2, column=2)
        self.Title = tkinter.StringVar()
        self.TitleEntry = Entry(self.master, textvariable=self.Title)
        self.TitleEntry.grid(row=2, column=3)

        self.AuthorLabel = Label(self.master, text="Author")
        self.AuthorLabel.grid(row=3, column=2)
        self.Author = tkinter.StringVar()
        self.AuthorEntry = Entry(self.master, textvariable=self.Author)
        self.AuthorEntry.grid(row=3, column=3)

        self.YearLabel = Label(self.master, text="Year")
        self.YearLabel.grid(row=4, column=2)
        self.Year = tkinter.StringVar()
        self.YearEntry = Entry(self.master, textvariable=self.Year)
        self.YearEntry.grid(row=4, column=3)

        self.PublisherLabel = Label(self.master, text="Publisher")
        self.PublisherLabel.grid(row=4, column=2)
        self.Publisher = tkinter.StringVar()
        self.PublisherEntry = Entry(self.master, textvariable=self.Publisher)
        self.PublisherEntry.grid(row=4, column=3)

        self.AddingBook = Button(self.master, text="add", command=self.addB)
        self.AddingBook.grid(row=5, column=2)
        self.cancelAddingBook = Button(self.master, text="cancel", command=self.clearAddB)
        self.cancelAddingBook.grid(row=5, column=3)
    def addB(self):
        ISBN = self.ISBN.get()
        Title = self.Title.get()
        Author = self.Author.get()
        Year = self.Year.get()
        Publisher = self.Publisher.get()
        programOBJ.append_book(ISBN,Title,Author,Year,Publisher)
        self.ISBNEntry.delete(0, "end")
        self.TitleEntry.delete(0, "end")
        self.AuthorEntry.delete(0, "end")
        self.PublisherEntry.delete(0, "end")
        pass
    def clearAddB(self):
        self.ISBNLable.grid_forget()
        self.ISBNEntry.grid_forget()
        self.AuthorLabel.grid_forget()
        self.AuthorEntry.grid_forget()
        self.TitleLabel.grid_forget()
        self.TitleEntry.grid_forget()
        self.YearEntry.grid_forget()
        self.YearLabel.grid_forget()
        self.cancelAddingBook.grid_forget()
        self.PublisherLabel.grid_forget()
        self.PublisherEntry.grid_forget()
        self.AddingBook.grid_forget()
    def SearchU(self):
        self.IDLabel = Label(self.master, text="ID")
        self.IDLabel.grid(row=1, column=2)
        self.ID = tkinter.StringVar()
        self.IDEntry = Entry(self.master, textvariable=self.ID)
        self.IDEntry.grid(row=1, column=3)

        self.CityLabel = Label(self.master, text="City")
        self.CityLabel.grid(row=2, column=2)
        self.City = tkinter.StringVar()
        self.CityEntry = Entry(self.master, textvariable=self.City)
        self.CityEntry.grid(row=2, column=3)

        self.StateLabel = Label(self.master, text="State")
        self.StateLabel.grid(row=3, column=2)
        self.State = tkinter.StringVar()
        self.StateEntry = Entry(self.master, textvariable=self.State)
        self.StateEntry.grid(row=3, column=3)

        self.CountryLabel = Label(self.master, text="Country")
        self.CountryLabel.grid(row=4, column=2)
        self.Country = tkinter.StringVar()
        self.CountryEntry = Entry(self.master, textvariable=self.Country)
        self.CountryEntry.grid(row=4, column=3)

        self.AgeLabel = Label(self.master, text="Age")
        self.AgeLabel.grid(row=5, column=2)
        self.Age = tkinter.StringVar()
        self.AgeEntry = Entry(self.master, textvariable=self.Age)
        self.AgeEntry.grid(row=5, column=3)

        self.SearchUserButton = Button(self.master, text="search", command=self.searchU)
        self.SearchUserButton.grid(row=6,column=2)
        self.cancelUserSearch = Button(self.master, text="cancel", command=self.clearSearchU)
        self.cancelUserSearch.grid(row=6, column=3)
    def searchU(self):
        if self.ID.get():
            ID = self.ID.get()
        else: ID = ''
        if self.City.get():
            City = self.City.get()
        else: City= ''
        if self.State.get():
            State = self.State.get()
        else: State=''
        if self.Country.get():
            Country = self.Country.get()
        else: Country = ''
        if self.Age.get():
            Age = self.Age.get()
        else: Age = ''
        programOBJ.search_user(ID, City, State, Country, Age)
        self.IDEntry.delete(0, "end")
        self.CityEntry.delete(0, "end")
        self.CountryEntry.delete(0, "end")
        self.AgeEntry.delete(0, "end")
        self.StateEntry.delete(0,"end")
    def clearSearchU(self):
        self.CountryEntry.grid_forget()
        self.CountryLabel.grid_forget()
        self.CityEntry.grid_forget()
        self.CityLabel.grid_forget()
        self.StateEntry.grid_forget()
        self.StateLabel.grid_forget()
        self.AgeEntry.grid_forget()
        self.AgeLabel.grid_forget()
        self.cancelUserSearch.grid_forget()
        self.SearchUserButton.grid_forget()
        self.IDEntry.grid_forget()
        self.IDLabel.grid_forget()
    def AddU(self):
        self.IDLabel = Label(self.master, text="ID")
        self.IDLabel.grid(row=1, column=2)
        self.ID = tkinter.StringVar()
        self.IDEntry = Entry(self.master, textvariable=self.ID)
        self.IDEntry.grid(row=1, column=3)

        self.CityLabel= Label(self.master, text="City")
        self.CityLabel.grid(row = 2, column=2)
        self.City= tkinter.StringVar()
        self.CityEntry = Entry(self.master, textvariable=self.City)
        self.CityEntry.grid(row=2, column=3)

        self.StateLabel = Label(self.master, text="State")
        self.StateLabel.grid(row=3, column=2)
        self.State = tkinter.StringVar()
        self.StateEntry = Entry(self.master, textvariable=self.State)
        self.StateEntry.grid(row=3, column=3)

        self.CountryLabel = Label(self.master, text="Country")
        self.CountryLabel.grid(row=4, column=2)
        self.Country = tkinter.StringVar()
        self.CountryEntry = Entry(self.master, textvariable=self.Country)
        self.CountryEntry.grid(row=4, column=3)

        self.AgeLabel = Label(self.master, text="Age")
        self.AgeLabel.grid(row=5, column=2)
        self.Age = tkinter.StringVar()
        self.AgeEntry = Entry(self.master, textvariable=self.Age)
        self.AgeEntry.grid(row=5, column=3)

        self.AddingUser= Button(self.master,text="add", command=self.addU)
        self.AddingUser.grid(row=6, column=2)
        self.cancelAddingUser= Button(self.master,text="cancel",command=self.clearAddU)
        self.cancelAddingUser.grid(row=6, column=3)
        pass
    def addU(self):
        ID = self.ID.get()
        City = self.City.get()
        State = self.State.get()
        Country = self.Country.get()
        Age = self.Age.get()
        programOBJ.append_user(ID,City,State,Country,Age)
        self.IDEntry.delete(0,"end")
        self.CityEntry.delete(0,"end")
        self.CountryEntry.delete(0,"end")
        self.AgeEntry.delete(0,"end")
    def clearAddU(self):
        self.CountryEntry.grid_forget()
        self.CountryLabel.grid_forget()
        self.CityEntry.grid_forget()
        self.CityLabel.grid_forget()
        self.StateEntry.grid_forget()
        self.StateLabel.grid_forget()
        self.AgeEntry.grid_forget()
        self.AgeLabel.grid_forget()
        self.cancelAddingUser.grid_forget()
        self.AddingUser.grid_forget()
        self.IDEntry.grid_forget()
        self.IDLabel.grid_forget()
    def Login(self):
        self.usernameLabel = Label(self.master, text="User Name")
        self.usernameLabel.grid(row=1, column=2)
        self.username = tkinter.StringVar()
        self.usernameEntry = Entry(self.master, textvariable=self.username)
        self.usernameEntry.grid(row=1, column=3)

        self.passwordLabel = Label(self.master, text="Password")
        self.passwordLabel.grid(row=2, column=2)
        self.password = tkinter.StringVar()
        self.passwordEntry = Entry(self.master, textvariable=self.password)
        self.passwordEntry.grid(row=2, column=3)

        self.validate_button = Button(self.master, text= "login", command=self.validate)
        self.validate_button.grid(row =3, column=3)

    def validate(self):
        user = self.username.get()
        password = self.password.get()
        if user == "admin" and password == "123456":
            self.Login_button.config(text="Logout", command= self.Logout)
            self.AddU_button.config(state="normal")
            self.AddB_button.config(state="normal")
            self.SortB_button.config(state="normal")
            self.SearchU_button.config(state="normal")
            self.SearchB_button.config(state="normal")
            self.passwordEntry.grid_forget()
            self.passwordLabel.grid_forget()
            self.usernameEntry.grid_forget()
            self.usernameLabel.grid_forget()
            self.usernameEntry.delete(0, "end")
            self.passwordEntry.delete(0, "end")
            self.validate_button.grid_forget()
        else:
            self.usernameEntry.delete(0, "end")
            self.passwordEntry.delete(0, "end")
    def Logout(self):
        self.Login_button.config(text="login")
        self.AddU_button.config(state="disabled")
        self.AddB_button.config(state="disabled")
        self.SortB_button.config(state="disabled")
        self.SearchU_button.config(state="disabled")
        self.SearchB_button.config(state="disabled")

root = Tk()
programOBJ=bookdataset()
GUI = programGUI(root, "admin" ,"123456" )
root.mainloop()