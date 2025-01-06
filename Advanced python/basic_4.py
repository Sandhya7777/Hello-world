# # # int a[10]
# '''
# 1. list = [1,2,3,4]
# 2. tuple = (1,2,3,4,5,6)
# 3. dictonary = {key1: value1, key2: value2, key3:value4}
# {
# "name": "Aritra",
# "title": "Chakraborty",
# "address": "Newtown"
# }
# 4. set = {1,2,3,4,5, "Aritra", "Chakraborty"} a = set()
# '''
# # a = [1,2,3,4, "Aritra", "Chakraborty", [1,2,3,4,5]]
# # # print(a)
# # # k = a.pop()
# # # print(k)
# # # print(a)

# # # # a.insert(4, "inserted data")
# # # # print(a)
# # # # print(a.remove("A"))
# # # # print(a)
# # # a.pop(3)
# # # print(a)

# # # int a[10][10] = [[1,2,3,4],[5,6,7,8]]


# #                 #    0         1          2 3 4
# # # a = [[1,2,3,4], ["Aritra", "Chakraborty", 4,5,6], [9,0,1,2]]
# # #         #  0           1                                  2


# # # print(a[1][2])
# # #    0 1 2 3 4
# # # a = (1,2,3,3,5, [1,2,3,4])
# # # b = ("Aritra", "Chakraborty")

# # # c = [1,2,3,3,5]
# # # d = ["Aritra", "Chakraborty"]
# # # a[5].append(5)
# # # print(a)

# # a = {
# #     "name": "Aritra",
# #     "title": "Chakraborty",
# #     "pin": 7000102,
# #     "address": {
# #         "current":{
# #             "location": "Kolkata",
# #             "pin": 700102
# #         },
# #         "permanent":{
# #             "location": "Newtown",
# #             "pin": 700162
# #         }
# #     },
# # }
# # print(dir(a))

# # print(a["address"]["current"].get("locality", "Not found"))

a = {1,2,3,4,5,5,5,6,6,6,6,6, "Aritra"}

lst = [1,2,3,4,5,6,6,6,6,6,0,0,0,111,111, "Aritra", "Aritra"]

# for i in range(0,len(lst)):
#     if lst[i] in lst:
#         lst.pop(i)

ab = {1,2,3,4,5,6}
cd = {4,5,6}

set_lst = set(lst)

print(cd.issubset(ab))

