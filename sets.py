#sets

dishes={"a","b","c"}
cutlery={"x","y","z"}
print(dishes.difference(cutlery))
print(dishes.intersection(cutlery))

dishes.add("v")
dishes.update(cutlery)

for x in dishes:
     print(x)

dinner_table=dishes.union(cutlery)

for x in dinner_table:
     print(x)
print(dishes.difference(cutlery))