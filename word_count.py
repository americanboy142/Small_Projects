f = open("word_count.txt","r")

text = f.read()

text = text.split()

#print(len())
#print(text[0])

word = "time"
count = 0
for i in text:
    if i.__contains__(word):
        count += 1

print(count)