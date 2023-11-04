def merge(left_half, right_half): 
    # Процедура слияния, которая объединяет два упорядоченных массива в один
    l_left_half, l_right_half = len(left_half), len(right_half)
    arr = [None for i in range(l_left_half + l_right_half)] 
    #Создаём список для слияния
    i = j = k = 0

    while i < len(left_half) and j < len(right_half):
         # Объединение левой и правой половин в один отсортированный массив.
        if left_half[i] < right_half[j]:  
            # Сравнение элементов левой и правой половин.
            arr[k] = left_half[i]  
            # Если элемент из левой меньше, помещаем его в исходный массив.
            i += 1
        else:
            arr[k] = right_half[j]  
            # Если элемент из правой меньше, помещаем его в исходный массив.
            j += 1
        k += 1


    while i < len(left_half): 
        # Добавление оставшихся элементов из левой и правой половин (если такие есть).
        arr[k] = left_half[i]
        i += 1
        k += 1

    while j < len(right_half):
        arr[k] = right_half[j]
        j += 1
        k += 1
    return arr


def merge_sort(arr): 
    # Создаём процедуру сортировки слиянием
    l_arr = len(arr)
    if l_arr == 1 or l_arr == 0: 
        # исключение, если массив нулевой или имеет один элемент
        return arr
    left_half, right_half = arr[0 : l_arr // 2], arr[l_arr // 2 : l_arr] 
    # разделение массива на две половины
    left_half, right_half = merge_sort(left_half), merge_sort(right_half) 
    # вызываем рекурсию сортировки для левой и правой частей массива
    mg = merge(left_half, right_half)
     # объединяем  половины
    for i in range(l_arr):
        arr[i] = mg[i]
    return arr

# Несортированный массив.
my_array = [12,22,5,0,18,-8,-2] 
#Сортировка слиянием
merge_sort(my_array) 
# Вывод 
print("Отсортированный массив (Merge Sort):", my_array) 
