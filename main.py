print('всем привет вы зашли в игру викторина')
print('ответьте на следующие вопросы что бы выиграть')
print('1 раунд')

cxtnxbr = 0

vopros = ["СКОЛЬКО КОМНАТ В ДВУХКОМНАТНОЙ КВАРТИРЕ",
          "КАК ПОЛУЧИТЬ РОБУКСЫ",
          "СКОЛЬКО ЧЕЛОВЕК НА ЗЕМЛЕ",
          "ГДЕ НАХОДИТСЕ БУРДЖ-ХАЛИФА",
          "СКОЛЬКО ГЛАЗ У ЧЕЛОВЕКА",
          "СКОЛЬКО НОГ У ПАУКА"]


otvets = ["4",
          'на сайте',
          "8000000000",
          "в Дубае",
          "2",
          "8"]

print(vopros[0])
a = input('пишите ответ здесь: ')
if a.lower() == otvets[0].lower():
    print("правильный ответ")
    cxtnxbr += 1
else:
    print("неправильный ответ")
    cxtnxbr -= 1

print(vopros[1])
a = input('пишите ответ здесь: ')
if a.lower() == otvets[1].lower():
    print("правильный ответ")
    cxtnxbr += 1
else:
    print("неправильный ответ")
    cxtnxbr -= 1

print(vopros[2])
a = input('пишите ответ здесь: ')
if a.lower() == otvets[2].lower():
    print("правильный ответ")
    cxtnxbr += 1
else:
    print("неправильный ответ")
    cxtnxbr -= 1

print(vopros[3])
a = input('пишите ответ здесь: ')
if a.lower() == otvets[3].lower():
    print("правильный ответ")
    cxtnxbr += 1
else:
    print("неправильный ответ")
    cxtnxbr -= 1

print(vopros[4])
a = input('пишите ответ здесь: ')
if a.lower() == otvets[4].lower():
    print("правильный ответ")
    cxtnxbr += 1
else:
    print("неправильный ответ")
    cxtnxbr -= 1

print(vopros[5])
a = input('пишите ответ здесь: ')
if a.lower() == otvets[5].lower():
    print("правильный ответ")
    cxtnxbr += 1
else:
    print("неправильный ответ")
    cxtnxbr -= 1
print(cxtnxbr)

if cxtnxbr > 4:
    print("Это отличный результат! Ты много знаешь.")
elif cxtnxbr > 2:
    print("Неплохой результат! Как здорово, что тебе предстоит узнать ещё так много всего.")
else:
    print("Видимо, ты только начинаешь свой путь! Ты ещё много чего узнаешь о мире, где мы живём.")
