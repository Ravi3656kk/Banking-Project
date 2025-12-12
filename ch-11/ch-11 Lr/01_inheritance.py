class Employee:
      company = "chhotu privet ltd"
      def show(self):
            print(f"the name is{self.name} and the salary is {self.salary}")

# class programmer:
#      def show(self):
#             print(f"the name is{self.name} and the salary is {self.salary}")

#      def showlanguage(self):
#            print(f"the name is {self.name} and he is good with{self.language} language")

class programmer(Employee):
      company = "ITC infotech"
      def showlanguage(self):
             print(f"the name is {self.name} and he is good with{self.language} language")
a = Employee()
b = programmer()

print(a.company, b.company)