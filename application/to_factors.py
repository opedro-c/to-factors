from math import prod


def validate_args(func):
    def validate(num):
        if num < 0:
            raise ValueError('Number must be equal or bigger than 0')
        if not isinstance(num, int):
            raise TypeError('Number must be an instance of class <int>')
        return func(num)
    return validate


@validate_args
def to_factors(num: int) -> list:
    results = []
    c = 2
    while num > 1:
        while num % c == 0:
            results.append(c)
            num = num / c
        c += 1
    return results


@validate_args
def to_superscript(num: int) -> str:
    superscript = ('⁰', '¹', '²', '³', '⁴', '⁵', '⁶', '⁷', '⁸', '⁹')
    return ''.join(map(lambda x: superscript[int(x)], str(num)))


def show_process(prime_factors: list) -> None:
        product = prod(prime_factors)
        for num in prime_factors:
            print(f'{int(product)}\t| {num}')
            product = product / num
        print('1\t|')


def format_to_factor(result: list) -> str:
    formatted = ''
    last_num = 0
    for num in result:
        if last_num == num:
            continue
        quantity = result.count(num)
        formatted += f'{num}{to_superscript(quantity)}'
        last_num = num
    return formatted


if __name__ == '__main__':

    def ask_number() -> int:
        while True:
            try:
                num = int(input('Type a natural number bigger than 1: '))
                if num <= 1:
                    raise ValueError
            except ValueError:
                print('Unvalid value!')
            else:
                break
        return num


    number = ask_number()
    number_in_prime_factors = to_factors(number)
    result = format_to_factor(number_in_prime_factors)
    show_process(number_in_prime_factors)
    print('Result: ', result)
