a = int(input('Введите длину стороны : '))
b = int(input('Введите длину стороны : '))
c = int(input('Введите длину стороны : '))


if a + b > c and a + c > b and b + c > a:
    if a == b == c :
        print('Равносторонний')
    elif a == b or a == c or b == c:
        print('Равнобедренный')
    else:
        print('Разносторонний')
else:
    print('Треугольник не существует')
      