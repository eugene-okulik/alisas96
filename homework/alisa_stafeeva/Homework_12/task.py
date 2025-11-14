class Flowers:
    def __init__(self, name, color, price, lifetime, stem_length):
        self.name = name
        self.color = color
        self.price = price
        self.lifetime = lifetime
        self.stem_length = stem_length

    def __str__(self):
        return f"{self.name}({self.color}, {self.price}, {self.stem_length}, {self.lifetime})"
    
    def __repr__(self):
        return f"{self.name}({self.color}, {self.price}, {self.stem_length}, {self.lifetime})"


class Rose(Flowers):
    def __init__(self, color, price, stem_length):
        super().__init__('Роза', color, price, 7, stem_length)


class Tulip(Flowers):
    def __init__(self, color, price, stem_length):
        super().__init__('Тюльпан', color, price, 4, stem_length)


class Violet(Flowers):
    def __init__(self, price, stem_length):
        super().__init__('Фиалка', 'фиолетовый', price, 2, stem_length)


class Bouquet:
    def __init__(self, *flowers):
        self.flowers = list(flowers)

    def bouquet_lifetime(self):
        return sum(flower.lifetime for flower in self.flowers) / len(self.flowers)
    
    def bouquet_price(self):
        return sum(flower.price for flower in self.flowers)
        
    def sort_by(self, attribute):
        return sorted(self.flowers, key=lambda flower: getattr(flower, attribute))
    
    def find_by(self, attribute, value):
        return list(flower for flower in self.flowers if getattr(flower, attribute) == value)


red_rose = Rose('красный', 100, 50)
white_rose = Rose('белый', 120, 70)
small_violet = Violet(110, 30)
white_tulip = Tulip('белый', 150, 50)
red_tulip = Tulip('красный', 150, 50)

bouquet1 = Bouquet(red_rose, white_rose, small_violet, white_tulip, red_tulip)
print(bouquet1.find_by('color', 'красный'))
print(bouquet1.sort_by('price'))
