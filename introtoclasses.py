class User:
    def __init__(self, name, age): # init method called whenever new object is called. It's where attributes go, and is an argument of the object
        self.name = name # define attribute to be called whenever object is called.
        self.age = age # attribute 
        print(name)   # this is where you specify what the attribute does when all classes are called. It's saying to print the name of the object, as it's defined
    def something(self): # this is a method. It specifies the operations that can be performed by class User. A method is the shit that the object does
        print("fuck you")
    def get_age(self):
        return self.age
user1 = User("Matthew", 19) # an instance of the class User, a.k.a object of class User
user1.something() #call something method on User1 object of User class
print(user1.get_age()) # call age variable/field of init method of User1 object of class User
user2 = User("Lucas", 21)
user2.something()
print(user2.get_age())

class Course:
    def __init__(self, name, max_students):
            self.name = name
            self.max_students = max_students
            self.students = [] # you can make an attribute and not assign it directly to one of the parameters
    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False
    def get_average_grade(self):
        pass
s1 = User("Luca", 20)
s2 = User("David",19)
s3 = User("Aidan", 21)

diffEq = Course("Differential Equations", 2)
diffEq.add_student(s1)
diffEq.add_student(s2) 
print(diffEq.students[0].name)  # prints Luca
