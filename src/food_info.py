import requests

food_info_path = "C:/Users/USER/Desktop/food_tank/"
food_info_name = "식품영양정보.txt"

def food_info(num_start,num_fin):
    key ="40afbe2975a0467d837e"
    url = "http://openapi.foodsafetykorea.go.kr/api/{}/I2790/json/{}/{}".format(key,num_start,num_fin)
    res = requests.get(url).json()
    food_info = res["I2790"]["row"]

    f = open(food_info_path+food_info_name,'a')
    for i in food_info:
        data = i['NUM']+","+i['DESC_KOR']+","+i['SERVING_SIZE']+","+\
        i['NUTR_CONT1']+","+i['NUTR_CONT2']+","+i['NUTR_CONT3']+","+\
        i['NUTR_CONT4']+","+i['NUTR_CONT5']+","+i['NUTR_CONT6']+","+\
        i['NUTR_CONT7']+","+i['NUTR_CONT8']+"\n"
        f.write(data)
    f.close()

def make_db(total):
    count = 1
    num1 = int(total/1000)
    num2 = total - num1*1000
    for i in range(1,num1+1):
        food_info(count,count+999)
        count += 1000
    food_info(num1*1000+1,total)

key ="40afbe2975a0467d837e"
url = "http://openapi.foodsafetykorea.go.kr/api/{}/I2790/json/{}/{}".format(key,1,1)
res = requests.get(url).json()
total_count = int(res['I2790']["total_count"])
f = open(food_info_path+food_info_name,'w')
f.write(str(total_count)+"\n")
f.close()

make_db(total_count)
