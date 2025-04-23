# while Loop
# program to display numbers from 1 to 5

# initialize the variable
i = int(input('Enter Starting Value:'))
n = int(input('Enter Ending Value:'))

# while loop from i = 1 to 5
while i <= n:   
    print('while loop :',i)
    i = i + 1    
    
# while loop using else statements
counters = 5 
#int(input('Enter Value: '))

while counters < 3:
    counters = counters + 1
    print('Inside loop')
else:
    print('Inside else')
    
#The else block will not execute 
# if the while loop is terminated by a break statement.    
counter = 0

while counter < 3:
    # loop ends because of break
    # else part is not executed 
    if counter == 1:
        break
        print('If block...')       
    else:
        print('Else block...')
        
    print('Inside loop')
    counter = counter + 1
else:
    print('Inside else')