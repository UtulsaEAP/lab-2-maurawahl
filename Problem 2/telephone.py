def telephone():

    print("What is your phone number?")
    phone_number = int(input())

    first = phone_number // 10000000
    second = (phone_number % (first*100000)) // 10000
    third = phone_number % ((phone_number // 10000))

    output = ("(" + str(first) + ")" + " " + str(second) + "-" + str(third))
    print(output)

if __name__ == "__main__":
    telephone()