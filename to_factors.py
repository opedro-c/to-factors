def to_factor(num: int, show_process: bool=False) -> list:    
    results = []
    c = 2
    while num > 1:
        while num % c == 0:
            results.append(c)
            if show_process:
                print(f'{int(num)}\t|{c}')
            num = num / c
        c += 1
    if show_process:
        print('1 \t|')
    return results


def to_superscript(num: int) -> str:
    superscript = ('⁰', '¹', '²', '³', '⁴', '⁵', '⁶', '⁷', '⁸', '⁹')
    return ''.join(map(lambda x: superscript[int(x)], str(num)))
    

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
    result = format_to_factor(to_factor(number, show_process=True))
    print('Result: ', result)
