temp = int(input("What's the temperature today? "))
if not (temp >= 0 and temp <= 30):
     print("The temperature is bad today")
     print("Sorry Buddy, stay indoors!")
elif not (temp < 0 or temp > 30):
     print("The temperature is great today")
     print("Go outside, Buddy")