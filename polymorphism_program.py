# This is a polymorphism program

class QA:
    def work(self):
        print("Testing manually")

class Automation(QA):
    def work(self):
        print("Testing using automation tools")


qa1 = QA()
qa2 = Automation()

qa1.work()
qa2.work()

