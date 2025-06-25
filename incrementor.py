class Incrementor:
    def __init__(self, start=0, step=1):
        self.value = start
        self.step = step

    def increment(self):
        self.value += self.step
        return self.value

if __name__ == "__main__":
    inc = Incrementor(start=0, step=1)
    for _ in range(5):
        print(inc.increment())