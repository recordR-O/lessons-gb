#6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.

user_first = int(input("Введите результат начальной пробежки : "))
user_result = int(input("Введите желаемый результат : "))

day = 1

print(f"1-й день : {round(user_first, 2)}")

while user_first < user_result:
    user_first *= 1.1
    day += 1
    print(f"{day}-й день : {round(user_first, 2)}")

print(f"На {day}-й день вы достигните результата - не менее {user_result} км! ")



