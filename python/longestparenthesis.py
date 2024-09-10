def longestValidParentheses(s: str) -> int:
    longest = 0
    for i in range(len(s)):
        if len(s) - i < longest:
            break
        opened = 0
        print(f"{i=}")
        for length, c in enumerate(s[i:]):
            print(f"{c=}, {length=}, {opened=}")
            if c == "(":
                opened = opened + 1
            elif c == ")":
                opened = opened - 1
            if opened < 0:
                break
            elif opened == 0 and length + 1 > longest:
                longest = length + 1
    return longest

print(longestValidParentheses("(()"))
