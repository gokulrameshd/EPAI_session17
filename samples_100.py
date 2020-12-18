
# write a python program to add two and print the result.
num1 = 5465461
num2 = 8765468
sum = num1 + num2
print(f'Sum: {sum}')


# write a python function to add two user provided numbers and return the sum
def add_two_numbers(num1, num2):    
    sum = num1 + num2    
    return sum

# write a program to find and print the largest among three numbers and print the result.
num1 = 123
num2 = 125
num3 = 148
if (num1 >= num2) and (num1 >= num3):   
    largest = num1
elif (num2 >= num1) and (num2 >= num3):   
    largest = num2
else:   largest = num3
print(f'largest:{largest}')

# write a program to find length of list and print the result.
l = [1,2,3,4,5]
print(len(l))


# write a function to find length of list and return the result.
def get_list_length(l):
    return len(l)


# write a program to convert tuple to list and print the result.
t = (1,2,4,5,6)
print(f'list:{list(t)}')


# write a function to convert tuple to list and print the result.
def convert_tuple2list(t):
    return list(t)

# write a program to convert list to tuple and print the result.
l = ['a',4,5]
print(f'tuple:{tuple(l)}')

# write a function to convert list to tuple and print the result.
def list2tuple(l):
    return tuple(l)

# write a function to find length of list and return the result.
def tuple_lenght(t):
    return len(t)


# write a program to find length of list and print the result.
t = 1,2,3,4,5
print(f'tuple length: {len(t)}')

# write a program to concat two list and print the result.
l1 = [1,2,3]
l2 = [4,5,6]

print(f'sum : {l1 + l2}')

# write a functiom to concat two list and return the result.
l1 = [1,2,3]
l2 = [4,5,6]
def list_concat(l1,l2):
    return l1 + l2 

# write Python code to convert Celsius scale to Fahrenheit scale  and print the result.
def Cel_To_Fah(n): 
    return (n*1.8)+32
n = 20
print(int(Cel_To_Fah(n))) 

# write Python program to convert temperature from Fahrenheit to Kelvin  and print the result.
  
def Fahrenheit_to_Kelvin(F): 
    return 273.5 + ((F - 32.0) * (5.0/9.0)) 
F = 100
print("Temperature in Kelvin ( K ) = {:.3f}" 
            .format(Fahrenheit_to_Kelvin( F ))) 

# write Function to convert temperature  from degree Celsius to Kelvin  and print the result.
def Celsius_to_Kelvin(C): 
    return (C + 273.15) 
C = 100 
print("Temperature in Kelvin ( K ) = ",  
                    Celsius_to_Kelvin(C)) 

# write Python code to convert radian to degree  and print the result.
def Convert(radian): 
    pi = 3.14159
    degree = radian * (180/pi) 
    return degree 
radian = 5
print("degree =",(Convert(radian))) 

# write  Function to Rotate  the matrix by 180 degree  and print the result.
def rotateMatrix(mat): 
    N = 3  
    i = N - 1;  
    while(i >= 0): 
        j = N - 1; 
        while(j >= 0): 
            print(mat[i][j], end = " "); 
            j = j - 1; 
        print(); 
        i = i - 1; 
  
mat = [[1, 2, 3], 
       [ 4, 5, 6 ], 
       [ 7, 8, 9 ]]; 
rotateMatrix(mat); 

# write  Function to left rotate n by d bits 
def leftRotate(n, d): 
    INT_BITS = 32
    return (n << d)|(n >> (INT_BITS - d)) 


n = 16
d = 2

print("Left Rotation of",n,"by",d,"is",end=" ") 
print(leftRotate(n, d)) 

# write Function to right rotate n by d bits  and print the result.
def rightRotate(n, d): 
    INT_BITS = 32

    return (n >> d)|(n << (INT_BITS - d)) & 0xFFFFFFFF

n = 16
d = 2

print("Right Rotation of",n,"by",d,"is",end=" ") 
print(rightRotate(n, d)) 

