student={}
while True:
    print("\n--------STUDENT MANAGER APP-------")
    print("1. Add Studet")
    print("2. View Students")
    print("3. Check Result")
    print("4. Exit")

    choice=input("Enter your choice")

    if choice=='1':
        name=input("Enter student name: ")
        marks=int(input("Enter marks"))
        student[name]=marks
        print(f"{name} Succesfuly Added")
    elif choice=="2":
        if not student:
            print("No student found!")
        else:
            for name, marks in student.items():
                 print(name, ":", marks)
    elif choice=="3":        
        name=input("Enter your name: ")

        if name in student:
            marks=student[name] # student ka marke name mai jayega aur aur mark mai assign ho jayega 

            if marks>=40:
                print("Student Pass")
            else:
                print("Fail")
        else:
            print("Studetn Not Found")
    elif choice=="4":
          print("Exiting....")
          break

    else:
         print("In_valid Input")
        