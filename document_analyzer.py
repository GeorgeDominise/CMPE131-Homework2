import string

text = open("document.txt", encoding="utf8")

d = dict()

for line in text:
        line = line.strip()
        line = line.lower()
        line = line.translate(line.maketrans("", "", string.punctuation))
        words = line.split(" ")
        for word in words:
            if word in d:
                d[word] = d[word] + 1
            else:
                d[word] = 1
x = {}
for key in list(d.keys()):
    x[key] = d[key]

sort = sorted(x.items(), key = lambda x:x[1], reverse = True)
top5 = list(sort)[:5]
for i in top5:
    print(i[0], ":", i[1])