class Dog:
    """A simple attempt to model a dog."""
    def __init__(self,name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command"""
        print(f"{self.name} is now sitting.")
    def roll_over(self):
        """simulate rolling over in response to a command"""
        print(f"{self.name} rolled over!")
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def set_age(self,age):
        if self.age < age:
            self.age = age
    def __str__(self):
        """create a string representation of a dog"""
        return f"Name: {self.name}\nAge: {self.age}"

d = Dog("Molly",10)
d.sit()
print(d)
d.name = "Suzy"
print(d)
