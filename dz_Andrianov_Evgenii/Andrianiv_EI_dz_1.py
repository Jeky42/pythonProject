#1. Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
# до минуты: <s> сек;
# до часа: <m> мин <s> сек;
# до суток: <h> час <m> мин <s> сек;
# * в остальных случаях: <d> дн <h> час <m> мин <s> сек.

duration = int(input())
days =  duration // (24 * 3600)
hours = (duration - days * 24 * 3600) // 3600
minutes = (duration - (days * 24 * 3600 + hours * 3600)) // 60
seconds = duration - (days * 24 * 3600 + hours * 3600 + minutes * 60)
print('в', duration, ':', days, 'дней' ,hours, 'часов', minutes, 'минут', seconds, 'секунд')

#2. Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень числа X):

#3.Склонение слова

i = input("Введите процент:")
numbs = {11,12,13,14}
for i in range(100):
    i = i + 1
    if i in numbs:
        print(i, "процентов")
    elif i % 10 == 1:
        print(i, "процент")
    elif i % 10 > 1 and i % 10 <5:
        print(i, "процента")
    else:
        print(i, "процентов")