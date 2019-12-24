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

# if (x < 1) and (x > 12):
#     print("Введите номер месяца от 1 до 12")

    # try:
    #     (x < 1) and (x > 12)
    # except tuple index out of range:
    #     print("Введите номер месяца от 1 до 12")

def logic_calendar(y):
    y = int(x) - 1
    return y
print("Порядковый месяц " + str(x) + " это " + (year_rus[logic_calendar(x)]) + " по Аннглийски это " + (year_eng[logic_calendar(x)]))