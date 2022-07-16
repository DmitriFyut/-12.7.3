import random

num = random.randint(1, 100)
print("Угадайте число от 1 до 100 :)")
count = 0
while True:
    guess = int(input(f"{count + 1} попытка: "))
    if guess == num:
        print(f"Верно! C {count + 1} попытки!")
        if (count + 1) <= 3:
            print("Великолепный результат!!! Хорошая интуиция! :)")
        break
    elif guess > num and guess <= 100:
        print(f"Загаданное число < {guess}")
    elif guess < num and guess <= 100:
        print(f"Загаданное число > {guess}")
    else:
        print("УПС! Возможно Вы ввели не то...")
    count += 1