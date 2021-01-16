def service_price():
    service = input('서비스 종류를 입력: a/b/c/: ')
    valueAdded = input('부가세를 포함? y/n: ')
    if valueAdded == 'y':
        if service == 'a':
            result = 23 * 1.1
        elif service == 'b':
            result = 40 * 1.1
        elif service == 'c':
            result = 67 * 1.1

    elif valueAdded == 'n':
        if service == 'a':
            result = 23
        elif service == 'b':
            result = 40
        elif service == 'c':
            result = 67

    print(round(result, 1), '만원 입니다.')

service_price()
