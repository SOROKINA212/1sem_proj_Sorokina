# ???? ????? x, y. ????????? ?????????? ????????????: "????? ? ???????????? (x, y) ????? ?? ?????? ???
# ??????? ???????????? ????????"
x, y = int(input("??????? ?????? ????????: ")), int(input("??????? ?????? ????????: "))  # ???? ??????? ????????
while type(x) != int and type(y) != int:
    try:
        x = int(x)
        y = int(y)
    except ValueError:
        print("???? ?? ???????? ?? ???????? ?????????????, ?????????? ?????. . .")
        x, y = int(input("??????? ?????? ????????: ")), int(input("??????? ?????? ????????: "))
if x < 0 and y != 0:   # ???????? ?? ?????????????? ?? ?????? ??? ??????? ???????????? ????????
    print("????? ????? ?? ?????? ??? ??????? ????????")
else:
    print("????? ?? ????? ?? ?????? ??? ??????? ????????")