def convert_base(num, to_base=10, from_base=10):
    # first convert to decimal number
    if isinstance(num, str):
        n = int(num, from_base)
    else:
        n = int(num)
    # now convert decimal to 'to_base' base
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n < to_base:
        return alphabet[n]
    else:
        return convert_base(n // to_base, to_base) + alphabet[n % to_base]

print(convert_base('AA16342F', from_base=16, to_base=8))
#Out[41]: '25205432057'

print(convert_base('111', from_base=2))
#Out[42]: '7'

print(convert_base(33, to_base=16))
#Out[43]: '21'

print(convert_base(33333, to_base=20))
#Out[44]: '436D'

print(convert_base(3333333, to_base=20))
#Out[45]: '10GD6D'
