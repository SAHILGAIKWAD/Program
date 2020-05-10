# Program - Class Method and Variable, Static Method anad Variable

# Class
class MyStudent:
  
  # Class Method
  name = "Python"
  
  # Constructor
  def __init__(self, fname, lname):
    # Instance Variable 
    self.fname = fname
    self.lname = lname
  
  # Instance Method  
  def info(self):
   print(self.fname, self.lname)
  
  # Class Method
  @classmethod
  def prog(cls):
    print(cls.name)
  
  # Static Method
  @staticmethod
  def show():
    print("Hello World!!!")
    
# Object
obj = MyClass("Sahil", "Gaikwad")

# function
obj.info()
obj.prog()
obj.show()
