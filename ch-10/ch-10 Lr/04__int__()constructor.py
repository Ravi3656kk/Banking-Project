
class Employee:
      language = "python" #this is a class attribute
      salary = 1200000

      def __init__(self , name, salary, language):
            self.name = name
            self.salary = salary
            self.language = language

            print("i am creating an object")

      def getinfo(self):
            print(f"the language is {self.language}.The salary is {self.salary}")

      @staticmethod      
      def greet():
            print("good morning")

harry = Employee("harry", 1600000, "java programing language")
#harry.name = "java programing language"
print(harry.name,harry.salary,harry.language)

