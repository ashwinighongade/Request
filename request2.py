import json
import requests
url=requests.get("https://api.merakilearn.org/courses")
data=url.json()
b=open("new.json","w")
c=json.dump(data,b,indent=4)
i=0
while i<len(data):
    print((i+1),".",data[i]["name"],data[i]["id"])
    i+=1
print()
course_name=int(input("Enter the number which is your want :"))
print(data[course_name-1]["name"])
print(course_name)
url1=requests.get("https://api.merakilearn.org/courses/"+str(data[course_name-1]["id"])+"/exercises")
data1=url1.json()
b1=open("details1.json","w")
f=json.dump(data1,b1,indent=4)
main_list=[]
j=0
k=1
for i in data1["course"]["exercises"]:
    if i["parent_exercise_id"]==[]:
        j+=1
        main_list.append(i)
    if i["parent_exercise_id"]==i["id"]:
        print(j+1,".",i["name"])
        main_list.append(i)
        j+=1
    if i["parent_exercise_id"]!=i["id"]:
        print(" ",k,".",i["name"])
        main_list.append(i)
        k+=1
with open("main.json","w") as f:
    json.dump(main_list,f,indent=4)
print()
topic_no=int(input("select the option  :"))
for j in range(0,len(main_list)):
    if topic_no==j+1:
        print(topic_no,main_list[j]["name"])
        a=main_list[j]["parent_exercise_id"]
c=1
sub1=[]
sub2=[]
for i in range(0,len(main_list)):
    if main_list[i]["parent_exercise_id"]==a:
        print(" ",c,main_list[i]["name"])
        sub1.append(main_list[i]["name"])
        sub2.append(main_list[i]["content"])
        c+=1
ch_user=int(input("Enter the number :"))
print()
print("child data is",topic_no)
print()
print(sub2[ch_user-1])
