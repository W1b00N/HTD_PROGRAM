# tuple1 = (1, 2, 3, 4, 5)
# tuple2 = ("a", "b", "c")
# tuple3 = (1, 2, 3.14, "a", "b", "c")
# # print(tuple1)
# print(type(tuple1))  # การเช็คชนิดข้อมูล
# print(tuple3[2]) #อ่านข้อมูลจากตำแหน่งที่กำหนด
# print(tuple3[3:])
# print('b' in tuple3)

# dict1 = {
#     "name": "wibun",
#     "weight": 72,
#     "year": 2011,
#     "color": ["orange", "black", "pink"],
# }
# # print(dict1["color"][1])
# # print(dict1["name"]+str(dict1['weight']))
# dict1["weight"] = 75  # แก้ไขค่าภายใน
# dict1["high"] = 176  # เพิ่มข้อมูลใน dictionaries
# dict1.update({"weight": 76, "high": 174})  # update dictionary
# del dict1["color"]  # delete
# dict1.clear()  # clear

# dict2 = {
#     "firstname": "wibun",
#     "lastname": "ranu",
#     "email": "wibun@gmail.com",
#     "height": 176,
# }
# print(len(dict2))
# print(len(dict2.keys()))
# print(len(dict2.values()))

# print("firstname" in dict2)
# print("firstname" in dict2.keys())
# print("176" in dict2.values())
# set1 = {1, 2, 3, 4, 5}
# set2 = {1, 2, 3, 4, 5, "a", "b", "c", "d"}
# # print(set2)  # แสดงผลค่าที่มีภายใน
# # for i in set2:
# #     print(i)

# set2.add("You")
# print(set2)
# set2.update({26, "F"})
# set2.remove("You")
# set2.clear()
# print(set2)
setA = {1, 2, 3, 4, 5}
setB = {3, 4, 5, 6, 7}

#union set
print(setA | setB) # ตัวที่ซ้ำนับครั้งเดียว
# intersection set
print(setA & setB) # แสดงเฉพาะตัวที่เหมือนกัน
# difference set
print(setA - setB)
# symmertric difference
print(setA ^ setB)


