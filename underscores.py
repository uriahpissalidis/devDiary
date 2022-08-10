a = input("type here:")
a1 = ""
for i in range(len(a)):
    if a[i] == ' ':
        a1 = a1 + '_'
    else:
        a1 = a1 + a[i]
a1 = a1.replace('.', "")
print(a1)
a = input()