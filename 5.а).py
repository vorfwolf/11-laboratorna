#Виконав: Лавренюк Б.В., 1 курс, 122Г, ФТФ
#5.а) Дан текстовий файл f. Отримати в файлі g кількість букв, що знаходяться в файлі f.
k = open('f.txt').read() #відкриваємо текстовий файл f
print(k) #виводимо його зміст

d = [] #пустий список
for i in k:
    if i.isalpha(): #проходимося по змісту і якщо компонент є буквою додаємо цей компонент до пустого списку d
        d.append(i)

g = open('g.txt', 'w') #відкриваємо текстовий файл g для запису
g.write(str(len(''.join(d)))) #записуємо в нього кількість букв файла f
g.close() #закриваємо текстовий файл g
print(open('g.txt').read()) #виводимо зміст файла g
