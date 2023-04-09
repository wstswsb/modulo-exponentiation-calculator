class ModuloExponentiationCalculator:
    def __init__(self):
        self.start = True

    def calculate(self, number: int, power: int, mod: int, additional_item=1):
        if self.start:
            print(f'({number})^{power} mod {mod} = ')
            self.start = False
        if power == 1:
            result = number
            if additional_item != 1:
                print(f'{number} * {additional_item} mod {mod} = ', end="")
                print(f'{number * additional_item} mod {mod} = ', end="")
                result = number * additional_item % mod
                print(result)
            return result
        if power % 2 == 0:
            half_power = int(power / 2)
            print(f'({number}^2)^{half_power} * {additional_item} mod {mod} = ')
            print(f'({number ** 2})^{half_power} * {additional_item} mod {mod} =')
            print(f'({number ** 2 % mod})^{half_power} * {additional_item} mod {mod}')
            number = number ** 2 % mod
            power /= 2
            print()
            return self.calculate(number, power, mod, additional_item)
        elif power % 2 == 1:
            half_power = int(power / 2)
            print(f'({number}^2)^{half_power} * {number} * {additional_item} mod {mod} = ')
            additional_item = number * additional_item
            print(f'({number}^2)^{half_power} * {additional_item} mod {mod} = ')
            additional_item = additional_item % mod
            print(f'({number ** 2})^{half_power} * {additional_item} mod {mod} =')
            print(f'({number ** 2 % mod})^{half_power} * {additional_item} mod {mod} =')
            number = number ** 2 % mod
            power = half_power
            print()
            return self.calculate(number, power, mod, additional_item)


calculator = ModuloExponentiationCalculator()
result = calculator.calculate(number=237, power=4445352423323, mod=523)
