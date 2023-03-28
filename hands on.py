#Di ko po pala nasave ma'am pasensya po
class Students:
    def __init__(self, name, pre, mid, fin):
        self.name = name
        self.pre = pre
        self.mid = mid
        self.fin = fin
    def ave(self):
        self.average = (self.pre + self.mid + self.fin) / 3
    def show(self):
        self.ave()
        print("Name: ", self.name)
        print("Prelim Grade: ", self.pre)
        print("Midterm Grade: ", self.mid)
        print("Final Grade: ", self.fin)
        if self.average >= 70:
            self.status = "Passed"
        else:
            self.status = "Failed"
        print("Average Grade: {} ({})".format(round(self.average,0), self.status))
print()
print("Student's Average Grade ")
print()
Name = str(input("Enter Name: "))
pre = float(input("Enter Prelim: "))
mid = float(input("Enter Midterm: "))
fin = float(input("Enter Finals: "))
print()
stud = Students(Name, pre, mid, fin)
stud.show()
