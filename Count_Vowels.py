word = input('Enter A Word - ')
count = 0
for i in word:
    if i == 'a':
        count=count+1;
    elif i == 'e':
        count=count+1;
    elif i == 'i':
        count=count+1
    elif i == 'o':
        count=count+1;
    elif i == 'u':
        count=count+1;

print("No. Of Vowels = ",count)