# Lila Shearer, FizzBuzz Python

number=0


while number < 50:
    if number >50:
        break
    else:
        number+=1
        if number%5 == 0 and number%3 == 0:
            print("FizzBuzz")
        elif number%3 == 0:
            print("Fizz")
        elif number%5 == 0:
            print("Buzz")
        else:
            print(number)
 
        
