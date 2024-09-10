def findSubstring(s, words):
    rv = []
    for word in words:
        i = s.find(word)
        while i != -1:
            j = i + len(word)
            rests = words.copy()
            rests.remove(word)
            found = True
            print(f"{rests=}")
            while rests and found:
                found = False
                rest = None
                for rest in rests:
                    print(f"trying {j}:{j+len(rest)} = {s[j:j+len(rest)]}")
                    if rest == s[j:j+len(rest)]:
                        print("found")
                        found = True
                        j = j + len(rest)
                        break
                if found:
                    rests.remove(rest)
            if not rests:
                rv.append(i)
                i = s.find(word, i + 1)
            else:
                i = s.find(word, i + 1)
    return rv


print(findSubstring("barfoothefoobarman", ["foo", "bar"]))
