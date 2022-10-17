#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Дополнительно к требуемым в заданиях операциям перегрузить операцию индексирования [].
# Максимально возможный размер списка задать константой. В отдельном поле size должно
# храниться максимальное для данного объекта количество элементов списка; реализовать метод
# size(), возвращающий установленную длину. Если количество элементов списка изменяется во
# время работы, определить в классе поле count. Первоначальные значения size и count
# устанавливаются конструктором.
# Создать класс Money для работы с денежными суммами. Сумма должна быть представлена
# списоком, каждый элемент которого — десятичная цифра. Максимальная длина списка —
# 100 цифр, реальная длина задается конструктором. Младший индекс соответствует
# младшей цифре денежной суммы. Младшие две цифры — копейки.


class Money:
    const_len = 100
    def __init__(self, number):
        self.lst = []
        self.number = str(number)
        for i in self.number:
            self.lst.append(i)
        self.size(self.lst)

    def size(self, lst):
        size = len(lst)
        if size > Money.const_len:
            print("Первышена максимальная длина списка")
            exit(1)

    def __add__(self, other):
        summ_lst = []
        lst1 = self.lst[::-1]
        lst2 = other.lst[::-1]
        lst1 = int("".join(lst1))
        lst2 = int("".join(lst2))
        summ_str = str(lst1 + lst2)
        for i in summ_str:
            summ_lst.append(i)
        self.size(summ_lst)
        return "".join(summ_lst[::-1])

    def __sub__(self, other):
        summ_lst = []
        lst1 = self.lst[::-1]
        lst2 = other.lst[::-1]
        lst1 = int("".join(lst1))
        lst2 = int("".join(lst2))
        summ_str = str(lst1 - lst2)
        for i in summ_str:
            summ_lst.append(i)
        self.size(summ_lst)
        return "".join(summ_lst[::-1])
            

if __name__ == '__main__':
    r1 = Money(11233)
    r2 = Money(12222)
    print(f"r1 + r2 = {r1 + r2}")
    print(f"r1 - r2 = {r1 - r2}")
