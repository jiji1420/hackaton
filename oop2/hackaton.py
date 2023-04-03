import json

from decimal import Decimal

file_path = 'cars.json'

class GetMixin:
    def get_data(self):
        with open(file_path) as file:
            return json.load(file)
        
    def get_id(self):
        with open('id.txt') as file:
            id = int(file.read())
            id += 1

        with open('id.txt', 'w') as file:
            file.write(str(id))
        return id 
        
class CreateMixin(GetMixin):
    def create(self):
        data = super().get_data()
        try:
            new_product = {
            'id': super().get_id(),
            'brand':input('Введите марку машины: '),
            'model':input('Введите модель машин: '),
            'year' :int(input('Введите год машины: ')),
            'engine':round(float(input('Введите обьем двигателя:')),1),
            'color':input('Введите цвет машины: '),
            'kuzov':input('Введите кузов машин: '),
            'probeg':int(input('Введите пробег машины: ')),
            'price':round(float(input('Введите стоимость товара:')),2)        
            }

        except ValueError:
            print('Ввели некорректные данные')
            self.create()
        else:
            data.append(new_product)

        with open(file_path, 'w') as file:
            json.dump(data, file)
            print('Successfully created')

class ListingMixin(GetMixin):
    def listing(self):
        print('Список машин')
        data = super().get_data()
        print(data)
        print('End')

class RetrieveMixin(GetMixin):


    def retrieve(self):
        data = super().get_data()

        try:
            id = int(input('Введите id машины: '))
        except ValueError:
            print('Ввели некорректные данные')
            self.retrieve()
        else:
            one_product = list(filter(lambda x: x['id'] == id, data))

        if not one_product:
            print('Такой машины нет')
        else:
            print(one_product[0])

class UpdateMixin(GetMixin):
    def update(self):
        data = super().get_data()
        
        try:
            id = int(input('Введите  id машины: '))
        except ValueError:
            print('Ввели некорректные данные')
            self.update()
        else:
            one_product = list(filter(lambda x: x['id'] == id, data))

            if not one_product:
                print('Такой машины нет')

            product = data.index(one_product[0])

            choice = int(input('Что вы хотите изменить? 1 - brand, 2 - model, 3 - year,4 - engine, 5 - color, 6 - kuzov, 7 - probeg, 8 - price '))
            if choice == 1:
                data[product]['brand'] = input('Введите новую марку: ')
            
            elif choice == 2:
                try:
                    data[product]['model'] = input('Введите новую модель: ')
                except ValueError:
                    print('=========')
            
            elif choice == 3:
                data[product]['year'] = int(input('Введите год машины: '))
            
            elif choice == 4:
                try:
                    data[product]['engine'] = round(float(input('Введите обьем двигателя: ')),1)
                except ValueError:
                    print('=========')
            
            elif choice == 5:
                data[product]['color'] = input('Введите новый цвет: ')
            
            elif choice == 6:
                try:
                    data[product]['kuzov'] = (input('Введите кузов машины: '))
                except ValueError:
                    print('=========')

            elif choice == 7:
                data[product]['probeg'] = int(input('Введите пробег машины: '))

            elif choice == 8:
                try:
                    data[product]['price'] = round(float(input('Введите новую стоимость: ')),2)
                except ValueError:
                    print('===========')
                else:
                    print('Такого поля нет')
                self.update()

                with open(file_path, 'w') as file:
                    json.dump(data, file)

class DeleteMixin(GetMixin):
    def delete(self):
        data = super().get_data()
        try:
            id = int(input('Введите id машины: '))
        except ValueError:
            print('Ввели некорректные данные')
            self.delete()
        else:
            one_product = list(filter(lambda x: x['id']==id,data))
            if not one_product:
                print('Такой машины нет')
            product = data.index(one_product[0])
            data.pop(product)
        
        with open(file_path, 'w') as file:
            json.dump(data,file)
            print('Удалили')


class Cars(CreateMixin,ListingMixin,RetrieveMixin,UpdateMixin,DeleteMixin):
    def __init__(self, brand=' ', model=' ', year=0, engine=0, color=' ', kuzov=' ', probeg=0, price=0):
        self.brand = brand
        self.model = model
        self.year = year
        self.engine = engine
        self.color = color
        self.kuzov = kuzov
        self.probeg = probeg
        self.price = price

car = Cars()
car.create()
# car.listing()
# car.retrieve()
# car.update()
# car.delete()