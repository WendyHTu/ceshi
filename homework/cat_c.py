#!usr/bin/env python3.9
# -*- coding:utf-8 -*-

from animal_f import Animal

class Cat(Animal):
    def __init__(self,name,color,age,gender):
        super().__init__(name,color,age,gender)
        self.hair = "short"

    def talent(self):
        print(f'{self.name} 会抓老鼠')

    def spark(self):
        print(f"{self.name} 会喵喵叫")

if __name__== "__main__":
    lili = Cat('lili','white',2,'female')
    print(f"{lili.name} 的颜色：{lili.color}，毛发：{lili.hair}, 年龄：{lili.age}岁，性别：{lili.gender}")
    lili.spark()
    lili.talent()
    lili.run()
