import re

res = "apple banana peach pear grape melon yes no shu yun"
ls = ["apple", "pear", "grape", "shu", "heart"]
bl = ["gold", "sell"]
f = open("test.txt", "r")
data = f.read()
# print(data)
k = ["apple", "pear"]
sub = "GOLD"
#x = re.sub(k[0], sub, data, flags=re.IGNORECASE)
#x = re.sub(k[1], sub, x, flags=re.IGNORECASE)

# print(x)
n = data

if [x for x in ls if re.search(x, data, re.IGNORECASE)]:
    if not[i for i in bl if re.search(i, data, re.IGNORECASE)]:
        for j in ls:
            n = re.sub(j, j.upper(), n, flags=re.IGNORECASE)
            print(n)
        print(n)

f.close()
