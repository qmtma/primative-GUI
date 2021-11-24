import csv
import os.path
import pickle

class book:
    def __init__(self,ISBN, book_title,book_author,year_of_publication,publisher,rating=None,rating_count=None):
        self.ISBN= ISBN
        self.book_title= book_title
        self.book_author = book_author
        self.year_of_publication = year_of_publication
        self.publisher = publisher
        if rating:
            self.rating = rating
        else:self.rating =0
        if rating_count:
            self.rating_count = rating_count
        else:self.rating_count=0
    def __str__(self):
        print(f"books details are ({self.ISBN}, {self.book_title}, {self.book_author}, {self.year_of_publication}, {self.publisher})")
    pass
class Location:

    def __init__(self,user):
        try:
            self.city = user[0]
        except IndexError: self.city = "0"
        try:
            self.state = user[1]
        except IndexError: self.state = "0"
        try: self.country = user[2]
        except IndexError: self.country = "0"
class user:
    def __init__(self, user_id, locate, age):
        self.user_id = user_id
        self.password="0"
        self.address = locate
        self.age= age
        self.reviewed = []
        self.set_password(locate)
    def __str__(self):
        print(f"user details are ({self.user_id}, {self.address}, {self.age})")
    def set_password(self, locate):
        tempObjet =Location(locate)
        try:char1 = tempObjet.city.strip()[0]
        except IndexError: char1="0"
        try:char2 = tempObjet.state.strip()[0]
        except IndexError:char2="0"
        try:char3 =tempObjet.country.strip()[0]
        except IndexError:char3="0"
        password = f"{char1}{char2}{char3}"
        if self.age:
            password+= str(int(float(self.age)))
        else: password += "0"
        self.password=password
class bookdataset:
    def __init__(self):
        self.books=[]
        self.users=[]
        if os.path.exists("book.dat") and os.path.exists("user.dat"):
            self.load_objs()
        else:
            self.store_objs()
    def append_user(self,ID=None, City=None, State=None, Country=None, Age=None):
        locate = [City,State,Country]
        self.books.append(user(ID,locate,Age))
    def append_book(self,ISBN=None, Title=None, Author=None, Year=None, Publisher=None):
        self.books.append(book(ISBN,Title,Author,Year,Publisher))
    def load_books(self):
        temp=[]
        with open("Books.csv", 'r') as csvfile:
            read = csv.reader(csvfile, delimiter=',')
            next(read)
            for line in read:
                var1 = line[0]
                var2 = line[1]
                var3 = line[2]
                var4 = line[3]
                var5 = line[4]
                obj = book(var1, var2, var3, var4, var5)
                temp.append(obj)
        self.books=temp
        pass
    def load_users(self):
        temp = []
        with open("Users.csv", 'r') as csvfile:
            read = csv.reader(csvfile, delimiter=',')
            next(read)
            for line in read:
                var1 = line[0]
                var2 = line[1].split(',')
                var3 = line[2]
                obj = user(var1, var2, var3)
                temp.append(obj)
        self.users = temp
    def init_rating(self):
        with open('Review_small.csv','r') as csvFile:
            read = csv.reader(csvFile, delimiter=',')
            next(read)
            temp =[]
            for line in read:
                for item in self.books:
                    if item.ISBN == line[1]:
                        item.rating_count += 1
                        item.rating = int(line[2])/item.rating_count
                        obj = book(item.ISBN, item.book_title, item.book_author, item.year_of_publication,
                                   item.publisher, item.rating,item.rating_count)
                        temp.append(obj)
            self.books = temp
        pass
    def init_reviewed(self):
        with open("Review_small.csv","r") as csvFile:
            read = csv.reader(csvFile, delimiter=',')
            next(read)
            for line in read:
                for item in self.users:
                    if line[0]== item.user_id:
                        item.reviewed.append(line[1])
    def load_objs(self):
        if os.path.exists("book.dat"):
            with open('book.dat', 'rb') as input:
                obj1 = pickle.load(input)
                self.books= obj1
        if os.path.exists("users.dat"):
            with open('users.dat', 'rb') as input:
                obj1 = pickle.load(input)
                self.users = obj1
    def store_objs(self):
        with open("users.dat", "wb") as writeFile:
            with open("Users.csv", "r") as csvfile:
                read = csv.reader(csvfile, delimiter=',')
                next(read)
                for line in read:
                    var1 = line[0]
                    var2 = line[1].split(',')
                    var3 = line[2]
                    obj = user(var1, var2, var3)
                    self.users.append(obj)
                pickle.dump(self.users, writeFile, pickle.HIGHEST_PROTOCOL)
        with open("Books.csv", 'r') as csvfile:
            with open('book.dat', 'wb') as writeFile:
                read = csv.reader(csvfile, delimiter=',')
                next(read)
                for line in read:
                    var1 = line[0]
                    var2 = line[1]
                    var3 = line[2]
                    var4 = line[3]
                    var5 = line[4]
                    obj = book(var1, var2, var3, var4, var5)
                    self.books.append(obj)
                pickle.dump(self.books, writeFile, pickle.HIGHEST_PROTOCOL)
    def search_books(self, ISBN=None,Title=None,Author=None,Year=None,Publisher=None):
        chcklist = [ISBN, Title, Author, Year, Publisher]
        for item in self.books:
            dictionary = item.__dict__
            thing=list(dictionary.values())
            try:
                thingT = [thing[0], thing[1].strip(), thing[2].strip(), thing[3].strip(), thing[4].strip()]
                if chcklist == thingT:
                    book.__str__(item)
                    print(set(chcklist))
                    print(set(thingT))
                    break
                elif set(chcklist).intersection(set(thingT)):
                    book.__str__(item)
                    continue
            except IndexError:continue
    def search_user(self,ID=None,City=None,State=None,Country=None,Age=None):
        for item in self.users:
            chcklist = [ID, City, State, Country, Age]
            dictionary = item.__dict__
            thing=list(dictionary.values())
            try:
                thingT = [thing[0], thing[2][0].strip(), thing[2][1].strip(), thing[2][2].strip(), thing[3].strip()]
                if chcklist == thingT:
                    user.__str__(item)
                    break
                elif set(chcklist).issubset(set(thingT)):
                    user.__str__(item)
                    continue
            except IndexError: continue
    def sort_books(self, sortingTag):
        if sortingTag == "1":
            self.books.sort(key=lambda x: x.ISBN)
        if sortingTag == "2":
            self.books.sort(key=lambda x: x.book_title)
        if sortingTag == "3":
            self.books.sort(key=lambda x: x.book_author)
        if sortingTag == "4":
            self.books.sort(key=lambda x: x.year_of_publication)
        if sortingTag == "5":
            self.books.sort(key=lambda x: x.publisher)
        if sortingTag == "6":
            self.books.sort(key=lambda x: x.rating)
        if sortingTag == "7":
            self.books.sort(key=lambda x: x.rating_count)
        pass



