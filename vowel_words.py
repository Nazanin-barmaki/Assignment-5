Words = input ('Enter your words : ')

List_Words = []
List_Vowels = ['i', 'o', 'u', 'e', 'a', 'I', 'O', 'U', 'E', 'A']

for letter in Words :
    
    List_Words.append(letter)
    
for i in range (len(List_Words)):
    
    if List_Words[i] in List_Vowels :
        
        List_Words[i] = '?'
        
print(''.join(List_Words))