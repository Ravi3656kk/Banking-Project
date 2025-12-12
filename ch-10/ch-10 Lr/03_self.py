
class Employee:
      language = "python" #this is a class attribute
      salary = 1200000

      def getinfo(self):
            print(f"the language is {self.language}.The salary is {self.salary}")

      @staticmethod      
      def greet():
            print("good morning")

harry = Employee()
harry.language = "java programing language"

#attribute
harry.getinfo()
harry.greet()

#Employee.getinfo(harry)

      
