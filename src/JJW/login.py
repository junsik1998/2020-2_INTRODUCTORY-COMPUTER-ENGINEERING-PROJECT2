import os
from check import *

def login():
    os.system("clear")
    id = input("ID : ")

    if existID(id):
        directory = "./Users/"+id
        f = open(directory+"/password.txt", 'r')
        userPW = f.readline()

        pw = input("패스워드 : ")
        if userPW == pw:
            print(f"로그인에 성공했습니다.")
            return id
        else : 
            print("비밀번호가 다릅니다. 다시 시도해주세요.")
            return None
    else:
        return None

def signUp():
    # ID 입력
    while True:
        id = input("사용하실 아이디를 입력해주세요 ")
        if checkID(id):
            break

    # user directory 생성
    directory = "./Users/"+id
    os.makedirs(directory)
    os.makedirs(directory+"/diary") # 추가
    os.makedirs(directory+"/food") # 추가

    # PW 입력
    while True:
        pw = input("사용하실 비밀번호를 입력해주세요 ")
        if checkPW(pw):
            break
    
    # password.txt 생성
    f = open(directory+"/password.txt", 'w')
    f.write(pw)
    f.close()

    while True:
        sex = input("성별 : ")
        if checkSex(sex):
            break

    f = open(directory+"/info.txt", "w")
    f.write(converSex(sex)+"\n")

    while True:
        age = input("나이 : ")
        if checkAge(age):
            break
    f.write(age+"\n")

    while True:
        height = input("키 : ")
        if checkHeight(height):
            break
    f.write(height+"\n")

    while True:
        weight = input("몸무게 : ")
        if checkWeight(weight):
            break
    f.write(weight)

    f.close()
    