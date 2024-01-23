class Car:
    def __init__(self, car_brand, car_model, car_price, car_color, car_year):
        self.car_brand = car_brand
        self.car_model = car_model
        self.car_price = int(car_price)
        self.car_color = car_color
        self.car_year = int(car_year)
    def display_info(self):
        print('Car name: ', self.car_brand)
        print('Model: ', self.car_model)
        print('Price:', self.car_price)
        print('Color: ', self.car_color)
        print('Year: ', self.car_year)
def car_main():
    car_a = Car("Alfa", "Romeo", 27500, 'white', 1999)
    car_b = Car("Peugeot", '307', 100000, 'blue', 2004)
    car_c = Car('Peugeot', '206', 3500, 'white', 2004)
    car_d = Car('Peugeot', '301', 9000, 'purple', 1991)
    car_list = [car_a, car_b, car_c, car_d]
    
    
    def sort_price(e):
        return e.car_price
    sorted_cars = sorted(car_list, key=sort_price)
    
    for car in sorted_cars:
        car.display_info()
        
    
car_main()
                