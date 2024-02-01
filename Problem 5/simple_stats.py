
def simple_stats():

    print("input the first number")
    num1 = float(input())

    print("input the second number")
    num2 = float(input())

    print("input the third number")
    num3 = float(input())

    print("input the fourth number")
    num4 = float(input())

    product = num1*num2*num3*num4
    average = (num1+num2+num3+num4)/4

    print(f'{product:.0f}' + " " + f'{average:.0f}')
    print(f'{product:.3f}' + " " + f'{average:.3f}')
if __name__ == "__main__":
    simple_stats()