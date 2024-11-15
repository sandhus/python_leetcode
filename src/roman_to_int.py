"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

    I can be placed before V (5) and X (10) to make 4 and 9.
    X can be placed before L (50) and C (100) to make 40 and 90.
    C can be placed before D (500) and M (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer.
"""
def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """


    mapping = {
        "I" :1,  "V" :5, "X" :10, "L" :50, "C" :100, "D" :500, "M" :1000
    }

    inp = str(s)
    final =[]
    skip_next = False

    for i in inp:
        print(i)
        if skip_next:
            skip_next = False
            continue
        try:
            if i == "I" and (inp[inp.index(i)+1] == "V"):
                final.append(str(4))
                skip_next = True
                continue
            if i == "I" and (inp[inp.index(i) + 1] == "X"):
                final.append(str(9))
                skip_next = True
                continue
            if i == "X" and (inp[inp.index(i) + 1] == "L"):
                final.append(str(40))
                skip_next = True
                continue
            if i == "X" and (inp[inp.index(i) + 1] == "C"):
                final.append(str(90))
                skip_next = True
                continue
            if i == "C" and (inp[inp.index(i) + 1] == "D"):
                final.append(str(400))
                skip_next = True
                continue
            if i == "C" and (inp[inp.index(i) + 1] == "M"):
                final.append(str(900))
                skip_next = True
                continue
            final.append(str(mapping[i]))
            print(final)
        except KeyError:
            continue

    ans =0
    if final:
        for k in final:
            ans += int(k)

    return print(ans)


romanToInt("III")