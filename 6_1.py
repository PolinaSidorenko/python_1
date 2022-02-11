"""Создать класс TrafficLight (светофор). определить у него один атрибут color (цвет)
и метод running (запуск); атрибут реализовать как приватный; в рамках метода реализовать переключение
светофора в режимы: красный, жёлтый, зелёный; продолжительность первого состояния (красный) составляет
7 секунд, второго (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;"""

import time
class TrafficLight:
    __color = ['Красный', 'Желтый', 'Зеленый']
    def running(self):
        count = 0
        while True:
            if count <3:
                print(TrafficLight.__color[0])
                time.sleep(7)
                print(TrafficLight.__color[1])
                time.sleep(2)
                print(TrafficLight.__color[2])
                time.sleep(8)
                count+=1
            else:
                break

a = TrafficLight()
a.running()