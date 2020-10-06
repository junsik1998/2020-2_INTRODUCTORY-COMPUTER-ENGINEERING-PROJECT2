import requests
import os

food_info_path = os.getcwd()
food_info_name = "식품영양정보.txt"

def food_info(num_start,num_fin):
    key ="40afbe2975a0467d837e"
    url = "http://openapi.foodsafetykorea.go.kr/api/{}/I2790/json/{}/{}".format(key,num_start,num_fin)
    res = requests.get(url).json()
    food_info = res["I2790"]["row"]

    f = open(food_info_path+food_info_name,'a')
    for i in food_info:
        data = i['NUM']
        data = data.replace(","," ")
        f.write(data+",")
        data = i['SERVING_SIZE']
        data = data.replace(","," ")
        f.write(data+",")
        data = i['NUTR_CONT1']
        data = data.replace(","," ")
        f.write(data+",")
        data = i['NUTR_CONT2']
        data = data.replace(","," ")
        f.write(data+",")
        data = i['NUTR_CONT3']
        data = data.replace(","," ")
        f.write(data+",")
        data = i['NUTR_CONT4']
        data = data.replace(","," ")
        f.write(data+",")
        data = i['NUTR_CONT5']
        data = data.replace(","," ")
        f.write(data+",")
        data = i['NUTR_CONT6']
        data = data.replace(","," ")
        f.write(data+",")
        data = i['NUTR_CONT7']
        data = data.replace(","," ")
        f.write(data+",")
        data = i['NUTR_CONT8']
        data = data.replace(","," ")
        f.write(data+"\n")
    f.close()

def make_db(total):
    count = 1
    num1 = int(total/1000)
    num2 = total - num1*1000
    for i in range(1,num1+1):
        food_info(count,count+999)
        count += 1000
    food_info(num1*1000+1,total)
    
try:
    key ="40afbe2975a0467d837e"
    url = "http://openapi.foodsafetykorea.go.kr/api/{}/I2790/json/{}/{}".format(key,1,1)
    res = requests.get(url).json()
    total_count = int(res['I2790']["total_count"])
    f = open(food_info_path+food_info_name,'w')
    f.write(str(total_count)+"\n")
    f.close()

    make_db(total_count)
except requests.exceptions.ConnectionError as msg:
    print("API 호출 error 발생으로 유해식품정보 업데이트를 실패하였습니다.\n")
    print("통신 오류입니다. 네트워크를 확인해주세요.")
except json.decoder.JSONDecodeError as msg:
    print("API 호출 error 발생으로 유해식품정보 업데이트를 실패하였습니다.\n")
    print(msg)
