def print_line2(char,times):
    print(char * times)

def print_lines(char,times):
    row = 0
    while row < 5:
        print_line2(char,times)
        row += 1

print_lines("+",5)

name ="程序员"
