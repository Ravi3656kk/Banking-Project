class TwoVectoroD:
      def __init__(self, i,j):
            self.i = i
            self.j = j
      
      def show(self):
            print(f"The vector is {self.i}i + {self.j}j")


class ThreeDVector(TwoVectoroD):
      def __init__(self, i,j,k):
            super().__init__(i,j)
            self.k = k
      
      def show(self):
            print(f"The vector is {self.i}i + {self.j}j + {self.k}k")

a = TwoVectoroD(1,2)
a.show()
b =  ThreeDVector(1, 2, 3)   
b.show()