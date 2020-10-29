import requests
import os

food_info_path = "./"
food_info_name = "식품영양정보.txt"

def food_info(num_start,num_fin):
    key ="40afbe2975a0467d837e"
    url = "http://openapi.foodsafetykorea.go.kr/api/{}/I2790/json/{}/{}".format(key,num_start,num_fin)
    res = requests.get(url).json()
    food_info = res["I2790"]["row"]

    f = open(food_info_path+food_info_name,'a',encoding="utf-8")
    for i in food_info:
        data = i['NUM']
        data = data.replace(",","")
        data = data.replace(" ","")
        f.write(data+",")
        data = i['DESC_KOR']
        data = data.replace(",","")
        data = data.replace(" ","")
        f.write(data+",")
        data = i['SERVING_SIZE']
        data = data.replace(",","")
        data = data.replace(" ","")
        f.write(data+",")
        data = i['NUTR_CONT1']
        data = data.replace(",","")
        data = data.replace(" ","")
        f.write(data+",")
        data = i['NUTR_CONT2']
        data = data.replace(",","")
        data = data.replace(" ","")
        f.write(data+",")
        data = i['NUTR_CONT3']
        data = data.replace(",","")
        data = data.replace(" ","")
        f.write(data+",")
        data = i['NUTR_CONT4']
        data = data.replace(",","")
        data = data.replace(" ","")
        f.write(data+",")
        data = i['NUTR_CONT5']
        data = data.replace(",","")
        data = data.replace(" ","")
        f.write(data+",")
        data = i['NUTR_CONT6']
        data = data.replace(",","")
        data = data.replace(" ","")
        f.write(data+",")
        data = i['NUTR_CONT7']
        data = data.replace(",","")
        data = data.replace(" ","")
        f.write(data+",")
        data = i['NUTR_CONT8']
        data = data.replace(",","")
        data = data.replace(" ","")
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

def mk_food():
    try:
        key ="40afbe2975a0467d837e"
        url = "http://openapi.foodsafetykorea.go.kr/api/{}/I2790/json/{}/{}".format(key,1,1)
        res = requests.get(url).json()
        check_food = os.path.isfile(food_info_path+food_info_name)

        if check_food == False:

            print("식품영양정보 파일을 생성합니다.")
            f = open(food_info_path+food_info_name,'w',encoding="utf-8")
            f.write("0")
            f.close()

        if res['I2790']['RESULT']['CODE'] != 'INFO-000':
            print("API 호출 error 발생으로 식품영양정보 업데이트를 실패하였습니다.")
            print(res['I2790']['RESULT']['MSG'])

        else:
            total_count = int(res['I2790']["total_count"])
            f = open(food_info_path+food_info_name,'r',encoding="utf-8")
            check_num = int(f.readline())
            f.close()
            if total_count != check_num:
                f = open(food_info_path+food_info_name,'w',encoding="utf-8")
                f.write(str(total_count)+"\n")
                f.close()
                make_db(total_count)
                print("식품영양정보 파일 업데이트를 완료했습니다")
            #else:
                #print("식품영양정보 파일의 변경된 정보가 없기 때문에 업데이트를 하지 않겠습니다.")
    except requests.exceptions:
        print("API 호출 error 발생으로 식품영양정보 업데이트를 실패하였습니다.")
        print("통신 오류입니다. 네트워크를 확인하십시오. ")
