#1) მომხმარებელს უნდა შემოატანინოთ რიცხვი და შემდეგ უნდა დაბეჭდოთ არის თუ არა ეს რიცხვი ხუთის ჯერადი
num = int(input("enter your number: "))
if num % 5 == 0:
    print("You entered number that can be multiplied 5 without remains")
else:
    print("You entered number that cannot be multiplied by 5 without remains")