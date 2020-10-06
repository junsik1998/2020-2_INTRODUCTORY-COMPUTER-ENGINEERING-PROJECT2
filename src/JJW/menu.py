menuList = {
    "시작 메뉴":["프로그램 종료", "회원가입", "로그인"],
    "메인 메뉴":["프로그램 종료", "일지 작성", "일지 불러오기", "일지 분석", "유해식품 검색"],
    "일지 불러오기 메뉴":["메인메뉴로 돌아가기", "일지 수정하기", "일지 삭제하기"],
}

def showMenu(menuName):
    print(menuName)
    for i in range(len(menuList[menuName])):
        print(i, menuList[menuName][i])
    return input("번호를 선택해주세요.")
