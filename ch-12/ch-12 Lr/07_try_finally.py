def main():
      try:
          a = str(input("enter your seting  name: "))
          print(a)
          return

      except Exception as e:
        print(e)
        return

      finally:
             print("i am inside of finally")

main()