# 2- Напишите программу для проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# Нужно написать таблицу истинности.

print('Задача: напишите таблицу истинности для всех значений предикат')
print('для утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z.')
print('\nРешение: ')

for x in [0,1]:
    for y in [0,1]:
        for z in [0,1]:
            print('¬ (', x,'⋁', y,'⋁', z,') = ', not x and not y and not z)

#for x in [True,False]:
#    for y in [True,False]:
#        for z in [True,False]:
#            print(x,'or', y,'or', z,' = ', not x and not y and not z)