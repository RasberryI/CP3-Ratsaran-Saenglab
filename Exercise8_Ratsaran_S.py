username = input("username:")
password = input("password:")
if username == "admin" and password == "1234" :
    print("Done!")
    print("--------rasberry's shop---------")
    print("1.Iphone X | Price : 15,000 THB ")
    print("2.Iphone 11 | Price : 20,000 THB ")
    print("3.Iphone 12 | Price : 22,000 THB ")
    print("4.Iphone 13 | Price : 25,000 THB ")
    X = 15000
    XI = 20000
    XII = 22000
    XIII = 25000
    Goods = input("What iphone do you want(pls type number):")
    if Goods == "1":
        pieces = int(input("How many pieces do you want to buy? :"))
        print("You must pay for :", X * pieces, "THB")
        print("Thank you")
    elif Goods == "2":
        pieces = int(input("How many pieces do you want to buy? :"))
        print("You must pay for :", XI * pieces, "THB")
        print("Thank you")
    elif Goods == "3":
        pieces = int(input("How many pieces do you want to buy? :"))
        print("You must pay for :", XII * pieces, "THB")
        print("Thank you")
    elif Goods == "4":
        pieces = int(input("How many pieces do you want to buy? :"))
        print("You must pay for :", XIII * pieces, "THB")
        print("Thank you")