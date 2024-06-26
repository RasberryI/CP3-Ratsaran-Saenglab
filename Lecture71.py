Menu_name = []
Price = []
menuname = ""
number = 0
total = 0

while menuname.lower() != "exit":
    menuname = input("What do you want? \n")
    Menu_name.append(menuname)
    if menuname.lower() == "exit":
        del Menu_name[-1]
        break
    else:
        price = int(input("Price \n"))
        Price.append(price)
        total += price


def showbill():
    print("===จ่ายกูมาสะดีๆ===")
    List = 0
    Quene = 0
    for i in Menu_name:
        print(f"{List+1}. {Menu_name[List]} ราคา {Price[List]} บาท.")
        List += 1
        Quene += 1

    print(f"ราคารวม {total} บาท")
    print("================")

showbill()



