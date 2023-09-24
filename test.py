str = "= 33 300 $"
p = ''
for s in str:

    if s >= '0' and s <= '9':
        p+=s
p = int(p)
print(p)


