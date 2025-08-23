# This is an abstraction program

from abc import ABC, abstractmethod

class Testing(ABC):  # Abstract class
    @abstractmethod
    def test(self):
        pass

class AutomationTesting(Testing):
    def test(self):
        print("Doing automation testing")


tester = AutomationTesting()
tester.test()
