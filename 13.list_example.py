# List - is collections of elements , 
# every elements seprate by comma(,) & define in to [] braces..

# multiple type list   
"""list1 = [1, 2, "Python", "JAVA", 15.9, True]      

# int,string , bool, flot 
list2 = ["A", "B", "c", "D"]   
list_3 = [1,2,3,4,5]   
  
# printing the list  
print(list1)  
print(list2)  
print(list_3)

# Python List operation

# 1. Repeation  [ repetition operator * ]
list1 = [1, 2, 3, 4, 5]
  
a = list1 * 2
print('Repeation of List : ' , a)  

# 2. concatination [ concatenation operator + ] 
list1 = [11, 22, 33, 44, 55]  
list2 = ['A', 'B', 'C', 'D', 'E']  
   
b = list1 + list2
print('Concatination of List : ',b)  

# 3. length of List     
list1 = [11, 12, 13, 14, 15, 16, 17, 18, 19,20] 
c = len(list1)
print('Length of List : ',c)  

# 4. Iteration [ using for loop ]
list1 = [21, 22, 23, 24, 25]  

for i in list1:   
    print('Iterating of List : ',i)  
    
# 5. Membership
list1 = [10, 20, 30, 40, 50]  
# true when value is avalible in list  
# false when value is not avalible in list

print(60 in list1) #  false 
print(70 in list1) # false 
  
print(30 in list1) # true
print(10 in list1)  # true


# Python in Built Function of List
    
# [ len() , max() , min() ]
list1 = [12, 16, 18, 20, 39, 40]  

# 1. length of the list  
print('Length of List :',len(list1))  #output: 6

# 2. maximum elements of the list  
print('Maximum Element of List :',max(list1)) #output: 40

# 3. minimum elements of the list 
print('Minimum Element of List :',min(list1)) #output: 12

# List Methods :

# 1. append() : Adds List Element as value of 
# List end of list [last ma].
List = ['JAVA', 'Python', 2, 5]

List.append(6)
List.append("enter your name")
print('List Append():', List)

# 2.Insert() [add the elements on specific position ]
List.insert(2,'Flutter')
print('List Insert():',List)

# 3.Extend [ concate the two list without create new list]:  
List1 = [1, 2, 3]
List2 = [2, 3, 4, 5]

# Add List2 to List1
List1.extend(List2)
print("List Extend () First Time :",List1)
 # output : [1,2,3,2,3,4,5]
 
# Add List1  to List2 now
List2.extend(List1)
print('List Extend () Second Time :',List2)
# output : [2,3,4,5,1,2,3,2,3,4,5]

# + operator creates a new list containing the 
# concatenated elements, 
# extend() modifies one of the lists in place by 
# adding the elements from another list.

# 4. Sum [not work when pass string value]
List = [1, 2, 1, 4, 5] 
print("Sum of List Elements : " ,sum(List)) # output : 13

# 5. Count [count the simmiler elements ]
List = [1, 2, 3, 1, 2, 1, 2, 3, 2, 1]
print("Count the Elements :",List.count(2)) # output : 4

# 6. index return the index number
ListIndex1 = [1,2,3,4,5,6]
print(" List Index() :",ListIndex1.index(3)) 
#you have to pass value  #output : 2  

ListIndex2 = [1,2,3,"yourname",5,1.1]
print(" List Index() :",ListIndex2.index("yourname"))  

#7. sort() , 8. reverse()
ListData = [5,6,3,2,1] 

# reverse() : only reverse the list without sorting elements 
ListData.reverse()
print('LIST DATA Reverse:',ListData) # output : 1 2 3 6 5

# sort() : sorting elements [small to large]
ListData.sort()
print("List Short() : ",ListData)   # output : 1 2 3 5 6     

# 9. pop
ListData1 = [11,22,33,44,55,66]

a = ListData1.pop() # remove last element

print("List pop() First Time : ",a)

b = ListData1.pop(2) # remove specific element by passing index
print("List pop() Second Time : ",b)
print('after Call POP(): ',ListData1) # output : 11 22 44 55 
 
# 10. slicing List 

fruit=['apple','cherry','pineapple','orange','mango']

slice_list=fruit[1:3] # print 2 element 1 and 2
slice_list=fruit[:3] # print 3 element 0 - 2
slice_list=fruit[-2:] #print last 2  

print('Slice List : ',slice_list) 

"""  
# 2D List  # List inside List [collectionof List = 2D List]

"""array=[ [1,2,3,4,5], 
        ['A','B','C','D','E'],
        [66,77,88,99,11],
        [23.5,45.4,67.2,32,10] ]

#display
print('2D List : ',array)

#get the first row
print('Fetch First Row :',array[0])

#get the third row
print('Fetch Second Row :',array[2])

#get the first row third element
print('Elements :',array[0][2])  

#get the third row forth element
print('Elements :',array[2][3])


#creare 2D array with 4 rows and 5 columns with Updating , Deleting
array=[[23,45,43,23,45],
       [45,67,54,32,45],
       [89,90,87,65,44],
       [23,45,67,32,10]]

#update row values in the 3rd row
print('Befor Updated List Values : ',array)

array[2] = [0,'name',24,35.56,True]

print('After Updated List Values : ',array)

#update the first row , third column
array[0][2]='yourname'

print('After Update Elements :', array)

#update the second row , third column
array[1][2]=400

# deleting
# [delete array list]

print('Befor Deleted List:',array)

del array[0]

print('After Deleted List:',array)

# [delete array element using index]
del array[1][2]

#display
print(array)
"""

# dynamic list : Declaring the empty list   [ 1. append() ]

number_list = []
n = int(input("Enter the list size :"))

print("\n")

for i in range(0, n):
    item = input('Enter the Elements :')
    number_list.append(item)
    print(f"Index: {i}, elements: {n}")


  

 
 
"""

# [ 2. remove() ]
list = [0,1,2,3,4,'a','b',5]       

print("Before Remove Elements")     

for i in list:      
    print(i,end=" ")
          
# pass value [ not indext ]
list.remove(3)      

print("\n After Removing element...")      

for i in list:      
    print(i,end=" ")     
"""