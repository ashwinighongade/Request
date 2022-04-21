import json
import requests
import os
if os.path.exists("course.json"):
    with open("course.json", "r") as f:
        s=f.read() 
        var1 = json.loads(s)
else:
    def course_details():
        global data
        url=requests.get("https://api.merakilearn.org/courses")
        data=url.json()
        b=open("new.json","w")
        c=json.dump(data,b,indent=4)
        i=0
        while i<len(data):
            print((i+1),".",data[i]["name"],data[i]["id"])
            i+=1
        print()
    course_details()
    course_name=int(input("Enter the number which course do your want details :"))
    print(data[course_name-1]["name"])
    print(course_name)

    def topic_details():
        global main_list
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
    # user1=input("what do you want pervious or next(n/p/c) :")
    def option():
        if user1=="p":  
            course_details() 
        elif user1=="c":
            topic_details()
            
        else:
            print(data[course_name]["name"],data[course_name]["id"])

    user1=input("what do you want pervious or next(n/p/c) :")
    option()
    # i=0
    # while 
    def parent_exer():
        global a
        for j in range(0,len(main_list)):
            if topic_no==j+1:
                print(topic_no,main_list[j]["name"])
                a=main_list[j]["parent_exercise_id"]
    topic_no=int(input("select option which parent exericese do you want  :"))
    parent_exer()
    def parent_ch():
        global sub2
        c=1
        sub1=[]
        sub2=[]
        for i in range(0,len(main_list)):
            if main_list[i]["parent_exercise_id"]==a:
                print(" ",c,main_list[i]["name"])
                sub1.append(main_list[i]["name"])
                sub2.append(main_list[i]["content"])
                c+=1
    def option1():
        if user2=="p":
            topic_details()
        else:
            parent_ch()
    user2=input("what do you want pervious or next(p/c) :")
    option1()
    def child_exer():
        print("child data is",topic_no)
        print()
        print(sub2[ch_user-1])
    ch_user=int(input("Enter the child exercise content do you want :"))
    child_exer()

