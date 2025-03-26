import random

# Генерація випадкового числа від 1 до 50
random_number = random.randint(1, 50)

print("Я загадав число від 1 до 50. Спробуйте вгадати!")

# Змінна для зберігання числа, яке вводить користувач
user_guess = None

# Цикл триває, поки користувач не вгадає число
while user_guess != random_number:
    # Вводимо число від користувача
    user_guess = int(input("Введіть ваше число: "))
    
    # Різниця між введеним числом і загаданим
    difference = abs(user_guess - random_number)
    
    # Підказки залежно від різниці
    if difference <= 3:
        print("Дуже близько!")
    elif difference <= 10:
        print("Близько!")
    else:
        print("Далеко!")

# Якщо число вгадано
print("Вітаю! Ви вгадали число:", random_number)
