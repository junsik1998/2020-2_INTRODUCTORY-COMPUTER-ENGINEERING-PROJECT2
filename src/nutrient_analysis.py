from datetime import datetime
import os
import urllib.request
import cv2
import time

menuList = {
    "일지 분석":["메인 메뉴로 이동","영양 정보 분석","유해 식품 검사"],
    "영양정보 분석":["일지 분석으로 이동","오늘 일지 분석", "날짜 지정해서 분석"]
}
#해당 날짜에 있는 식품의 섭취 영양소 리스트 반환 [], user=string형 date=int형
def Receive_nutrient_list(user,date):
    nutrient_list=[0,0,0,0,0,0,0,0,0]
    diary = open('./Users/'+user+'/diary/'+str(date)+'.txt','r', encoding='UTF8')
    foods=diary.readlines()
    
    for food in foods:
        food = food[:-1]
        #food의 nutrient 받아오기
        food_nutrient=foodInfo(food)
        for i in range(0,9):
            if food_nutrient[i+2]=='':
                continue
            nutrient_list[i] = nutrient_list[i] + float(food_nutrient[i+2])
    return nutrient_list


def ingest_high(nutname):
    print(nutname+"의 섭취량이 많습니다. 섭취량을 줄이세요.")

def ingest_middle(nutname):
    print(nutname+"의 섭취량이 적당합니다. 이 섭취량을 유지하세요.")

def ingest_low(nutname):
    print(nutname+"의 섭취량이 적습니다. 섭취량을 늘리세요.")


#영양 분석 함수
#user는 string형 date는 int형 list는 0:열량 1:탄수화물 2:단백질 3.지방 4.당류 5.나트륨 6.콜레스테롤 7.포화지방산 8.트렌스지방
def Nutrient(user,date, list):
    info_file=open('./Users/'+user+'/info.txt','r',encoding='UTF8')
    info=info_file.readlines()
    
    height=int(info[2][:-1])
    weight=int(info[3])
    sex=info[0][:-1]
    age=int(info[1][:-1])

    #사용자의 표준 체중, 열량, BMI
    stdweight=(height-100)*0.9
    stdcalorie=stdweight*35
    BMI=weight/(height*height)

    print('['+str(date),'영양 정보 분석]')
    print('섭취 영양소')
    print('열량:',str(list[0])+"kcal 탄수화물:",str(list[1])+"g 단백질:", str(list[2])+"g 지방:",str(list[3])+"g 당류:", str(list[4])+"g \n나트륨:", str(list[5])+"mg 콜레스테롤:", str(list[6])+"mg 포화지방산:", str(list[7])+"mg 트렌스지방:",str(list[8]))
    print('표준 섭취 열량: '+str(stdcalorie)+"kcal\t사용자가 섭취한 열량: "+str(list[0])+"kcal")

    #열량
    if(stdcalorie<list[0]):
        print("열량 섭취량이 많습니다. 섭취량을 줄이세요.")
    elif(stdcalorie>list[0]):
        print("열량 섭취량이 적습니다. 섭취량을 늘리세요.")
        
    #탄수화물
    std_calbo_low=stdcalorie*0.55
    std_calbo_high=stdcalorie*0.65
    if(std_calbo_high<list[1]):
        ingest_high('탄수화물')
    elif(std_calbo_low<list[1] and list[1]<=std_calbo_high):
        ingest_middle('탄수화물')
    else:
        ingest_low('탄수화물')
        
    #단백질
    std_protein_low=stdcalorie*0.3
    std_protein_high=stdcalorie*0.35
    if(std_protein_high<list[2]):
        ingest_high('단백질')
    elif(std_protein_low<list[2] and list[2]<=std_protein_high):
        ingest_middle('단백질')
    else:
        ingest_low('단백질')
        
    #지방
    if(BMI<=23):
        std_fat_low=stdcalorie*0.15
        std_fat_high=stdcalorie*0.30
        if(std_fat_high<list[3]):
            ingest_high('지방')
        elif(std_fat_low<list[3] and std_fat_high>=list[3]):
            ingest_middle('지방')
        else:
            ingest_low('지방')
    else:
        std_fat_low=stdcalorie*0.15
        std_fat_high=stdcalorie*0.25
        if(std_fat_high<list[3]):
            ingest_high('지방')
        elif(std_fat_low<list[3] and std_fat_high>=list[3]):
            ingest_middle('지방')
        else:
            ingest_low('지방')
    #당류
    if(age>13):
        if(list[4]>50):
            ingest_high('당류')
        else:
            ingest_middle('당류')
    else:
        if(list[4]>30):
            ingest_high('당류')
        else:
            ingest_middle('당류')
            
    #나트륨
    if(list[5]>5000):
        ingest_high('나트륨')
    else:
        ingest_middle('나트륨')
    #콜레스테롤
    if(sex=='남'):
        if(list[6]>300):
            ingest_high('콜레스테롤')
        else:
            ingest_middle('콜레스테롤')
    else:
        if(list[6]>219):
            ingest_high('콜레스테롤')
        else:
            ingest_middle('콜레스테롤')
    #포화지방산
    if(list[7]>15):
        ingest_high('포화지방산')
    else:
        ingest_middle('포화지방산')
    #트렌스지방
    if(list[8]>2):
        ingest_high('트렌스지방')
    else:
        ingest_middle('트렌스지방')
    print('')

