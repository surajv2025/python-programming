import csv
import os


class Book:
    def __init__(self,bid, name, author, price):
        self.bid = bid
        self.title = name
        self.author = author
        self.price = price
        self.is_issue = False  # book kisi member ko issue hui hai ya nahi
        self.isAlive = True    # book library me available hai ya delete ho chuki hai

    def show(self):
        print("Book ID:", self.bid)
        print("Book Title:", self.title)
        print("Book Author:", self.author)
        print("Book Price:", self.price)
        print("Is Issued:", self.is_issue)


class Member:
    def __init__(self, mid, name,phno):
        self.mid = mid
        self.name = name
        self.phno = phno
        self.isAlive=True  # member active hai ya remove ho chuka hai

        self.lib_card={}  
        # dictionary me member ki issued books store hongi
        
        # Yaha key = Book ID aur value = Book Title


    def show(self):
        print("Member ID:", self.mid)
        print("Member Name:", self.name)
        print("Member Phone Number:", self.phno)
        print("Is Alive:", self.isAlive)
        print("Library Card:", self.lib_card)


class Lib:
    def __init__(self,name,address,phno):
        self.name=name
        self.address=address
        self.phno=phno

        self.book=[]   # library ki saari books ke objects store honge
        self.member=[] # library ke saare members ke objects store honge

        self.load_data()
        # CHANGE: Jaise hi library ka object banega, CSV se purana data load hoga


    # CHANGE 1: Ye method memory ka data CSV files me save karega
    def save_data(self):

        # Books ka data books.csv me save karna
        with open("books.csv","w",newline="") as f:

            fields=["bid","title","author","price","is_issue","isAlive"]

            writer=csv.DictWriter(f,fieldnames=fields)
            # DictWriter dictionary ke data ko CSV rows me convert karta hai

            writer.writeheader()
            # CSV file me sabse pehle column headings likhega

            for b in self.book:
                writer.writerow({
                    "bid":b.bid,
                    "title":b.title,
                    "author":b.author,
                    "price":b.price,
                    "is_issue":b.is_issue,
                    "isAlive":b.isAlive
                })
                # Har book object ki details CSV me ek row banakar save hongi


        # Members ka data members.csv me save karna
        with open("members.csv","w",newline="") as f:

            fields=["mid","name","phno","isAlive"]

            writer=csv.DictWriter(f,fieldnames=fields)
            writer.writeheader()

            for m in self.member:
                writer.writerow({
                    "mid":m.mid,
                    "name":m.name,
                    "phno":m.phno,
                    "isAlive":m.isAlive
                })


        # Issued books ka data issue_records.csv me save karna
        with open("issue_records.csv","w",newline="") as f:

            fields=["mid","bid","title"]

            writer=csv.DictWriter(f,fieldnames=fields)
            writer.writeheader()

            for m in self.member:

                # m.lib_card.items() se dictionary ki key aur value dono milti hain
                # Yaha bid = Book ID aur title = Book ka naam
                for bid,title in m.lib_card.items():

                    writer.writerow({
                        "mid":m.mid,
                        "bid":bid,
                        "title":title
                    })


    # CHANGE 2: CSV files se data read karke objects dobara create karna
    def load_data(self):

        # Pehle check karenge ki books.csv file exist karti hai ya nahi
        if os.path.exists("books.csv"):

            with open("books.csv","r",newline="") as f:

                reader=csv.DictReader(f)
                # DictReader CSV ki har row ko dictionary ke form me read karta hai

                for row in reader:

                    b=Book(
                        int(row["bid"]),
                        row["title"],
                        row["author"],
                        float(row["price"])
                    )

                    # CSV se values string ke form me aati hain
                    # Isliye True/False ko dobara Boolean me convert kar rahe hain
                    b.is_issue = row["is_issue"] == "True"
                    b.isAlive = row["isAlive"] == "True"

                    self.book.append(b)
                    # Banaya hua Book object library ki list me add kar diya


        # Members ki CSV file read karna
        if os.path.exists("members.csv"):

            with open("members.csv","r",newline="") as f:

                reader=csv.DictReader(f)

                for row in reader:

                    m=Member(
                        int(row["mid"]),
                        row["name"],
                        int(row["phno"])
                    )

                    m.isAlive = row["isAlive"] == "True"

                    self.member.append(m)


        # Issued books ka record read karna
        if os.path.exists("issue_records.csv"):

            with open("issue_records.csv","r",newline="") as f:

                reader=csv.DictReader(f)

                for row in reader:

                    mid=int(row["mid"])
                    bid=int(row["bid"])
                    title=row["title"]

                    # Check karenge ki ye issue record kis member ka hai
                    for m in self.member:

                        if m.mid == mid:

                            # Us member ke library card me book wapas add kar denge
                            m.lib_card[bid]=title
                            break


    def show(self):
        print("Library Name:", self.name)
        print("Library Address:", self.address)
        print("Library Phone Number:", self.phno)

        # Sirf active books aur members count hongi
        print("Total Book:",len([b for b in self.book if b.isAlive==True]))
        print("Total Members:",len([m for m in self.member if m.isAlive==True]))


    def add_book(self):
        bid=int(input("Enter Book ID:"))

        # Same Book ID dobara add nahi karne denge
        for b in self.book:
            if b.bid==bid:
                print("Book ID already exists")
                return

        name=input("Enter Book Title:")
        author=input("Enter Book Author:")
        price=float(input("Enter Book Price:"))

        b=Book(bid, name, author, price)
        self.book.append(b)

        self.save_data()  # CHANGE: Book add hone ke baad CSV update karna
        print("Book Added Successfully")


    def show_book(self):
        if len(self.book)==0:
            print("No Book Available")

        else:
            print("......................")

            for b in self.book:

                # Sirf wahi books show hongi jo delete nahi hui hain
                if b.isAlive==True:
                    b.show()
                    print("......................")


    def del_book(self):
        if len(self.book)==0:
            print("No Books Available")

        else:
            bid=int(input("Enter Book ID to Delete:"))

            for b in self.book:

                if b.bid == bid and b.isAlive==True:

                    # Issued book ko delete nahi kar sakte
                    if b.is_issue==True:
                        print("Book is already issued. Return it first.")
                        return

                    b.isAlive = False
                    self.save_data()  # CHANGE: Delete hone ke baad CSV update

                    print("Book Deleted Successfully")
                    break

            else:
                # for loop me koi matching book nahi mili tab else chalega
                print("Book not found")


    def add_member(self):
        mid=int(input("Enter Member ID:"))

        # Duplicate Member ID check karna
        for m in self.member:
            if m.mid==mid:
                print("Member ID already exists")
                return

        name=input("Enter Member Name:")
        phno=int(input("Enter Member Phone Number:"))

        m=Member(mid, name, phno)
        self.member.append(m)

        self.save_data()
        print("Member Added Successfully")


    def show_members(self):
        if len(self.member)==0:
            print("No Members Available")

        else:
            print("......................")

            for m in self.member:

                # Sirf active members ko show karenge
                if m.isAlive==True:
                    m.show()
                    print("......................")


    def remove_member(self):
        if len(self.member)==0:
            print("No Members Available")

        else:
            mid=int(input("Enter Member ID to Remove:"))

            for m in self.member:

                if mid == m.mid and m.isAlive==True:

                    # Agar member ke library card me books hain to remove nahi karenge
                    if len(m.lib_card)>0:
                        print("Member has issued books. Return them first.")
                        return

                    m.isAlive = False
                    self.save_data()

                    print("Member Removed Successfully")
                    break

            else:
                print("Member not found")


    def book_issue(self):
        bid=int(input("Enter Book ID to Issue:"))

        for b in self.book:

            # Book ID match ho, book issued na ho aur available bhi ho
            if bid==b.bid and b.is_issue==False and b.isAlive==True:

                mid=int(input("Enter Member ID to Issue Book:"))

                for m in self.member:

                    # Member ID match ho aur member active bhi ho
                    if mid==m.mid and m.isAlive==True:

                        if len(m.lib_card)==3:
                            print("Member has already issued 3 books.......")

                        else:

                            # Book ID ko key aur book title ko value banakar dictionary me store karna
                            m.lib_card[bid]=b.title

                            b.is_issue=True

                            self.save_data()  # CHANGE: Issue ke baad CSV update

                            print("Book Issued Successfully")
                            return

                else:
                    print("Member not found or not alive.......")
                    return

        else:
            print("Book not found or already issued or not alive.....")


    def book_return(self):
        bid=int(input("Enter Book ID to Return:"))
        mid=int(input("Enter Member ID to Return Book:"))

        for b in self.book:

            if b.bid==bid and b.is_issue==True:

                for m in self.member:

                    # Check karenge ki book isi member ke library card me hai
                    if m.mid==mid and bid in m.lib_card:

                        b.is_issue=False

                        # Dictionary se returned book ka record remove karna
                        m.lib_card.pop(bid)

                        self.save_data()  # CHANGE: Return ke baad CSV update

                        print("Book Returned Successfully.......")
                        return

                else:
                    print("Book not issued to this member.......")
                    return

        else:
            print("Book not found or not issued...........")


li=Lib("City Library","sunderpur",1234567890)

while True:
    print("press 1 for show lib details:")
    print("press 2 for add book:")
    print("press 3 for show book:")
    print("press 4 for delete book:")
    print("press 5 for add member:")
    print("press 6 for show members:")
    print("press 7 for remove member:")
    print("press 8 for book issue:")
    print("press 9 for book return:")
    print("press 10 for exit:")

    op=int(input("Enter your choice:"))

    if op==1:
        li.show()

    elif op==2:
        li.add_book()

    elif op==3:
        li.show_book()

    elif op==4:
        li.del_book()

    elif op==5:
        li.add_member()

    elif op==6:
        li.show_members()

    elif op==7:
        li.remove_member()

    elif op==8:
        li.book_issue()

    elif op==9:
        li.book_return()

    elif op==10:
        break

    else:
        print("Invalid Choice")