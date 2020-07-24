class FizzBuzz:

    def convert(self, number: int):
        result = ''

        if number % 3 == 0:
            result += 'Fizz'

        if number % 5 == 0:
            result += 'Buzz'

        if result != '':
            return result
        else:
            return number
