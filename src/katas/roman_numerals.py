class RomanNumerals:

    numerals = {
        'M': 1000,
        'CM': 900,
        'D': 500,
        'CD': 400,
        'C': 100,
        'XC': 90,
        'L': 50,
        'XL': 40,
        'X': 10,
        'IX': 9,
        'V': 5,
        'IV': 4,
        'I': 1,
    }

    def generate(self, number):
        if (number <= 0 or number >= 4000):
            return False

        result = ''

        for numeral, arabic in self.numerals.items():
            while number >= arabic:
                result += numeral

                number -= arabic

        return result
