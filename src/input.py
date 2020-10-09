import re


def inputFoodName():
    while True:
        input_text = input('입력 > ')
        if input_text == '':
            return input_text
        return_text = ''
        find_text = re.findall(r'[가-힣\?\*]+', input_text)
        korean = re.findall(r'[가-힣]+', input_text)
        two_star = re.findall(r'\*{2,}', input_text)
        for temp in find_text:
            return_text += temp
        if input_text == return_text and len(return_text) <= 20 and korean and not two_star:
            return return_text
        elif input_text != return_text:
            print("입력 가능한 문자는 완전한 한글, 와일드카드 문자(?, *) 입니다.")
        else:
            if len(return_text) > 20:
                print("20글자 이하로 입력해주세요.")
            if not korean:
                print("완전한 한글 문자가 최소 1글자 이상 포함되어야 합니다.")
            if two_star:
                print("* 기호는 2개 이상 연속하여 입력할 수 없습니다.")


def inputProduct():
    while True:
        input_text = input('입력 > ')
        if input_text == '':
            return input_text
        return_text = ''
        find_text = re.findall(r'[가-힣a-zA-Z\s\?\*]+', input_text)
        korean_english = re.findall(r'[가-힣a-zA-Z]+', input_text)
        two_star = re.findall(r'\*{2,}', input_text)
        for temp in find_text:
            return_text += temp
        if input_text == return_text and len(return_text) <= 20 and korean_english and not two_star:
            return return_text
        elif input_text != return_text:
            print("입력 가능한 문자는 완전한 한글, 영문자, 와일드카드 문자(?, *) 입니다.")
        else:
            if len(return_text) > 20:
                print("20글자 이하로 입력해주세요.")
            if not korean_english:
                print("완전한 한글 문자 또는 영문자가 최소 1글자 이상 포함되어야 합니다.")
            if two_star:
                print("* 기호는 2개 이상 연속하여 입력할 수 없습니다.")


def inputBarcode():
    while True:
        input_text = input('입력 > ')
        barcode_text = ''
        return_text = ''
        find_text = re.findall(r'[0-9\s\-]+', input_text)
        number = re.findall(r'[0-9]+', input_text)
        for temp in find_text:
            barcode_text += temp
        for temp in number:
            return_text += temp
        if input_text == barcode_text and 5 <= len(return_text) <= 30:
            return return_text
        elif len(return_text) < 5 or len(return_text) > 30:
            print("숫자를 5개 이상 30개 이하로 입력해주세요.")
        else:
            print("입력 가능한 문자는 숫자, 공백, - 기호 입니다.")


def inputNumber(start, end):
    while True:
        try:
            number = int(input('입력 > '))
            if start <= number <= end:
                return number
            else:
                print(str(start) + "이상 " + str(end) + "이하의 숫자로 입력해 주세요.")
        except ValueError:
            print("숫자만 입력 가능합니다.")


def inputUser(type=''):
    if type == 'foodname':
        return inputFoodName()
    elif type == 'product':
        return inputProduct()
    elif type == 'barcode':
        return inputBarcode()
    else:
        return input()