# Function to rotate string left and right by d length  and print the result.

def rotate(input,d): 

    Lfirst = input[0 : d] 
    Lsecond = input[d :] 
    Rfirst = input[0 : len(input)-d] 
    Rsecond = input[len(input)-d : ] 


    print ("Left Rotation : ", (Lsecond + Lfirst) ) 
    print ("Right Rotation : ", (Rsecond + Rfirst)) 

input = 'GeeksforGeeks'
d=2
rotate(input,d)  

# write Python3 code to demonstrate to create a substring from a string  and print the result.

ini_string = 'xbzefdgstb'

print ("initial_strings : ", ini_string) 

sstring_strt = ini_string[:2] 
sstring_end = ini_string[3:] 

print ("print resultant substring from start", sstring_strt) 
print ("print resultant substring from end", sstring_end) 

# write Python3 code to demonstrate to create a substring from string  and print the result.
ini_string = 'xbzefdgstb'
print ("initial_strings : ", ini_string) 
sstring_alt = ini_string[::2] 
sstring_gap2 = ini_string[::3] 

print ("print resultant substring from start", sstring_alt) 
print ("print resultant substring from end", sstring_gap2) 

# write Python3 code to demonstrate to create a substring from string and print the result. 
ini_string = 'xbzefdgstb'
sstring = ini_string[2:7:2] 
print ('resultant substring{sstring}') 

# Program to cyclically rotate an array by one  and print the result.

def cyclicRotate(input): 
    print ([input[-1]] + input[0:-1]) 

# write Python3 code to demonstrate list slicing from K to end using None  and print the result.
test_list = [5, 6, 2, 3, 9] 
K = 2
res = test_list[K : None] 
print (f"The sliced list is :{str(res)} "  ) 

# write Python code t get difference of two lists Using set() and print the result.
def Diff(li1, li2):
	return (list(list(set(li1)-set(li2)) + list(set(li2)-set(li1))))

li1 = [10, 15, 20, 25, 30, 35, 40]
li2 = [25, 40, 35]
print(Diff(li1, li2))

# write a program for round for integers and print the result.
integer = 18
print(f"Round off value : {round(integer , -1)}")

# write a program for floating pointwrite a program  and print the result.
print(f"Round off value : {round(51.6)}")

# write Program to demonstrate conditional operator  and print the result.
a, b = 10, 20
min = a if a < b else b 
print(min) 

# write Python program to demonstrate ternary operator using tuples, Dictionary and lambda and print the result.
a, b = 10, 20
print( (b, a) [a < b] ) 
print({True: a, False: b} [a < b]) 
print((lambda: b, lambda: a)[a < b]()) 

# write a python program using "any" function and print the result.
print (any([False, True, False, False])) 

# write a python program using "all" function and print the result.
print (all([False, True, False, False])) 

#write Python3 code to demonstrate working of Check if tuple has any None value using any() + map() + lambda  and print the result.
test_tup = (10, 4, 5, 6, None) 
res = any(map(lambda ele: ele is None, test_tup)) 
print("Does tuple contain any None value ? : " + str(res)) 

# write Python3 code to demonstrate working of Check if tuple has any None value using not + all()  and print the result.
test_tup = (10, 4, 5, 6, None) 
print("The original tuple : " + str(test_tup))  
res = not all(test_tup) 
print("Does tuple contain any None value ? : " + str(res)) 

# write Python3 code to demonstrate working of  Sort tuple list by Nth element of tuple  using sort() + lambda  and print the result.
test_list = [(4, 5, 1), (6, 1, 5), (7, 4, 2), (6, 2, 4)] 
print("The original list is : " + str(test_list)) 
N = 1
test_list.sort(key = lambda x: x[N]) 
print("List after sorting tuple by Nth index sort : " + str(test_list)) 

# write Python program to demonstrate printing of complete multidimensional list row by row.  and print the result.
a = [[2, 4, 6, 8, 10], [3, 6, 9, 12, 15], [4, 8, 12, 16, 20]] 
for record in a: 
	print(record) 

