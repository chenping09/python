def proc(n):
    if n== 0 :
        return
    print(n)
    proc(n-1)
    print(n)

proc(5)