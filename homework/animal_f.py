#!usr/bin/env python3.9
# -*- coding:utf-8 -*-

class Animal:
    name = "Animal"

    def __init__(self,name,color,age,gender):
        self.name = name
        self.color = color
        self.age = age
        self.gender = gender
        Animal.name = name


    @classmethod
    def spark(cls):
        print(f"{cls.name} 会叫")

    @classmethod
    def run(cls):
        print(f"{cls.name} 会跑")



if __name__ == "__main__":
    dog = Animal("Tom","grey",4,"male")
    print(f"{dog.name} 的颜色：{dog.color}，年龄：{dog.age}岁，性别：{dog.gender}")
    dog.spark()
    dog.run()