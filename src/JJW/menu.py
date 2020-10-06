startMenu = {
    0:"프로그램 종료", 
    1:"회원가입", 
    2:"로그인"}
    
mainMenu = {
    0:"프로그램 종료", 
    1:"일지 작성", 
    2:"일지 불러오기", 
    3:"일지 분석", 
    4:"유해식품 검색"}

loadDairyMenu = {
    0:"메인메뉴로 돌아가기",
    1:"일지 수정하기",
    2:"일지 삭제하기"
}

def showMenu(menu):
    for idx, menu in menu.items():
        print(idx, menu)