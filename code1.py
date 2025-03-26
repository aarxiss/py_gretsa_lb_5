import random

# Генерація випадкового числа від 1 до 10
random_number = random.randint(1, 10)

print("Я загадав число від 1 до 10. Спробуйте вгадати!")

# Змінна для зберігання числа, яке вводить користувач
user_guess = None

# Цикл триває, поки користувач не вгадає число
while user_guess != random_number:
    # Вводимо число від користувача
    user_guess = int(input("Введіть ваше число: "))
    
    # Перевірка на правильність
    if user_guess < random_number:
        print("Більше!")
    elif user_guess > random_number:
        print("Менше!")
    
# Якщо число вгадано
print("Вітаю! Ви вгадали число:", random_number)
2
