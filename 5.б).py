#Виконав: Лавренюк Б.В., 1 курс, 122Г, ФТФ
#5.б) Дано текстові файли f1 і f2. Переписати зі збереженням порядку проходження
#кожен другий компонент файлу f1 в f2, а кожен другий компонент файлу f2 - в файл f1.
#Використовувати допоміжний файл h.
a = open('f1.txt').read() #відкриваємо текстовий файл f1
print(a) #виводимо його зміст
k = open('f1.txt').read().split() #розділяємо зміст файлу f1 на окремі слова

d = [] #пустий список
for i in range(len(k)):
    for j in range(len(k[i])): #проходимося по кожному компоненту окремого слова
        if j % 2 == 1: # і додаємо кожен другий компонент в пустий список d
            d.append(k[i][j])

a = open('f2.txt').read() #відкриваємо текстовий файл f2
print(f'\n{a}') #абзац
k = open('f2.txt').read().split() #розділяємо зміст файлу f2 на окремі слова

z = [] #пустий список
for i in range(len(k)):
    for j in range(len(k[i])): #проходимося по кожному компоненту окремого слова
        if j % 2 == 1: # і додаємо кожен другий компонент в пустий список z
            z.append(k[i][j])

h = open('h.txt', 'w') #відкриваємо текстовий файл h для запису
h.write(''.join(d)) #записуємо спочатку рядком кожен другий компонент файлу f1
h.write('\n')
h.write(''.join(z)) #потім записуємо рядком кожен другий компонент файлу f2
h.close() #закриваємо текстовий файл h

print(open('h.txt').read()) #виводимо зміст файлу h
print('\n')

p = open('h.txt')
f2 = open('f2.txt', 'a') #відкриваємо текстовий файл f2 на дозапис
f2.write(f'\n{p.readline()}') # і дозаписуємо перший рядок файлу h, тобто кожен другий компонент файлу f1
f1 = open('f1.txt', 'a') #відкриваємо текстовий файл f1 на дозапис
f1.write(f'\n{p.readline()}') # і дозаписуємо другий рядок файлу h, тобто кожен другий компонент файлу f2
f2.close() #закриваємо текстовий файл f2
f1.close() #закриваємо текстовий файл f1

print(open('f1.txt').read()) #виводимо заново зміст файлу f1
print('\n') #абзац
print(open('f2.txt').read()) #виводимо заново зміст файлу f2

