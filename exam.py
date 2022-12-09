word1 = input("word 1 ---> ")
word2 = input("word 2 ---> ")

f = open("text.txt", "r")
content = f.read()
result = ""
content = content.replace(",", " ")
for word in content.split(" "):
    if(word == word1):
        result += word2 + " "
    else:
        result += word + " "
f = open("text.txt", "w")
f.write(result)

