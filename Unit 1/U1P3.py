# print(ord('a'))
# print(ord('b'))

s = 'nvkawapzsnehwngwpqo'
# s = 'abcbcd'
maxstr = s[0]
currstr = s[0]

try:
    for i in range(len(s)):
        if s[i+1] >= s[i]:
            currstr += s[i+1]
            if len(maxstr) < len(currstr):
                maxstr = currstr
        else:
            currstr = s[i+1]
except:
    pass

print(maxstr)
# print(f"Max: {maxstr}")
# print(f"Current: {currstr}")