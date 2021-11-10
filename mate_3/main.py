#task_1
my_tuplex = (4, 6, 2, 8, 3, 1)
a = int(input('введите целое число:'))
l = list(my_tuplex)
l.append(a)
tuple(l)
print(l)
#task_2
tuplex = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
print([t[:-1] + (100,) for t in tuplex])
#task_3
list = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d',)]
list = [t for t in list if t]
print(list)
#task_4
my_list = [1, 2, 3]
sg = ''.join(str(item) for item in my_list)
print(sg)
#task_5
n = int(input('введите число:'))
a = 0
if n > 0:
    while n > 0:
        num = n % 10
        n = n // 10
        a = a * 10 + num
else:
    n = -n
    while n > 0:
        num = n % 10
        n = n // 10
        a = a * 10 + num
    a = -a
print(a)

