
def caffeine():

    print("How much caffeine?")
    caffeine_mg = float(input())
    
    print("After 6 hours: " + f'{caffeine_mg/2:.2f}' + " mg")
    print("After 12 hours: " + f'{caffeine_mg/4:.2f}' + " mg")
    print("After 24 hours: " + f'{caffeine_mg/16:.2f}' + " mg")

if __name__ == "__main__":
    caffeine()