while 1==1:
     print("Help, I am stuck in a loop")
name =""
while len(name) ==0:
      name= input("Enter your name: ")
print("Hello " + name)
name =None
while not name:
      name= input("Enter your name: ")
print("Hello " + name)