my_list=[1,2,"Li li","Hua hua","Ji ba","Shanghai","Beijing","Aomen"]

my_list.append("Sing")
print(my_list)

my_list.insert(-1,"Play")
print(my_list)


del my_list[-1]
print(my_list)

my_list.pop()
print(my_list)

my_list.pop(0)
print(my_list)

my_list.remove(2)
print(my_list)

my_list.sort()
print(my_list)

my_list.sort(reverse=True)
print(my_list)

my_list = sorted(my_list)
print(my_list)

my_list = sorted(my_list,reverse=True)
print(my_list)

my_list.reverse()
print(my_list)

print(len(my_list))