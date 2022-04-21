# import os 
import json
import requests
# if os.path.exists("course.json"):
#     with open("course.json", "r") as f:
#         s=f.read() 
#         data = json.loads(s)
# else:
response=requests.get("https://api.merakilearn.org/courses")
var1=response.json()
with open("course.json","w") as f:
    data_course=json.dump(var1,f, indent=4)
q=open("course.json","r")
s=q.read()
data=json.loads(s)
i=0
while i < len(data):
    print(str(i+1),data[i]["name"],data[i]["id"])
    i+=1
user=int(input("Enter the number :"))
print(var1[user-1]["name"])
idd=var1[user-1]["id"]
response1=requests.get("https://api.merakilearn.org/courses/"+str(idd)+"/exercises")
var2=response1.json()
with open("topic_details.json","w") as s:
    det=json.dump(var2,s,indent=4)
print(det)
q1=open("topic_details.json","r")
s1=q1.read()
data1=json.loads(s1)
i=0
while i<len(data1["course"]["exercises"]):
    print(str(i+1),data1["course"]["exercises"][i]["name"])
    i+=1
user1=int(input("Enter the number which you want:"))
i=0
while i<len(data1["course"]["exercises"][user1-1]["content"]):
    print(data1["course"]["exercises"][user1-1]["content"][i]["value"])
    i+=1
while user1<=len(data1["course"]["exercises"]):
    option=input("select the option next or pervious(n or p)")
    if option=="p":
        user1-=1
        if option=="p" and user1>1:
            print(data1["course"]["exercises"][user1]["name"],"\n")
            i=0
            while i<len(data1["course"]["exercises"][user1]["content"]):
                print(data1["course"]["exercises"][user1]["content"][i]["value"])
                i+=1
        else:
            i=0
            while i<len(data1):
                print(str(i+1),data1["course"]["exercises"][i]["name"])
                i+=1
       
    elif option=="n":
        user1+=1
        if option=="n" and user1<len(data1["course"]["exercises"]):
            print(data1["course"]["exercises"][user1]["name"],"\n")
            i=0
            while i<len(data1["course"]["exercises"][user1]["content"]):
                print(data1["course"]["exercises"][user1]["content"][i]["value"])
                i+=1
        if user1+1==len(data1["course"]["exercises"]):
            print("course datails completed")
            break
    else:
        print("Wrong option")
        break