digits = "23"
rv = []
for digit in digits:
    news = []
    if not rv:
        rv = [""]
    for v in rv:
        if not v:
            v = ""
        if digit == "2":
            news.append(v + "a")
            news.append(v + "b")
            news.append(v + "c")
        elif digit == "3":
            news.append(v + "d")
            news.append(v + "e")
            news.append(v + "f")
        elif digit == "4":
            news.append(v + "g")
            news.append(v + "h")
            news.append(v + "i")
        elif digit == "5":
            news.append(v + "j")
            news.append(v + "k")
            news.append(v + "l")
        elif digit == "6":
            news.append(v + "m")
            news.append(v + "n")
            news.append(v + "o")
        elif digit == "7":
            news.append(v + "p")
            news.append(v + "q")
            news.append(v + "r")
            news.append(v + "s")
        elif digit == "8":
            news.append(v + "t")
            news.append(v + "u")
            news.append(v + "v")
        elif digit == "9":
            news.append(v + "w")
            news.append(v + "x")
            news.append(v + "y")
            news.append(v + "z")
    rv = news
print(rv)
