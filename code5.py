import random

# Список кольорів
colors = ['червоний', 'синій', 'зелений', 'жовтий', 'фіолетовий']

# Випадковий вибір кольору
secret_color = random.choice(colors)

# Кількість спроб
attempts = 3

print("Вгадай колір! Можливі кольори: червоний, синій, зелений, жовтий, фіолетовий.")
print("Після кожної спроби я скажу, чи це теплий чи холодний колір.")

while attempts > 0:
    # Отримання відповіді від користувача
    guess = input(f"Ти маєш {attempts} спроби. Введи колір: ").lower()

    if guess not in colors:
        print("Це не один із можливих кольорів. Спробуй ще раз.")
        continue

    if guess == secret_color:
        print("Вітаємо! Ти вгадав колір!")
        break
    else:
        attempts -= 1

        # Підказка
        if guess in ['червоний', 'жовтий']:
            print("Теплий колір!")
        else:
            print("Холодний колір!")

        if attempts == 0:
            print(f"На жаль, ти не вгадав. Правильний колір був {secret_color}.")
