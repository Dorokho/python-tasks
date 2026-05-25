class Dessert:
    
    def __init__(self, name=None, calories=None):
        self.set_name(name)
        self.set_calories(calories)

    #getter для name
    def get_name(self):
        return self._name
    
    #setter для name
    def set_name(self, name):
        if isinstance(name, str):
            self._name = name
        else:
            self._name = ""

    #getter для calories
    def get_calories(self):
        return self._calories
    
    #setter для calories
    def set_calories(self, calories):
        if isinstance(calories, (int, str)):
            self._calories = calories
        else:
            self._calories = 0

    #десерт считается полезным, если калорий меньше 200
    def is_healthy(self):
        try:
            return self._calories < 200
        except:
            return False
        
    #любой десерт вкусный
    def is_delicious(self):
        return True


dessert = Dessert("Cake", 150)

print(dessert.get_name())         
print(dessert.get_calories())     
print(dessert.is_healthy())        
print(dessert.is_delicious())