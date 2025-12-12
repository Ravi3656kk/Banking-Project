class Employee:
      company = "ITC "
      name = "default name"
      def show(self):
            print(f"the name of Employee is {self.name} and the company is {self.company}")

class Coder:
      language = "python"
      def printLanguage(self):
            print(f"out of all languages here is your language {self.language} ")

class programmer(Employee, Coder):
      company = "ITC infotech"
      def showlanguage(self):
             print(f"the name is {self.company} and he is good with {self.language} language")

a = Employee()
b = programmer()

b.show()
b.printLanguage()
b.showlanguage()