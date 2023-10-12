rows = int(input("How any rows: "))
columns = int(input("How any columns: "))
symbol = input("Enter a symbol to use: ")

for i in range(rows):
      for j in range(columns):
           print(symbol, end="")
      print()