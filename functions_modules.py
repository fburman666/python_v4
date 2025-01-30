#2.1
def my_function(text):
    print(f"{text} är en riktig hacker")

#2.2a
def eko(text):
    print(f"{text}{text}")

#2.2b
def eko2b(text, count):
    result = ""
    while count > 0:
       result = result + text
       count -= 1
    print(result)

#2.3
def loop_function():
    end = 5
    y = 1
    for x in range(1, 100):
        y *= 2
        if x == end:
            break
    print(y)

#2.4
def last(list_of_numbers):
    list_of_numbers.reverse()
    result = list_of_numbers[0]
    print(result)

#2.5
def cut_edges(list_of_numbers):
    list_of_numbers.pop(0)
    list_of_numbers.reverse()
    list_of_numbers.pop(0)
    list_of_numbers.reverse()
    print(list_of_numbers)

#2.6
def increase(x):
    x += 1
    return x

#2.7
def average (x, y):
    return (x + y)/2

#2.8
def pretty_print(ugly_list):
    print(f"Listan har {len(ugly_list)} element")
    for element in ugly_list:
        index = ugly_list.index(element) + 1
        print(f"{index}. {element}")
