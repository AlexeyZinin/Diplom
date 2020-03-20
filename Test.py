

class PIDRegulator:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def normalize(self):
        result = (self.a + self.b) * self.c
        self.a += 10
        print(result)


pidr = PIDRegulator(1, 2, 4)
for _ in range(6):
    pidr.normalize()