# write Python program to demonstrate that we can access multidimensional list using square brackets  and print the result. 
a = [ [2, 4, 6, 8 ], 
    [ 1, 3, 5, 7 ], 
    [ 8, 6, 4, 2 ], 
    [ 7, 5, 3, 1 ] ] 

for i in range(len(a)) : 
    for j in range(len(a[i])) : 
        print(a[i][j], end=" ") 
    print()	 

# write a program for Adding a sublist  and print the result.

a = [[2, 4, 6, 8, 10], [3, 6, 9, 12, 15], [4, 8, 12, 16, 20]] 
a.append([5, 10, 15, 20, 25]) 
print(a) 

#write a program for  Extending a sublist  and print the result.

a = [[2, 4, 6, 8, 10], [3, 6, 9, 12, 15], [4, 8, 12, 16, 20]] 
a[0].extend([12, 14, 16, 18]) 
print(a) 

# write a program for Reversing a sublist  and print the result.
a = [[2, 4, 6, 8, 10], [3, 6, 9, 12, 15], [4, 8, 12, 16, 20]] 
a[2].reverse() 
print(a) 

# write a Python3 program to demonstrate the use of replace() method  and print the result.

string = "geeks for geeks geeks geeks geeks"

print(string.replace("geeks", "Geeks")) 

print(string.replace("geeks", "GeeksforGeeks", 3)) 

# write Python3 code to demonstrate working of Rear word replace in String using split() + join()  and print the result.
test_str = "GFG is good"
print("The original string is : " + test_str) 
rep_str = "best"
res = " ".join(test_str.split(' ')[:-1] + [rep_str]) 
print("The String after performing replace : " + res) 

# write Python3 code to demonstrate working of Rear word replace in String using rfind() + join()  and print the result.
test_str = "GFG is good"
print("The original string is : " + test_str) 
rep_str = "best"
res = test_str[: test_str.rfind(' ')] + ' ' + rep_str 
print("The String after performing replace : " + res) 

# write Python3 code to demonstrate Shift from Front to Rear in List using list slicing and "+" operator  and print the result.
test_list = [1, 4, 5, 6, 7, 8, 9, 12] 
print ("The original list is : " + str(test_list)) 
test_list = test_list[1 :] + test_list[: 1] 
print ("The list after shift is : " + str(test_list)) 

# Python3 code to demonstrate Shift from Front to Rear in List using insert() + pop()  and print the result.
test_list = [1, 4, 5, 6, 7, 8, 9, 12] 
print ("The original list is : " + str(test_list)) 
test_list.insert(len(test_list) - 1, test_list.pop(0)) 
print ("The list after shift is : " + str(test_list)) 


# write Python3 code to demonstrate working of Sort by Rear Character in Strings List Using sort()  and print the result.

def get_rear(sub): 
    return sub[-1] 
test_list = ['gfg', 'is', 'best', 'for', 'geeks'] 
print("The original list is : " + str(test_list)) 
test_list.sort(key = get_rear) 
print("Sorted List : " + str(test_list)) 


# write Python3 code to demonstrate working of Sort by Rear Character in Strings List Using sorted() + lambda  and print the result.

test_list = ['gfg', 'is', 'best', 'for', 'geeks'] 

print("The original list is : " + str(test_list)) 

res = sorted(test_list, key = lambda sub : sub[-1]) 

print("Sorted List : " + str(res)) 


# write Python3 code to demonstrate Remove Rear K characters from String List using list comprehension + list slicing  and print the result.

test_list = ['Manjeets', 'Akashs', 'Akshats', 'Nikhils'] 

print("The original list : " + str(test_list)) 

K = 4

res = [sub[ : len(sub) - K] for sub in test_list] 

print("The list after removing last characters : " + str(res)) 


# write Python3 code to demonstrate Remove Rear K characters from String List using map() + lambda  and print the result.

test_list = ['Manjeets', 'Akashs', 'Akshats', 'Nikhils'] 

