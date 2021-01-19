import re

example1 = '저는 91년에 태어났습니다. 97년에는 IMF가 있었습니다. 지금은 2021년입니다.'
print(re.findall(r'\d.+년', example1))  # 숫자로 시작, 어떤문자든 반복되며 '년'으로 끝나는 문자열 반환

print(re.findall(r'\d.+?년', example1)) # '년'이라는 글자를 찾으면 패턴 찾기 중단
print(re.findall(r'\d+.년', example1))  # 숫자를 반복시킨후 '년'으로 끄탄는 문자열 반환

example = '이동민 교수는 다음과 같이 설명했습니다(이동민, 2019). 그런데 다른 학자는 이 문제에 대해서 다른 견해를 가지고 있었습니다(최재영, 2019). 또 다른 견해도 있었습니다(Lion, 2018).'
result = re.findall(r'\(.+\)', example)
print(result)

result = re.findall(r'\(.+?\)', example)
print(result)
