
import json
import requests
response=requests.get("https://api.merakilearn.org/courses")
var1=response.json()
with open("course1.json","w") as f:
    data=json.dump(var1,f, indent=4)
serial=1
for i in var1:
    print(serial,i["name"],i["id"])
    serial+=1
user=int(input("Enter the number :"))
print(var1[user-1]["name"])
response1=requests.get("https://api.merakilearn.org/courses/"+str(var1[user-1]["id"])+"/exercises")
var2=response1.json()
with open("topic_details1.json","w") as s:
    data1=json.dump(var2,s,indent=4)
    serial1=1
    list1=[]
    list2=[]
for j in var2["course"]["exercises"]:
    if j["parent_exercise_id"]==None:
        print(" ",serial1,j["slug"])
        serial1+=1
        new_no=1
        list1.append(j)
        list2.append(j)
        continue
    if j["parent_exercise_id"]==j["id"]:
        print(serial1,j["name"])
        serial1+=1
        new_no=1
        list1.append(j)
    for l in var2["course"]["exercises"]:
        if j["parent_exercise_id"]!=j["id"]:
            print("  ",new_no,j["name"])
            new_no+=1
            list2.append(j)
            break
user1=input("what do you want pervious or next(n/p) :")
if user1=="p":
    serial=1
    for i in var1:
        print(serial,i["name"],i["id"])
        serial+=1
    user=int(input("Enter the number :"))
    print(var1[user-1]["name"])
    response1=requests.get("https://api.merakilearn.org/courses/"+str(var1[user-1]["id"])+"/exercises")
    var2=response1.json()
    with open("topic_details1.json","w") as s:
        data1=json.dump(var2,s,indent=4)
        serial1=1
        list1=[]
        list2=[]
    for j in var2["course"]["exercises"]:
        if j["parent_exercise_id"]==None:
            print(" ",serial1,j["slug"])
            serial1+=1
            new_no=1
            list1.append(j)
            list2.append(j)
            continue
        if j["parent_exercise_id"]==j["id"]:
            print(serial1,j["name"])
            serial1+=1
            new_no=1
            list1.append(j)
        for l in var2["course"]["exercises"]:
            if j["parent_exercise_id"]!=j["id"]:
                print("  ",new_no,j["name"])
                new_no+=1
                list2.append(j)
                break
    with open("list2.json","w") as f:
        json.dump(list2,f,indent=4)
    with open("list1.json","w") as f:
        json.dump(list1,f,indent=4)

    with open("topic_details1.json","w") as s:
        json.dump(list1,s,indent=4)
    parent=int(input("Enter the parent exercise which is you want :"))
    for k in list1:
        if k["parent_exercise_id"]==k["id"]:
            print(list1[parent-1]["name"])
            num=(list1[parent-1]["name"])
            val=[]
            val3=[]
            new_no1=1
            for i in list2:
                if i["parent_exercise_id"]==num:
                    print(" ",new_no1,i["name"])
                    val.append(i["name"])
                    val3.append(i["content"])
                    new_no1+=1
    child=int(input("Enter the chile exercise which is you want: "))
    new_no2=1
    for s in range(0,len(val)):
        if child==new_no2:
            print(val[s])
            print(val3[s])
        new_no2+=1
elif user1=="n":
    with open("topic_details1.json","w") as s:
        json.dump(list1,s,indent=4)
    parent=int(input("Enter the parent exercise which is you want :"))
    for k in list1:
        if k["parent_exercise_id"]==k["id"]:
            print(list1[parent-1]["name"])
            num=(list1[parent-1]["name"])
            val=[]
            val3=[]
            new_no1=1
            for i in list2:
                if i["parent_exercise_id"]==num:
                    print(" ",new_no1,i["name"])
                    val.append(i["name"])
                    val3.append(i["content"])
                    new_no1+=1
    child=int(input("Enter the chile exercise which is you want: "))
    new_no2=1
    for s in range(0,len(val)):
        if child==new_no2:
            print(val[s])
            print(val3[s])
        new_no2+=1



