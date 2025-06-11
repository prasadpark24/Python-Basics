class student:
    def __init__(self):
        self.name=input("Enter Your Name:")
        self.reg_no=input("Enter Your Register number:")
        self.year=input("Enter Your Current Year:")
        self.DOB=input("Enter Your DOB(DD/MM/YYYY):")
        self.marks=[]
    def display_details(self):
        print("-----STUDENT DETAILS----")
        print("Student Name:",self.name)
        print("Register Number:",self.reg_no)
        print("Current Year:",self.year)
        print("DOB:",self.DOB)
    def sub_details(self):
        num_of_subs=int(input("Enter Number of subjects:"))
        for i in range(1, num_of_subs + 1):
            mark = float (input(f"Enter Mark of sub{i}:"))
            self.marks.append(mark)
class calculate:
    def grade_and_average(self,marks):
        total=sum(marks)
        avg=total/len(marks)

        print("\n------Marks and Result-----")
        print("Total Marks:",total)
        print("Percentage:",avg)
        if avg>90:
            grade="S"
        elif avg>80:
            grade="A"
        elif avg>70:
            grade="B"
        elif avg>60:
            grade="c"
        elif avg >50:
            grade="D"
        else:
            grade="Fail!"
      
            

        print("Grade:",grade)

s1=student()
s1.sub_details()
s1.display_details()

result=calculate()
result.grade_and_average(s1.marks)