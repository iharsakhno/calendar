year_rus = ("Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь")
year_eng = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")

while True:
    try:
        x=int(input("Введите порядковый номер любого месяца: "))
    except ValueError:
        print("This is not a whole number.")
        continue
    else:
        break

def logic_calendar(y):
    y = int(x) - 1
    return y
print("Порядковый месяц " + str(x) + " это " + (year_rus[logic_calendar(x)]) + " по Английски это " + (year_eng[logic_calendar(x)]))