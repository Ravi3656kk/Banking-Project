# def avrege():
#       a = int(input("enter your number: "))
#       b = int(input("enter your number: "))
#       c = int(input("enter your number: "))
#       d = int(input("enter your number: "))
#       e = int(input("enter your number: "))
      
#       avrege = (a+b+c+d+e)/5
#       print(avrege)
# avrege()
# print("thanku") 

# def bodmash():
#       a = int(input("enter the number: "))
#       b = int(input("enter the number: "))
#       c = int(input("enter the number: "))
#       d = int(input("enter the number: "))
#       e = int(input("enter the number: "))

#       bodmash = (a + b - c * d / e)
#       print(bodmash)

# bodmash()
# print("thanku for solving of question")

# def goodDay(name , ending):
#       print ("good Day , "+ name)
#       print(ending)
# goodDay("mukes", "thanku brother" )
# goodDay("rakesh", "thanku brother" )
# goodDay("manohar", "thanku brother" )

# s = set()
# s.add(20)    # so python consider 20 ==20.0 to be same value
# s.add(20.0)  # so python consider 20 ==20.0 to be same value
# s.add('20')

# print(len(s)) #there for the resion lenghth is 2

# def goodDay(name, ending="tank you"): #default arguments
#       print(f"good day,{name}")
#       print(ending)
# goodDay("anchal","kya lagrahi ho")

# def welcome(college , ending="placement karo bencho"):
#       print(f"welcome,{college}")
#       print(ending)
      
# welcome("vidya college of engineering","pata hai londe kitna paresa hai")

#recursion(calling itself)

def factorial(n):
      if(n==1 or n==0):
            return 1
      return n* factorial(n-1)

n = int(input("enter the number: "))
print(f"the facrorial of this number is: {n*factorial(n-1)}")

def arthemetic equation():