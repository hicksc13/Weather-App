#Forexample


numbers = [312, 1434, 68764, 4627, 84, 470, 9047, 98463, 389, 2]
high = numbers[0]
for number in numbers:
      if number > high:
          high = number
      print(f"The highest number is {high}")