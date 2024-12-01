class Car:
    className = 'Автомобиль'
    objectsCount = 0

    def __init__(self, tank_capacity, fuel_consumption, average_speed):
        self._tank_capacity = tank_capacity # емкость бака в литрах
        self._fuel_consumption = fuel_consumption # расход топлива на 100 км
        self._average_speed = average_speed # средняя скорость в километрах
        Car.objectsCount += 1

    def get_distance(self):
        distance = (self._tank_capacity/self._fuel_consumption) * 100
        print (f'Пройденное расстояние до полного опустошения бака: {distance:.2f} км')


class Truck(Car):
    className = 'Грузовик'

    def __init__(self, tank_capacity, fuel_consumption, average_speed, weight_of_cargo):
        super().__init__(tank_capacity, fuel_consumption, average_speed)
        self._weight_of_cargo = weight_of_cargo # вес груза в кг

    # метод 2: Соотношение веса груза к количеству топлива на 250 км  
    def weight2fuel250(self):
        fuel_needed250 = ((self._fuel_consumption/100) * 250)
        return f'Соотношение веса груза к количеству топлива на 250 км: {self._weight_of_cargo/fuel_needed250}'
    
    # доп перегрузка оператора сложения, получаем новый объект и проверяем условия сложения
    def __add__(self, other):
        if isinstance(other, Truck):
            return Truck(self._tank_capacity + other._tank_capacity,
                        self._fuel_consumption + other._fuel_consumption,
                        self._average_speed + other._average_speed,
                        self._weight_of_cargo + other._weight_of_cargo)
        raise TypeError('Сложение возможно только между объектами типа Truck')

class Bus(Car):
    className = 'Автобус'

    def __init__(self, tank_capacity, fuel_consumption, average_speed, passengers_count):
        super().__init__(tank_capacity, fuel_consumption, average_speed)
        self._passengers_count = passengers_count

    # метод 3: Соотношение числа пассажиров к количеству топлива на 250 км  
    def passengers2fuel250(self):
        fuel_needed250 = (self._fuel_consumption * 250) / 100
        if self._passengers_count > 0:
            print(f'Соотношение числа пассажиров к количеству топлива на 250 км: {self._passengers_count / fuel_needed250}')
        else:
            print('Число пассажиров должно быть больше нуля!')


car = Car(100, 25, 60)
car.get_distance()

tr = Truck(100, 25, 60, 10000)
print(tr.weight2fuel250())


bus = Bus(100, 25, 60, 60)
bus.passengers2fuel250()


tr2 = Truck(200, 50, 50, 20000)
result_truck = tr + tr2
# атрибуты нового объекта н
print("Новый грузовик после сложения:")
print(f"\tЕмкость бака: {result_truck._tank_capacity} л")
print(f"\tРасход топлива: {result_truck._fuel_consumption} л/100 км")
print(f"\tСредняя скорость: {result_truck._average_speed} км/ч")
print(f"\tВес груза: {result_truck._weight_of_cargo} кг")