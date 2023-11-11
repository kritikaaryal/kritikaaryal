#Absolute Path
#file = open("/Users/KAryal24/Documents/GitHub/kritikaaryal/testing.py")
file=open("testing.py")
data = file.read()
words=data.split()
#print(data)
num_words=len(words)

for i in range(num_words):
    print(words[num_words-i-1],end=" ")
output_file = open("TextFiles/reversed_text.txt","w")
output_file.write(words[0])
for i in range(1,num_words):
    output_file.write(" "+words[num_words-i-1].strip())
output_file.close()
