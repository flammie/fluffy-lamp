s = "mississippi"
p = "mis*is*p*."
matcher = None
star = False
pi = 0
si = 0
while pi < len(p) and si < len(s):
    if p[pi] == ".":
        matcher = "ANY"
    else:
        matcher = p[pi]
    pi = pi + 1
    if pi < len(p) and p[pi] == "*":
        star = True
        pi = pi + 1
    if star:
        if matcher == "ANY":
            while si < len(s):
                si = si + 1
        else:
            while si < len(s) and s[si] == matcher:
                si = si + 1
    else:
        if matcher == "ANY":
            if si < len(s):
                si = si + 1
        else:
            if si < len(s) and s[si] == matcher:
                si = si + 1
            elif si < len(s) and s[si] != matcher:
                print(f"Mismatched {matcher} at {si}: {s[si:]}")
if si == len(s) and pi == len(p):
    print("matched all")
else:
    print(f"tail left: {s[si:]} or {p[pi:]}")
