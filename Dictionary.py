dict1 = {"name" : "Aayan", "age" : 13, "grade" : "Eighth"}
#Printing
print(dict1)
print(dict1["name"])
print(dict1["age"])
#Editing
dict1["name"] = "Tawseef"
dict1["grade"] = "Ninth"
print(dict1)
dict1["birthday"] = "19th"
print(dict1)
#Popping and clearing
dict1.pop("name")
print(dict1)
dict1.popitem()
print(dict1)
dict1.clear()
print(dict1)
del dict1
#Student id
student_id = {"id1" : {"name" : ["Tawseef"], "grade" : ["VIII"], "subjects" : ["English", "Math", "Science"]}, "id2" : {"name" : ["Mamun"], "grade" : ["VIII"], "subjects" : ["English", "Math", "Science"]}, "id3" : {"name" : ["Aayan"], "grade" : ["VIII"], "subjects" : ["English", "Math", "Science"]}}
result = {}
for key, value in student_id.items():
    if value not in result.values():
        result[key] = value
print(result)
dict2 = {"Codingal": 2, "Is" : 2, "Best" : 1}
num = 2
count = 0
for key in dict2:
    if dict2[key] == num:
        count += 1
#Country code
print("Frequency of 2 is:", count)
dict3 = {"India" : "0091", "Nepal" : "00977", "Australia" : "0025", "Bangladesh" : "00880"}
print("Country code of India: ")
print(dict3.get("India", "Not found"))
print("Country code of Japan: ")
print(dict3.get("Japan", "Not found"))