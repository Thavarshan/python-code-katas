class Add(int):
    def __call__(self, number):
        return Add(self + number)
