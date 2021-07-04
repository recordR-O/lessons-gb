# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.


user_sec = 0
user_hour = 0
user_min = 0

user_time = int(input("Введите время в секундах: "))

if user_time < 0:
    print("Время не может идти назад! (пока что :))")
elif user_time >= 3600:
    user_hour = user_time // 3600
    user_min = (user_time % 3600) // 60
    user_sec = (user_time % 3600) % 60
else:
    user_min = user_time // 60
    user_sec = user_time % 60

print(f"{user_hour}:{user_min}:{user_sec}")


