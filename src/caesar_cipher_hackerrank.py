"""
https://www.hackerrank.com/challenges/caesar-cipher-1/problem
"""

def caesarCipher(s, k):
    # Write your code here
    st_lst = s.split("-")
    cnvrtd_lst = []
    for i in st_lst:
        moved_alp = ""
        for j in i:
            ascii = ord(str(j))
            ind = ascii + k
            if j.isupper() and ind > 90:
                ind = 65 + (ind - 90) - 1
            if j.islower() and ind > 122:
                ind = 97 + (ind - 122) - 1
            moved_alp = moved_alp + chr(ind)
            # print(moved_alp)
        cnvrtd_lst.append(moved_alp)

    st = cnvrtd_lst[0]
    cnvrtd_lst.pop(0)
    if len(cnvrtd_lst) > 0:
        for i in cnvrtd_lst:
            st += "-" + i

    return st


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
