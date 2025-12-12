from random import randint

class Train:

    def __init__(laundiyabaaz, trainNo):
        laundiyabaaz.trainNo = trainNo

    def book(laundiyabaaz, fro, to):
        print(f"ticket is booking in train no: {laundiyabaaz.trainNo} from {fro} to {to}")

    def getstatus(laundiyabaaz):
        print(f"train no: {laundiyabaaz.trainNo} is running on time")

    def getfare(laundiyabaaz, fro, to):
        print(f"ticket fare in train no: {laundiyabaaz.trainNo} from {fro} to {to} is {randint(222,5555)}")

t = Train(24217)
t.book("darbhanga", "new delhi")
t.getstatus()
t.getfare("darbhanga", "new delhi")
            