print("The original list : " + str(test_list)) 

K = 4

res = list(map(lambda i: i[ : (len(i) - K)], test_list)) 

print("The list after removing last characters : " + str(res)) 



# write Python3 code to demonstrate Kth Non-None String from Rear using next() + list comprehension  and print the result.

test_list = ["", "", "Akshat", "Nikhil"] 

print("The original list : " + str(test_list)) 
K = 2
test_list.reverse() 
test_list = iter(test_list) 
for idx in range(0, K): 
    res = next(sub for sub in test_list if sub) 

print("The Kth non empty string from rear is : " + str(res)) 


# write Python code to demonstrate Kth Non-None String from Rear using filter()  and print the result.

test_list = ["", "", "Akshat", "Nikhil"] 

print("The original list : " + str(test_list)) 

K = 2

res = list (filter(None, test_list))[-K] 

print("The Kth non empty string from rear is : " + str(res)) 

# write a program Creating a Dictionary  with Integer Keys  and print the result.
Dict = {1: 'Geeks', 2: 'For', 3: 'Geeks'} 
print("\nDictionary with the use of Integer Keys: ") 
print(Dict) 


# write a program Creating a Dictionary with Mixed keys  and print the result.
Dict = {'Name': 'Geeks', 1: [1, 2, 3, 4]} 
print("\nDictionary with the use of Mixed Keys: ") 
print(Dict) 

# write a program Creating an empty Dictionary  and print the result.
Dict = {} 
print("Empty Dictionary: ") 
print(Dict) 

# write a program Creating a Dictionary  with dict() method  and print the result.
Dict = dict({1: 'Geeks', 2: 'For', 3:'Geeks'}) 
print("\nDictionary with the use of dict(): ") 
print(Dict) 


# write a program Creating a Dictionary with each item as a Pair and print the result. 
Dict = dict([(1, 'Geeks'), (2, 'For')]) 
print("\nDictionary with each item as a pair: ") 
print(Dict) 

# write a program Creating a Nested Dictionary as shown in the below image  and print the result.
Dict = {1: 'Geeks', 2: 'For', 
        3:{'A' : 'Welcome', 'B' : 'To', 'C' : 'Geeks'}} 

print(Dict) 



# write a program Creating a Dictionary  and print the result.
Dict = {1: 'Geeks', 'name': 'For', 3: 'Geeks'} 

print("Accessing a element using get:") 
print(Dict.get(3)) 


#write a python Creating a Dictionary and  Accessing element using key  and print the result.
Dict = {'Dict1': {1: 'Geeks'}, 
    'Dict2': {'Name': 'For'}} 

print(Dict['Dict1']) 
print(Dict['Dict1'][1]) 
print(Dict['Dict2']['Name']) 

# write a program that uses delete function on  Dictionary  and print the result.
Dict = { 5 : 'Welcome', 6 : 'To', 7 : 'Geeks', 
        'A' : {1 : 'Geeks', 2 : 'For', 3 : 'Geeks'}, 
        'B' : {1 : 'Geeks', 2 : 'Life'}} 
print("Initial Dictionary: ") 
print(Dict) 

del Dict[6] 
print("\nDeleting a specific key: ") 
print(Dict) 

del Dict['A'][2] 
print("\nDeleting a key from Nested Dictionary: ") 
print(Dict) 


# write a rpogram Deleting an arbitrary key  using popitem() function in dictionary and print the result.
Dict = {1: 'Geeks', 'name': 'For', 3: 'Geeks'} 


pop_ele = Dict.popitem() 
print("\nDictionary after deletion: " + str(Dict)) 
print("The arbitrary pair returned is: " + str(pop_ele)) 

# write a  program for Deleting entire Dictionary  and print the result.
Dict = {1: 'Geeks', 'name': 'For', 3: 'Geeks'} 


Dict.clear() 
print("\nDeleting Entire Dictionary: ") 
print(Dict) 



# write a  Python3 code to demonstrate  set difference in dictionary list  using list comprehension  and print the result.

