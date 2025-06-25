class Decrementor:
    def __init__(self, start):
        self.value = start

    def decrement(self, step=1):
        self.value -= step
        return self.value

    def reset(self, new_start):
        self.value = new_start

# Example usage
if __name__ == "__main__":
    dec = Decrementor(10)
    print(dec.decrement())      # 9
    print(dec.decrement(2))     # 7
    dec.reset(20)
    print(dec.decrement(5))     # 15