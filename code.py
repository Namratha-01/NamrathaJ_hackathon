import  codecs

wordList = [line.strip() for line in codecs.open('File.txt' , 'r').readlines()]
wordList2 = [line.strip() for line in codecs.open('File2.txt', 'r').readlines()]
for x in range(len(wordList)) :
    for y in range(x + 1, len(wordList ) ):
        if wordList[x] == wordList[y]:
            wordList2.append(wordList[x])
        for y in wordList2:
            wordList.remove(y)

# assuming the code above is working
# now write your updated contents
with open('outfile1.txt','w') as outfile1:
    for word in wordList:
        outfile1.write(word + '\n')

with open('outfile2.txt','w') as outfile2:
    for word in wordList2:
        outfile2.write(word + '\n')
