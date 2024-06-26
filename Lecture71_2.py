Menu_List = []
number = 0
total = 0

while True:
    menuname = input("What do you want? \n")
    if menuname.lower() == "exit":
        break
    else:
        price = int(input("Price \n"))
        Menu_List.append([menuname,price])
        total += price


def showbill():
    print("===จ่ายกูมาสะดีๆ===")
    List = 0
    Quene = 0
    for i in Menu_name:
        print(f"{List+1}. {Menu_List[List][List]} ราคา {Menu_List[List][List+1]} บาท.")
        List += 1
        Quene += 1

    print(f"ราคารวม {total} บาท")
    print("================")

showbill()
print(Menu_List)



