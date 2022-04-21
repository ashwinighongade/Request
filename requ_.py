import json
import requests
def course():
    global var1
    response=requests.get("https://api.merakilearn.org/courses")
    var1=response.json()
    with open("course1.json","w") as f:
        data=json.dump(var1,f, indent=4)
    serial=1
    for i in var1:
        print(serial,i["name"],i["id"])
        serial+=1
course()
user=int(input("Enter the number :"))
print(var1[user-1]["name"])
def topic_det(): 
    global var2
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
topic_det()
# user1=input("what do you want pervious or next(n/p) :")
# if user1=="p":
#     ser