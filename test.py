import re

res = "apple banana peach pear grape melon yes no shu yun"
ls = ["apple", "pear", "grape", "shu", "heart"]


# Replace multiple words with K
# Using join() + split() + list comprehension

for i in ls:
    print(i)
    res = ' '.join(
        [i.upper() if idx == i else idx for idx in res.split()])
    print(res)
