#Loop COntrol Statement
#BREAK CONTROL STATEMENT
while True:
      name = input("Enter your name: ")
      if  name !="":
           break
#CONTINUE LOOP CONTROL STATEMENT

phone_number = "123-456-7890"

for i in phone_number:
      if i== "-":
           continue
      print(i, end="")

#PASS CONTROL STATEMENT

for i in range (1, 21):
      if i ==12:
           pass
      else:
           print(i, end="")