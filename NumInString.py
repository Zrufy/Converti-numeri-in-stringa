def int_to_en(num):
    d = { 0 : 'zero', 1 : 'uno', 2 : 'due', 3 : 'tre', 4 : 'quattro', 5 : 'cinque',
          6 : 'sei', 7 : 'sette', 8 : 'otto', 9 : 'nove', 10 : 'dieci',
          11 : 'undici', 12 : 'dodici', 13 : 'tredici', 14 : 'quattordici',
          15 : 'quindici', 16 : 'sedici', 17 : 'diciassette', 18 : 'diciotto',
          19 : 'diciannove', 20 : 'venti',
          30 : 'trenta', 40 : 'quaranta', 50 : 'cinquanta', 60 : 'sessanta',
          70 : 'settanta', 80 : 'ottanta', 90 : 'novanta' }
    k = 1000
    m = k * 1000
    b = m * 1000
    t = b * 1000

    assert(0 <= num)

    if isinstance(num,int) == False:
        return None

    if (num < 20):
        return d[num]

    if (num < 100):
        if num % 10 == 0: return d[num]
        else: return d[num // 10 * 10] + '-' + d[num % 10]

    if (num < k):
        if num == 100:
            return 'cento'
        if num % 100 == 0: return d[num // 100] + 'cento'
        elif num <= 199:
            return 'cento' + int_to_en(num % 100)
        else: return d[num // 100] + 'cento' + int_to_en(num % 100)

    if (num < m):
        if num == 1000:
            return 'mille'
        elif num <= 1999:
            return 'mille-' + int_to_en(num % k)
        if num % k == 0:
            return int_to_en(num // k) + 'mila'
        else:
            return int_to_en(num // k) + 'mila-' + int_to_en(num % k)

    if (num < b):
        if num == 1000000:
            return 'un milione'
        elif num <= 1999999:
            return 'un milione'+ int_to_en(num % m)
        if (num % m) == 0:
            return int_to_en(num // m) + ' milioni'
        else:
            return int_to_en(num // m) + ' milioni' + int_to_en(num % m)

    if (num < t):
        if num == 1000000000:
            return 'un miliardo'
        elif num <= 1999999999:
            return 'un miliardo' + int_to_en(num % m)
        if (num % b) == 0:
            return int_to_en(num // b) + ' miliardi'
        else: return int_to_en(num // b) + ' miliardi,' + int_to_en(num % b)
    if num == 1000000000000:
        return 'un trillione'
    elif num <= 1999999999999:
        return 'un trillione' + int_to_en(num % m)
    if (num % t == 0):
        return int_to_en(num // t) + ' trillioni'
    else: return int_to_en(num // t) + ' trillioni' + int_to_en(num % t)


for i in range(1,1000000000000):
    print("%s : %s" % (i,int_to_en(i)))