test_list1 = [{"HpY" : 22}, {"BirthdaY" : 2}, ] 
test_list2 = [{"HpY" : 22}, {"BirthdaY" : 2}, {"Shambhavi" : 2019}] 

print ("The original list 1 is : " + str(test_list1)) 
print ("The original list 2 is : " + str(test_list2)) 

res = [i for i in test_list1 if i not in test_list2] + [j for j in test_list2 if j not in test_list1] 

print ("The set difference of list is : " + str(res)) 

# write Python code to demonstrate sort a list of dictionary where value date is in string   and print the result.
ini_list = [{'name':'akash', 'd.o.b':'1997-03-02'}, 
            {'name':'manjeet', 'd.o.b':'1997-01-04'}, 
            {'name':'nikhil', 'd.o.b':'1997-09-13'}] 

print ("initial list : ", str(ini_list)) 

ini_list.sort(key = lambda x:x['d.o.b']) 

print ("result", str(ini_list)) 


# write a  Python3 code to demonstrate working of Convert Dictionaries List to Order Key Nested dictionaries Using loop + enumerate()  and print the result.

test_list = [{"Gfg" : 3, 4 : 9}, {"is": 8, "Good" : 2}, {"Best": 10, "CS" : 1}] 

print("The original list : " + str(test_list)) 

res = dict() 
for idx, val in enumerate(test_list): 
    res[idx] = val 

print("The constructed dictionary : " + str(res)) 

# write Python3 code to demonstrate working of Convert Dictionaries List to Order Key Nested dictionaries Using dictionary comprehension + enumerate() and print the result. 

test_list = [{"Gfg" : 3, 4 : 9}, {"is": 8, "Good" : 2}, {"Best": 10, "CS" : 1}] 

print("The original list : " + str(test_list)) 

res = {idx : val for idx, val in enumerate(test_list)} 
print("The constructed dictionary : " + str(res)) 

# write Python3 code to demonstrate working of Segregating key's value in list of dictionaries Using generator expression  and print the result.

test_list = [{'gfg' : 1, 'best' : 2}, {'gfg' : 4, 'best': 5}] 

print("The original list : " + str(test_list)) 

res = [tuple(sub["gfg"] for sub in test_list), 
    tuple(sub["best"] for sub in test_list)] 

print("Segregated values of keys are : " + str(res)) 


# write Python3 code to demonstrate working of Segregating key's value in list of dictionaries Using zip() + map() + values()  and print the result.

test_list = [{'gfg' : 1, 'best' : 2}, {'gfg' : 4, 'best': 5}] 

print("The original list : " + str(test_list)) 

res = list(zip(*map(dict.values, test_list))) 
 
print("Segregated values of keys are : " + str(res)) 

# write a  Python3 code to demonstrate working of Sort dictionaries list by Key's Value list index Using sorted() + lambda  and print the result.
 
test_list = [{"Gfg" : [6, 7, 8], "is" : 9, "best" : 10}, 
            {"Gfg" : [2, 0, 3], "is" : 11, "best" : 19}, 
            {"Gfg" : [4, 6, 9], "is" : 16, "best" : 1}] 
print("The original list : " + str(test_list)) 
K = "Gfg"
idx = 2
res = sorted(test_list, key = lambda ele: ele[K][idx]) 
print("The required sort order : " + str(res)) 

# write  Python3 code to demonstrate working of Sort dictionaries list by Key's Value list index Using sorted() + lambda (Additional parameter in case of tie) and print the result. 

test_list = [{"Gfg" : [6, 7, 9], "is" : 9, "best" : 10}, 
            {"Gfg" : [2, 0, 3], "is" : 11, "best" : 19}, 
            {"Gfg" : [4, 6, 9], "is" : 16, "best" : 1}] 
print("The original list : " + str(test_list)) 
K = "Gfg"
idx = 2
K2 = "best"
res = sorted(sorted(test_list, key = lambda ele: ele[K2]), key = lambda ele: ele[K][idx]) 
print("The required sort order : " + str(res)) 

