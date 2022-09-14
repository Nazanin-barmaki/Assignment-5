mathematical=input("enter your math phrase: ")
list_operation=[]
list_answer=[]
operation = ['*','/','+','-']
counter = 0

for math in mathematical:
    if mathematical=='/' or mathematical=='*' or mathematical=='+' or mathematical=='-':
        operation.append(mathematical)

for i in range(4):
        
        if mathematical == operation[i]:
            
            operation.append(mathematical)
                    

for i in range(4):
     list_answer = mathematical.split(operation[i])
     mathematical = ' '.join(list_answer)

list_answer = mathematical . split(' ')

while ''in mathematical :
        mathematical.remove('')

for i in range(len(mathematical)):

        mathematical[i] = int (mathematical[i])

while '+' in operation or  '-' in operation:   
            
        if operation[counter] == '+':
            
            mathematical[counter] = mathematical[counter]+mathematical[counter+1]
            
            mathematical.pop(counter+1) 
            operation.pop(counter)
            
            counter -= 1
            

while '*' in operation  or  '/' in operation:
        
        if operation[counter] == '*':
            
            mathematical[counter] = mathematical[counter] * mathematical[counter+1]
            
            mathematical.pop(counter+1) 
            operation.pop(counter)
            
            counter -= 1

        elif operation[counter] == '/':
            
            mathematical[counter] = mathematical[counter]/mathematical[counter+1]
            
            mathematical.pop(counter+1) 
            operation.pop(counter)

            counter -= 1   

            counter += 1
            counter = 0    


        elif operation[counter] == '-':
            
            mathematical[counter] = mathematical[counter]-mathematical[counter+1]
            
            mathematical.pop(counter+1) 
            operation.pop(counter)

            counter -= 1
    
            counter += 1 
            counter = 0

    

            print(' your mathematical pharases is '[0])
                



                    


