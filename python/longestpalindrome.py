
s = "cbbd"

longest = ""
for i in range(len(s)):
    for j in range(len(s), i, -1):
        print(i, j)
        print(s[i:j], s[j-1::-1])
        print(s[i:j], s[j-1:i-1:-1])
        if j - i < len(longest):
            print("bound")
            continue
        elif i == 0 and s[i:j] == s[j-1::-1]:
            longest = s[i:j]
            print("found", longest)
        elif s[i:j] == s[j-1:i-1:-1]:
            longest = s[i:j]
            print("found", longest)
print(longest)
