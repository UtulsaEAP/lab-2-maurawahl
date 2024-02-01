def right_arrow():

    print("What is the first character?")
    base_char = input()

    print("What is the second character?")
    head_char = input()

    row1 = '      ' + head_char
    row2 = base_char + base_char + base_char + base_char + base_char + base_char + head_char + head_char
    row3 = base_char + base_char + base_char + base_char + base_char + base_char + head_char + head_char + head_char
    row4 = base_char + base_char + base_char + base_char + base_char + base_char + head_char

    print(row1)
    print(row2)
    print(row3)
    print(row2)
    print(row4)

if __name__ == "__main__":
    right_arrow()