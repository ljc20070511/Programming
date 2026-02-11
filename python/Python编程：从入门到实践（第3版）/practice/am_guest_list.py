Guest_list = ["Li li","Hua hua","Ba ga"]
print(Guest_list,",Let's share a supper with sb.")

print(Guest_list[2],"can't go there.")
Guest_list.pop()
Guest_list.append("Ji fang")
print(Guest_list,",Let's share a supper with sb.")

print("I find a bigger table.")
Guest_list.insert(0,"Dong dong")
Guest_list.insert(2,"Ji hang")
Guest_list.append("Ji bang")
print(Guest_list,",Let's share a supper with sb.")

print("I only two guests can be invited to dinner.")
Guest_list.pop(0)
print("Sorry , you can't go there.")
Guest_list.pop(0)
print("Sorry , you can't go there.")
Guest_list.pop(0)
print("Sorry , you can't go there.")
Guest_list.pop(0)
print("Sorry , you can't go there.")
print(f"{Guest_list[0]} and {Guest_list[0]} , you are still invited.")
del Guest_list[0]
del Guest_list[0]
print(Guest_list)