from random import randint

class Train:

    def __init__(self, trainNo):
        self.trainNo = trainNo

    def book(self, fro, to):
        print(f"ticket is booking in train no: {self.trainNo} from {fro} to {to}")

    def getstatus(self):
        print(f"train no: {self.trainNo} is running on time")

    def getfare(self, fro, to):
        print(f"ticket fare in train no: {self.trainNo} from {fro} to {to} is {randint(222,5555)}")

t = Train(24217)
t.book("darbhanga", "new delhi")
t.getstatus()
t.getfare("darbhanga", "new delhi")
            