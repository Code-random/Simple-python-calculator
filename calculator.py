def start():
    print("Add-1")
    print("Minus-2")
    print("Times-3")
    print("Devide-4")

    menu = int(input("\nChose option\n"))
    l1 = int(input("Pierwsza liczba:\n"))
    l2 = int(input("Druga liczba:\n"))
    wyjątki(menu, l1, l2)
def wyjątki(menu, l1, l2):
    if l2 == 0:
        if menu == 4:
            print("\nCant devide by 0")
            
def liczenie(menu, l1, l2):
    if menu == 1:
        print("\n Answer:", l1 + l2)
    if menu == 2:
        print("\n Answer:", l1 - l2)
    if menu == 3:
        print("\n Answer:", l1 * l2)
    if menu == 4:
        if l2 != 0:
            print("\n Answer:", l1 / l2)
def exit_start():
    t == input()
    if [t] == int(input("\n Exit? t/n\n")):
        print("\nTurning off...")
    else:
        start() 
start()
#exit_start()
#print(exit)
