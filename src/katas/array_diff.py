class ArrayDiff:

    def differentiate(self, arrayOne: list, arrayTwo: list) -> list:
        return [item for item in arrayOne if item not in set(arrayTwo)]
