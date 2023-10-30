# Дан список целых чисел numbers. Необходимо написать в декларативном стиле процедуру для сортировки числа в списке в порядке убывания. Можно использовать любой алгоритм сортировки.

def sort_list_declarative(numbers):
    numbers.sort(reverse=True)
    return numbers


print(f"{sort_list_declarative([104, 33, -32, 57, 10, 0, 418, 56])}")