from input import inputNumber

menuList = {
    "시작 메뉴":["프로그램 종료", "회원가입", "로그인"],
    "메인 메뉴":["프로그램 종료", "일지 작성", "일지 불러오기", "일지 분석", "유해식품 검색"],
    "일지 불러오기 메뉴":["메인 메뉴로 돌아가기", "일지 수정하기", "일지 삭제하기"],
    "유해식품 검색 메뉴":["메인 메뉴로 이동", "제품명으로 검색", "바코드 번호로 검색"],
    "일지 분석":["메인 메뉴로 이동","영양 정보 분석","유해 식품 검사"],
    "영양정보 분석":["일지 분석으로 이동","오늘 일지 분석", "날짜 지정해서 분석"]
}
def showStartMenu(menuName):
    print("[" + menuName + "]")
    for i in range(len(menuList[menuName])):
        print(i, ".", menuList[menuName][i])
    return input("입력 > ")

def showMenu(menuName):
    print("[" + menuName + "]")
    for i in range(len(menuList[menuName])):
        print(i, ".", menuList[menuName][i])
    return inputNumber(0, len(menuList[menuName]) - 1)