# write Python3 code to demonstrate working of Convert List of Dictionaries to List of Lists Using loop + enumerate()  and print the result.

test_list = [{'Nikhil' : 17, 'Akash' : 18, 'Akshat' : 20}, 
            {'Nikhil' : 21, 'Akash' : 30, 'Akshat' : 10}, 
            {'Nikhil' : 31, 'Akash' : 12, 'Akshat' : 19}] 

print("The original list is : " + str(test_list)) 

res = [] 
for idx, sub in enumerate(test_list, start = 0): 
    if idx == 0: 
        res.append(list(sub.keys())) 
        res.append(list(sub.values())) 
    else: 
        res.append(list(sub.values())) 

print("The converted list : " + str(res)) 

# write a Python3 code to demonstrate working of Convert List of Dictionaries to List of Lists Using list comprehension and print the result. 

test_list = [{'Nikhil' : 17, 'Akash' : 18, 'Akshat' : 20}, 
            {'Nikhil' : 21, 'Akash' : 30, 'Akshat' : 10}, 
            {'Nikhil' : 31, 'Akash' : 12, 'Akshat' : 19}] 

print("The original list is : " + str(test_list)) 

res = [[key for key in test_list[0].keys()], *[list(idx.values()) for idx in test_list ]] 

print("The converted list : " + str(res)) 

# write a Python code demonstrate the working of sorted() with lambda and print the result.

lis = [{ "name" : "Nandini", "age" : 20}, 
{ "name" : "Manjeet", "age" : 20 },
{ "name" : "Nikhil" , "age" : 19 }]

print ("The list printed sorting by age: ")
print (sorted(lis, key = lambda i: i['age']))
print ("\r")

# write a Python3 code to demonstrate working of Extract dictionaries with values sum greater than K and print the result. 

test_list = [{"Gfg" : 4, "is" : 8, "best" : 9}, 
            {"Gfg" : 5, "is": 8, "best" : 1}, 
            {"Gfg" : 3, "is": 7, "best" : 6}, 
            {"Gfg" : 3, "is": 7, "best" : 5}] 

print("The original list : " + str(test_list)) 

K = 15

res = [] 
for sub in test_list: 
    sum = 0
    for key in sub: 
        sum += sub[key] 
    if sum > K: 
        res.append(sub) 

print("Dictionaries with summation greater than K : " + str(res)) 

# write Python3 program for illustration of values() method of dictionary  and print the result.

dictionary = {"raj": 2, "striver": 3, "vikram": 4} 
print(dictionary.values()) 

# write Python program to illustrate enumerate function and print the result. 
l1 = ["eat","sleep","repeat"] 
s1 = "geek"

obj1 = enumerate(l1) 
obj2 = enumerate(s1) 

print ("Return type:",type(obj1) )
print( list(enumerate(l1)) )

print( list(enumerate(s1,2)) )

# write Python program to illustrate  enumerate function in loops  and print the result.

l1 = ["eat","sleep","repeat"] 

for count,ele in enumerate(l1,100): 
    print (count,ele )

# write Python3 code to demonstrate working of  Merge Python key values to list  Using setdefault() + loop  and print the result.

test_list = [{'gfg' : 2, 'is' : 4, 'best' : 6}, 
            {'it' : 5, 'is' : 7, 'best' : 8}, 
            {'CS' : 10}] 

print("The original list is : " + str(test_list)) 

res = {} 
for sub in test_list: 
    for key, val in sub.items(): 
        res.setdefault(key, []).append(val) 

print("The merged values encapsulated dictionary is : " + str(res)) 


# write Python3 code to demonstrate working of Merge Python key values to list Using list comprehension + dictionary comprehension and print the result. 

test_list = [{'gfg' : 2, 'is' : 4, 'best' : 6}, 
            {'it' : 5, 'is' : 7, 'best' : 8}, 
            {'CS' : 10}] 

print("The original list is : " + str(test_list)) 