#부프롬프트3.1.1: 오늘 일지 분석
def today_nutrient(user):
    print()
    today=datetime.today()
    today=int(str(today)[:10].replace('-',''))
    #입력받은 날짜에 해당하는 일지가 있는지
    isit=isthere(user,today)
    if(isit):
        nutrient_list=Receive_nutrient_list(user,today)
        Nutrient(user,today,nutrient_list)
    else:
        print('['+str(today)+'의 섭취 일지가 없습니다.]')
        print('1.'+str(today),'의 식품 섭취 일지를 작성합니다.')
        print('2. 영양 정보 분석으로 이동합니다.')
        select='3'
        while(select!='1' or select!='2'):
            select=input('>')
            if(select=='1'):
                #식품 섭취 일지 작성으로
                x=1
            elif(select=='2'):
                NutrientAnalysis(user)
            else:
                print('잘못 입력하였습니다.')

#입력받은 날짜가 8자리의 숫자일 경우 이 8자리 숫자가 날짜 형식인지 구분해준다. date=string형
def date_check(date):
    check=1
    y=int(date[:4])
    m=int(date[4:6])
    d=int(date[6:8])
    if(m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12):
        if(d>=1 and d<=31):check=1
        else: check=0
    elif(m==4 or m==6 or m==9 or m==11):
        if(d>=1 and d<=30):check=1
        else: check=0
    elif(m==2):
        if((y%4==0 and y%100!=0) or y%400==0):
            if(d>=1 and d<=29):check=1
            else: check=0
        else:
            if(d>=1 and d<=28):check=1
            else: check=0
    else:
        check=0
    return check

#해당 날짜에 해당하는 식품 섭취일지가 있는지 확인 (path만 바꾸어 주면 된다.) user=string형 date=int형
def isthere(user, date):
    file_path='./Users/'+user+'/diary'
    file_list= os.listdir(file_path)
    for i in range(0,len(file_list)):
        file_list[i]=file_list[i][:-4]
    if len(file_list)==0:return False
    if str(date) in file_list:
        return True
    else:
        return False
     
