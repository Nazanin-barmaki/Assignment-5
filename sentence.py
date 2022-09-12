sentence = input('enter your sentence: ')
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
list_letters = []
count=0

word_list = sentence.split()
for i in letters:
    lt = sentence.count(i)
    if lt > 0:
     list_letters.append(f'{lt} {i}')

for i in word_list:
       count  += len(i)

for i in word_list:
   count+= len(i)

else:
        
        counter = 0

character = len (sentence)   

space = sentence.count('\n') + sentence.count(' ')

comma = sentence.count(',') +sentence.count('.')

print(f'number of letters: {list_letters}\nnumber of words: {len(word_list)}\nnumber of charachters: {count}\nnumber of spaces: {space} and enters: {comma}')