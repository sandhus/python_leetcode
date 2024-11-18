"""
You have a bomb to defuse, and your time is running out! Your informer will provide you with a circular array code
of length of n and a key k.

To decrypt the code, you must replace every number. All the numbers are replaced simultaneously.

    If k > 0, replace the ith number with the sum of the next k numbers.
    If k < 0, replace the ith number with the sum of the previous k numbers.
    If k == 0, replace the ith number with 0.

As code is circular, the next element of code[n-1] is code[0], and the previous element of code[0] is code[n-1].
Given the circular array code and an integer key k, return the decrypted code to defuse the bomb!

Example 1:

Input: code = [5,7,1,4], k = 3
Output: [12,10,16,13]
Explanation: Each number is replaced by the sum of the next 3 numbers. The decrypted code is
[7+1+4, 1+4+5, 4+5+7, 5+7+1]. Notice that the numbers wrap around.

"""


def diffuse(k, key):

    operation = find_operation(k)
    code = [0] * len(key)
    if operation and operation == 1:
        pass
    elif operation and operation == 2:
        extended_key = key * 2
        for i, el in enumerate(key):
            ans = sum(extended_key[i+1:i+k+1])
            #print(extended_key[i+1:i+k+1])
            code[i] = ans
    elif operation and operation == 3:
        extended_key = []
        for o in reversed(key):
            extended_key.append(o)
        extended_key = extended_key * 2
        for i, el in enumerate(extended_key[:len(key)]):
            ans = sum(extended_key[i+1:i+abs(k)+1])
            #print(extended_key[i+1:i+k+1])
            code[i] = ans
        code.reverse()
    return code


def find_operation(k):
    if k == 0:
        operation = 1
    elif k > 0:
        operation = 2
    elif k < 0:
        operation = 3
    else:
        print("Invalid K value")
        return False

    return operation

print(diffuse(k=-2, key = [2,4,9,3]))