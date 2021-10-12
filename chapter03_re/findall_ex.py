import re

# 두사람의 주민등록번호 앞 여섯자리만 추출하는 패턴
number = 'My number is 511223-1****** and yours is 521012-2******'

# '\d{6}' 패턴은 숫자를 여섯번 반복한 값 의미 
print(re.findall('\d{6}', number))
