#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Выполнить индивидуальное задание 1 лабораторной работы 4.1, максимально задействовав
# имеющиеся в Python средства перегрузки операторов.


class TaskOne:
   def __init__(self, first, second):
      self.first = first
      self.second = second
      self.summ = self.first * self.second

   def __add__(self, other):
      return self.summ + other.summ
      

if __name__ == '__main__':
   r1 = TaskOne(100, 2)
   r2 = TaskOne(200, 1)
   print(f'r1 + r2 = {r1 + r2}')
