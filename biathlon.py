import random

lap = 0

extra_time = 0

while lap < 4:

    misses = random.randint(0, 5)

    if misses == 0:
        extra_time += 0
    elif misses == 1:
        extra_time += 1
    elif misses == 2:
        extra_time += 2
    elif misses == 3:
        extra_time += 3
    elif misses == 4:
        extra_time += 4
    else:
        extra_time += 5

    lap += 1
    if lap == 1:
        print("Результаты стрельбы на первом круге: ")
    elif lap == 2:
        print("Результаты стрельбы на втором круге: ")
    elif lap == 3:
        print("Результаты стрельбы на третьем круге: ")
    else:
        print("Результаты стрельбы на четвертом круге: ")
    print("Кол-во промахов:", misses, "\nДобавочное время: +", extra_time, "мин")
    print("")
if extra_time == 1:
    miss = "промах"
elif 1 < extra_time < 5:
    miss = "промаха"
else:
    miss = "промахов"

print("Итого:", extra_time, miss)

if extra_time == 0:
    print("Поздравляем!Вы победитель следующей гонки!")
elif 0 < extra_time < 2:
    print("У вас неплохие шансы на победу в следующей гонке!")
else:
    print("С таким кол-во промахов будет сложно рассчитывать на победу в следующей гонке")
