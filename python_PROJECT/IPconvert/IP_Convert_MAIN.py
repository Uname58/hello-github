print("IPv4 transfer")
while True:
    #set up
    print("="*30, "\n")
    IPv4 = []
    i = 1
    #Input
    while i < 5:
        print("-"*30)
        choice = input("Binary /Decimal Octet(D/B): ")
        #dec form
        if choice.upper() == "D":
            dec = input(f"{i}. octet= ")
            if dec.isdigit() and 0 <= int(dec) <= 255:
                print(f"your input is deciaml: [ {dec} ]")
                IPv4.append(str(dec))
                i += 1
            else:
                print("Invalid Input!\n")
        #Bin form
        elif choice.upper() == "B":
            bin = int(input(f"{i}. octet= "), 2)
            if 0 <= bin <= 255:
                print(f"your input is deciaml: [ {bin} ]")
                IPv4.append(str(bin))
                i += 1
            else:
                print("Invalid Input!\n")
        #debug part
        else:
            print("!Error Input!\nplease re-enter !")
    #show result
    print("the complete IPv4 is:")
    print(".".join(IPv4))



