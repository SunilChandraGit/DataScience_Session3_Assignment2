'''Implement List comprehensions to produce the following lists.
Write List comprehensions to produce the following Lists
['A', 'C', 'A', 'D', 'G', 'I', ’L’, ‘ D’]
['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz']
['x', 'y', 'z', 'xx', 'yy', 'zz', 'xx', 'yy', 'zz', 'xxxx', 'yyyy', 'zzzz']
[[2], [3], [4], [3], [4], [5], [4], [5], [6]]
[[2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8]]
[(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]'''

#list1 to print each letter of "ACADGILD" in a list
list1 = [l for l in "ACADGILD"]

#print list1
print(list1)

#list2 to print each letter "xyz" , 1 to 4 times each grouped by letters
list2 = [x*y for x in "xyz" for y in range(1,5)]

#print list2
print(list2)

#list2 to print each letter "xyz" , 1 to 4 times each grouped by number of times they are printed
list3 = [x*y for y in (1,2,2,4) for x in "xyz"]

#print list3
print(list3)

#list4 for list of list of single numbers 
list4 = [[x+y] for x in range(1, 4) for y in range(1,4)]

#print list4
print(list4)

#list4 for list of list of numbers 
list5 = [[x+y for x in range(1,5)] for y in range(1,5)]

#print list5
print(list5)

#print cartesian set of two from 1 to 3  
list6=[(y, x) for x in range(1, 4) for y in range(1,4)]

#print list6
print(list6)