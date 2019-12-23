year_rus = ("Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь")
year_eng = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
print("Введите порядковый номер любого месяца: ")
x = input()
def logic_calendar(y):
    y = x - 1
    return y
print(year_rus(y))