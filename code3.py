import random

# Генерація випадкового коду від 1 до 20
secret_code = random.randint(1, 20)

# Кількість спроб
attempts = 3

# Гра
print("Вгадай код! Код у діапазоні від 1 до 20. У тебе є три спроби.")

while attempts > 0:
    # Отримання відповіді від користувача
    guess = int(input(f"Ти маєш {attempts} спроби. Введи свій варіант: "))
    
    if guess == secret_code:
        print("Вітаємо! Ти вгадав код!")
        break
    else:
        attempts -= 1
        if attempts > 0:
            print("Невірно. Спробуй ще.")
        else:
            print(f"На жаль, ти не вгадав. Правильний код був {secret_code}.")
