
def test_is_valid(test):
    if (isinstance(test, int)==True and 1<=test<=3 ):
        return True
    else:
        return False

value = int(input("Enter a value "))
print(test_is_valid(value))

fruit = 'banana'
print(fruit[0])
print(fruit[0:3])
print(fruit[:3])
print(fruit[3:])

index = 0
while index < len(fruit):
    letter = fruit[index]
    print(letter)
    index = index + 1