#부프롬프트3.1.2: 날짜 지정해서 분석
def range_nutrient(user):
    print('\n영양 정보 분석 날짜 입력')
    print('-날짜의 기본 형식은 YYYYMMDD인 8자리 정수로 한다.')
    print('날짜 범의로 입력은 "A~B"로 한다.(A와 B는 YYYYMMDD형식의 8자리 정수, A<=B)')
    print('날짜를 여러개 입력받을 때는 ","로 구분한다.')
    print('날짜를 세 개 입력 받는 경우의 예는 "A,B,C"로 한다.( A, B와 C는 YYYYMMDD형식의 8자리 정수)')
    print('숫자 0을 입력할 경우 영양정보분석으로 이동합니다.')
    
    date_list=[]
    
    #날짜 형식이 맞는지 확인
    while(1):
        check=1         #입력받은 문자가 날짜 형식이 아니면 check=0으로 반환
        date=input('>')
        date=date.replace(' ','')
        if(date=='0'):  #입력받은 문자가 '0'일 경우 부프롬프트3.1:영양정보분석으로 이동
              NutrientAnalysis(user)
        check_comma=date.split(',') #문자열에 ','가 있는지 확인
        for c in check_comma:
            check_tilde=c.split('~')    #문자열에 '~'가 있는지 확인
            if(len(check_tilde)==1):
                if(len(check_tilde[0])!=8):check=0
                else:
                    if not check_tilde[0].isdigit():check=0
                    else:
                        check=date_check(check_tilde[0])
                        if(check==1):
                            if int(check_tilde[0]) not in date_list:date_list.append(int(check_tilde[0]))
            elif(len(check_tilde)==2):
                for text in check_tilde:
                    if(len(text)!=8):check=0
                    if not text.isdigit():check=0
                if(check==1):
                    if(int(check_tilde[0])<=int(check_tilde[1])):
                        check=date_check(check_tilde[0])
                        check=date_check(check_tilde[1])
                    else:
                        check=0
                if(check==1):
                    for d in range(int(check_tilde[0]),int(check_tilde[1])+1):
                        if(date_check(str(d))==1):
                            if int(d) not in date_list:date_list.append(int(d))
                                
            else:
                check=0
        if(check==0):print('\n옳바른 입력 형식이 아닙니다.')
        else:
            break
    print()   
    #여기까지 온거면 날짜가 알맞은 형식으로 입력된 것이다.
    date_list.sort()
    for day in date_list:
        isit=isthere(user,day)
                    
        if(isit):
            nutrient_list=Receive_nutrient_list(user,day)
            Nutrient(user,day,nutrient_list)
        else:
            print(str(day),"에 해당하는 일지가 없습니다.\n")           

    check=input('0을 입력하면 영양정보 분석으로 이동합니다.\n>')
    while(check!='0'):
        print('잘못입력하였습니다.')
        check=input('0을 입력하면 영양정보 분석으로 이동합니다.\n>')
    
    NutrientAnalysis(user)


#부 프롬프트3.1: 영양정보 분석
def NutrientAnalysis(user):
    print()
    select='3'
    while(select!='0' and select!='1' and select!='2'):
        select=showMenu('영양정보 분석')
        if(select!='0' and select!='1' and select!='2'):
            print('\n잘못 입력하였습니다.\n')

    if(select=='0'):
        diary_analysis(user)
    elif(select=='1'):
        today_nutrient(user)
    else:
        range_nutrient(user)

#부 프롬프트3.2 유해 식품 검사
def harmfulFood(user):
    print()
    file_path='./Users/'+user+'/food'
    file_list= os.listdir(file_path)
    
    harmful_foods=[]
    for date in file_list:
        f=open('./Users/'+user+'/food/'+date,'r',encoding='UTF8')
        foods=f.readlines()
        for food in foods:
            food_list=[]
            food=food.replace('\n','')
            #food를 준식이 함수에 보낸다.return된 리스트를 food_list에 담는다.
            food_list=searchProductName(user,food)
            if len(food_list)==0:
                continue
            else:
                food_list.append(food_list)
                food_list.insert(0,date[:-4])
                food_list.insert(0,food)
                harmful_foods.append(food_list)

    index=1
    select='1'
    if(len(harmful_foods)==0):
        print('섭취한 유해식품이 없습니다.')
    else:
        for harm in harmful_foods:
            print(str(index)+'.\t'+harm[1],harm[0])
            index=index+1
        
        while(select!='0'):
            print('(숫자 ‘0’을 입력할 경우 메인 메뉴의 3. 식품 섭취 일지 분석하기로 이동)')
            select=input('자세히 알고 싶은 유해식품 index\n>')
            if(not select.isdigit() or 0>int(select) or int(select)>=index):
                print('잘못된 형식으로 입력하였습니다.\n')
                continue
            elif(select=='0'):
                print()
                break
            #select된 index에 대한 자세한 정보 보여주기
            print()
            print(harmful_foods[int(select)-1][0])
            print('섭취날짜:',(harmful_foods[int(select)-1][1]))
            print('회수 정보:',harmful_foods[int(select)-1][2])
            print('이미지 url:',harmful_foods[int(select)-1][3])
            print()
    


#부 프롬프트3: 일지 분석 명령
def diary_analysis(user):
    select=3
    while(select!='0'):
        select=showMenu('일지 분석')
        if(select=='1'):
            NutrientAnalysis(user)
        elif(select=='2'):
            harmfulFood(user)
        else:
            print('잘못 입력하였습니다.\n')
    if(select=='0'):
        #메인 메뉴로
        x=1