res = {key: list({sub[key] for sub in test_list if key in sub}) 
    for key in {key for sub in test_list for key in sub}} 

print("The merged values encapsulated dictionary is : " + str(res)) 

# write Python3 code to demonstrate working of Merge List value Keys to Matrix Using loop + pop() and print the result. 

test_dict = {'gfg' : [4, 5, 6], 
            'is' : [8, 8, 9], 
            'CS' : [1, 3, 8], 
            'Maths' : [1, 2]} 
 
print("The original dictionary : " + str(test_dict)) 

que_list = ['gfg', 'CS', 'Maths'] 

new_data = [test_dict.pop(ele) for ele in que_list] 
test_dict["merge_key"] = new_data 
 
print("The dictionary after merging : " + str(test_dict)) 

# write Python code to convert string to list  and print the result.

def Convert_1(string): 
    li = list(string.split(" ")) 
    return li 
 
str1 = "Geeks for Geeks"
print(Convert(str1)) 

# Python code to convert string to list  and print the result.
def Convert_2(string): 
    li = list(string.split("-")) 
    return li 

str1 = "Geeks-for-Geeks"
print(Convert(str1)) 

# write Python code to convert string to list character-wise  and print the result.
def Convert_3(string): 
    list1=[] 
    list1[:0]=string 
    return list1 

str1="ABCD"
print(Convert(str1)) 

# write Python3 code to demonstrate convert list of strings to list of tuples Using map() + split() + tuple()  and print the result.

test_list = ['4, 1', '3, 2', '5, 3'] 

print("The original list : " + str(test_list)) 

res = [tuple(map(int, sub.split(', '))) for sub in test_list] 

print("The list after conversion to tuple list : " + str(res)) 

# write Python3 code to demonstrate convert list of strings to list of tuples Using map() + eval  and print the result.

test_list = ['4, 1', '3, 2', '5, 3'] 
print("The original list : " + str(test_list)) 
res = list(map(eval, test_list)) 
print("The list after conversion to tuple list : " + str(res)) 

# write Python3 code to demonstrate Combining tuples in list of tuples Using list comprehension  and print the result.
test_list = [([1, 2, 3], 'gfg'), ([5, 4, 3], 'cs')] 
print("The original list : " + str(test_list)) 
res = [ (tup1, tup2) for i, tup2 in test_list for tup1 in i ] 
print("The list tuple combination : " + str(res)) 

# write Python3 code to demonstrate working of Add list elements to tuples list Using list comprehension + "+" operator  and print the result.
test_list = [(5, 6), (2, 4), (5, 7), (2, 5)] 
print("The original list is : " + str(test_list)) 
sub_list = [7, 2, 4, 6] 
res = [sub + tuple(sub_list) for sub in test_list] 
print("The modified list : " + str(res)) 


# write Python3 code to demonstrate working of Add list elements to tuples list Using list comprehension + "*" operator  and print the result.

test_list = [(5, 6), (2, 4), (5, 7), (2, 5)] 
print("The original list is : " + str(test_list)) 

sub_list = [7, 2, 4, 6] 
res = [(*sub, *sub_list) for sub in test_list] 
print("The modified list : " + str(res)) 

# write Python3 code to demonstrate conversion of list of tuple to list of list using list comprehension + join()  and print the result.

test_list = [('G', 'E', 'E', 'K', 'S'), ('F', 'O', 'R'), 
                            ('G', 'E', 'E', 'K', 'S')] 
print ("The original list is : " + str(test_list)) 
res = [''.join(i) for i in test_list] 
print ("The list after conversion to list of string : " + str(res)) 


# write Python3 code to demonstrate conversion of list of tuple to list of list using map() + join()  and print the result.

test_list = [('G', 'E', 'E', 'K', 'S'), ('F', 'O', 'R'), 
                            ('G', 'E', 'E', 'K', 'S')] 
print ("The original list is : " + str(test_list)) 
res = list(map(''.join, test_list)) 
print ("The list after conversion to list of string : " + str(res)) 


