class EvenNumbers:
    def __init__(self, n):
        try:
            if isinstance(n, int) and n >= 0:
                self.n = n
            else:
                self.n = 0
        except:
            self.n = 0

    def __iter__(self):
        self.current = 0
        return self
    
    def __next__(self):
        if self.current >= self.n:
            raise StopIteration
        
        value = self.current * 2
        self.current += 1
        return value
    
evens = EvenNumbers(5)
for num in evens:
    print(num)