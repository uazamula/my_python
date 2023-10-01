f1 = open("StudentsM1023.csv")
f2 = open("StudentsM1023_formatted.csv", 'w')
s1 = f1.read()

items_to_remove = '"<>'

for i in items_to_remove:
    s1 = s1.replace(i, "")

s1 = s1.replace(" ", ",")

f2.write(s1)
f1.close()
f2.close()
print(s1)