# write Python3 code to demonstrate working of Concatenating tuples to nested tuples using + operator + ", " operator during initialization  and print the result.
 
test_tup1 = (3, 4), 
test_tup2 = (5, 6), 
 
print("The original tuple 1 : " + str(test_tup1)) 
print("The original tuple 2 : " + str(test_tup2)) 
res = test_tup1 + test_tup2 
print("Tuples after Concatenating : " + str(res)) 

# write Python3 code to demonstrate working of Concatenating tuples to nested tuples Using ", " operator during concatenation  and print the result. 

test_tup1 = (3, 4) 
test_tup2 = (5, 6) 

print("The original tuple 1 : " + str(test_tup1)) 
print("The original tuple 2 : " + str(test_tup2)) 

res = ((test_tup1, ) + (test_tup2, )) 

print("Tuples after Concatenating : " + str(res)) 


# write Python code to demonstrate to remove the tuples if certain criteria met  and print the result.

ini_tuple = [('b', 100), ('c', 200), ('c', 45), 
                        ('d', 876), ('e', 75)] 

print("intial_list", str(ini_tuple))
result = [i for i in ini_tuple if i[1] <= 100] 
print ("Resultant tuple list: ", str(result)) 


# write Python code to demonstrate to remove the tuples if certain criteria met  and print the result.
ini_tuple = [('b', 100), ('c', 200), ('c', 45), 
                        ('d', 876), ('e', 75)] 
print("intial_list", str(ini_tuple)) 
result = list(filter(lambda x: x[1] <= 100, ini_tuple)) 
print ("Resultant tuple list: ", str(result)) 


# Python code to demonstrate to remove the tuples if certain criteria met  and print the result.
ini_tuple = [('b', 100), ('c', 200), ('c', 45), 
                        ('d', 876), ('e', 75)] 

print("intial_list", str(ini_tuple)) 
result = [] 
for i in ini_tuple: 
    if i[1] <= 100: 
        result.append(i) 
print ("Resultant tuple list: ", str(result)) 

# write Python code to demonstrate to remove the tuples if certain criteria met  and print the result.
ini_tuple = [('b', 100), ('c', 200), ('c', 45), 
                        ('d', 876), ('e', 75)] 
print("intial_list", str(ini_tuple)) 

result = [] 
for i in ini_tuple: 
    if i[1] <= 100: 
        result.append(i) 
print ("Resultant tuple list: ", str(result)) 


# write Python code to remove all strings from a list of tuples  and print the result.
listOfTuples = [('string', 'Geeks'), (2, 225), (3, '111'), (4, 'Cyware'), (5, 'Noida')]	 
output = [tuple(j for j in i if not isinstance(j, str)) for i in listOfTuples] 

print(output) 

# write Python3 code to demonstrate working of Extract Tuples with all Numeric Strings Using all() + list comprehension + isdigit()  and print the result.
test_list = [("45", "86"), ("Gfg", "1"), ("98", "10"), ("Gfg", "Best")] 
print("The original list is : " + str(test_list)) 
res = [sub for sub in test_list if all(ele.isdigit() for ele in sub)] 
print("Filtered Tuples : " + str(res)) 

# write Python3 code to demonstrate working of Extract Tuples with all Numeric Strings Using lambda + filter() + isdigit()  and print the result.
test_list = [("45", "86"), ("Gfg", "1"), ("98", "10"), ("Gfg", "Best")] 
print("The original list is : " + str(test_list)) 
res = list(filter(lambda sub : all(ele.isdigit() for ele in sub), test_list)) 
print("Filtered Tuples : " + str(res)) 

# write Python3 code to demonstrate working of Extract String till Numeric Using isdigit() + index() + loop  and print the result. 
test_str = "geeks4geeks is best"
print("The original string is : " + str(test_str)) 
temp = 0
for chr in test_str: 
    if chr.isdigit(): 
        temp = test_str.index(chr) 
print("Extracted String : " + str(test_str[0 : temp])) 

