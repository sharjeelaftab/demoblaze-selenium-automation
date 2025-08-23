# Parent class
class Person:
    def speak(self):
        print("I am a person")

# Child class inheriting from Person/Parent class
class Student(Person):
    def study(self):
        print("I am studying automation testing")


pupil = Student() # Created object of Student
pupil.speak()  # Called from parent class "Speak"
pupil.study()  # Called from child class "Study"
