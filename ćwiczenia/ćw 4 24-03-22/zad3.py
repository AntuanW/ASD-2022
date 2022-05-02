def anagram(str1, str2):
    def num(ch): return ord(ch) - 97

    if len(str1) != len(str2):
        return False

    B = [0]*26
    for x in str1:
        B[num(x)] += 1
    for x in str2:
        B[num(x)] -= 1
        if B[num(x)] < 0:
            return False
    return True
