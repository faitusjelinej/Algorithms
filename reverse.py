def reverseWords(s):
    res = ""
    i = 0
    n = len(s)

    while i < n:
        while i < n and s[i] == " ":
            i += 1
        if i >= n:
            break
        j = i + 1
        while j < n and s[j] != " ":
            j += 1
        word = s[i:j]

        if len(res)== 0:
            res = word
        else:
            res = word + " " + res
        i = j + 1
    return res

s = ' hello world '

print(reverseWords(s))

