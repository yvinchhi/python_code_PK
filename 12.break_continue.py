# break using for loop

for i in range(5):
    if i == 3:
        break
        #continue
    print(i)
    
    
# break using while loop

i=1
while i <= 10:
    print('6 * ',(i), '=',6 * i)
    if i >= 10:
        break
    i = i + 1   