dic = {}
n = int(input("Enter number of elements : "))

a = list(input("\nEnter the numbers : ").split())

print("\nList is : ", a)

for i in a:
    if i not in dic.keys():
        dic[i] = 1
    else:
        dic[i] = dic[i] + 1
print("\nDictionary:", dic)
l2 = [[k, v] for k, v in dic.items()]
l3 = [(k, v) for k, v in dic.items()]
print("\nList of list:", l2)
print("\nList of tuples:", l3)
