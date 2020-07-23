class FourDigitYearConverter:
    regex = r'\d{4}'

    def to_python(self,value): #꼭 네 자리를 입력받아야 하고 이를 숫자로 변형. 0234 입력시 234출력
        return int(value)
    def to_url(self,value): #다시 문자로 변환
        return '%04d' % value

