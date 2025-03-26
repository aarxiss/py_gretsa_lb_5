import random

# Генерація випадкового чотиризначного PIN-коду
pin_code = str(random.randint(1000, 9999))

# Кількість спроб
attempts = 5

print("Вгадай чотиризначний PIN-код! У тебе є 5 спроб.")

while attempts > 0:
    # Отримання відповіді від користувача
    guess = input(f"Ти маєш {attempts} спроби. Введи свій PIN-код: ")

    # Перевірка, чи введено правильний чотиризначний код
    if len(guess) != 4 or not guess.isdigit():
        print("Будь ласка, введи чотиризначний код.")
        continue

    # Підрахунок правильних цифр на правильних позиціях
    correct_digits = sum(1 for i in range(4) if guess[i] == pin_code[i])

    if guess == pin_code:
        print("Вітаємо! Ти вгадав PIN-код!")
        break
    else:
        attempts -= 1
        print(f"Невірно. Ти вгадав {correct_digits} цифри(й) на правильних позиціях.")

        if attempts == 0:
            print(f"Ти вичерпав спроби. Правильний PIN-код був {pin_code}.")
