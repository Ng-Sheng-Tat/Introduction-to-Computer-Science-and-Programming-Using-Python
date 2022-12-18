count = 0
for i in range(len(s)):
    try:
        if s[i] == 'b' and s[i+1] == 'o' and s[i+2] == 'b':
            count += 1
    except:
        pass
print(count)