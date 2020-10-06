import requests
import os

badfood_info_path = os.getcwd()
badfood_info_name = "유해식품정보.txt"

try:
    key = "40afbe2975a0467d837e"
    url = "http://openapi.foodsafetykorea.go.kr/api/{}/I0490/json/1/1".format(key)
    res = requests.get(url).json()

    check_badfood = os.path.isfile(badfood_info_path+badfood_info_name)
    if check_badfood == False:
        print("유해식품정보 파일을 생성합니다.")
        f = open(badfood_info_path+badfood_info_name,'w')
        f.write("0")
        f.close()

    if res['I0490']['RESULT']['CODE'] != 'INFO-000':
        print("API 호출 error 발생으로 유해식품정보 업데이트를 실패하였습니다.")
        print(res['I0490']['RESULT']['MSG'])
    else:
        total_count = int(res['I0490']['total_count'])
        f = open(badfood_info_path+badfood_info_name,'r')
        check_num = int(f.readline())
        f.close()
        if total_count != check_num:
            update_url = "http://openapi.foodsafetykorea.go.kr/api/{}/I0490/json/1/{}".format(key,total_count)
            update_res = requests.get(update_url).json()
            food_info = update_res['I0490']["row"]
            f = open(badfood_info_path+badfood_info_name,'w')
            f.write(str(total_count)+"\n")
            f.close()
            f = open(badfood_info_path+badfood_info_name,'a')
            for i in food_info:
                data = i['PRDTNM']
                data = data.replace(","," ")
                f.write(data+",")
                data = i['RTRVLPRVNS']
                data = data.replace(","," ")
                f.write(data+",")
                data = i['BSSHNM']
                data = data.replace(","," ")
                f.write(data+",")
                data = i['ADDR']
                data = data.replace(","," ")
                f.write(data+",")
                data = i['PRCSCITYPOINT_TELNO']
                data = data.replace(","," ")
                f.write(data+",")
                data = i['BRCDNO']
                data = data.replace(","," ")
                f.write(data+"\n")
            f.close()
            print("업데이트를 완료했습니다")
        else:
            print("변경된 정보가 없기 때문에 업데이트를 하지 않겠습니다.")
except requests.exceptions.ConnectionError:
    print("API 호출 error 발생으로 유해식품정보 업데이트를 실패하였습니다.\n")
    print("통신 오류입니다. 네트워크를 확인해주세요. ")
except json.decoder.JSONDecodeError as msg:
    print("API 호출 error 발생으로 유해식품정보 업데이트를 실패하였습니다.\n")
    print(msg)
