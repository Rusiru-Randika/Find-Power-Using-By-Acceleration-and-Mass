def main():
    yeslist = ["Y","y"]
    print("           Find Power Using By Acceleration and Mass     ")
    print("            This Phython Project By Rusiru Randika.   ")
    print(" ")
    print("        This program uses the equation F = ma Newton. ")
    print("")
    print("Do You Want to Find Power        :- Press 1")
    print("Do You Want to Find Mass         :- Press 2")
    print("Do You Want to Find Acceleration :- Press 3")
    print("")
    z=input("What do You Want Find ? : ")
    print("")

    if z == "1":
        def power():
            
                              

            m=int(input("Input Mass(kg) : "))
            print(" ")

            a=int(input("Input Acceleration(ms⁻²) : "))
            print("")

            f=m*a

            print("Power Value : ",f,"N")
            print("")
        power()

    if  z== "2":
        
        def mass():
            f=int(input("Input Power(N) : "))
            print(" ")

            a=int(input("Input Acceleration(ms⁻²) : "))
            print("")

            m=f/a

            print("Mass Value : ",m,"kg")
            print("")
        mass()

    if  z== "3":
        
        def mass():
            f=int(input("Input Power(N) : "))
            print(" ")

            m=int(input("Input Acceleration(ms⁻²) : "))
            print("")

            a=f/m

            print("Acceleration Value : ",a,"ms⁻²")
            print("")
        mass()

    else:        
        print("You can try again or exit")
        print("")
            
                


    restart=input("Do You Want to Start Again ?(Y/N) : ")

    print("")
    if restart in yeslist:
        main()
        print("")

    else:
        input("Goodbye...!!!")
        exit()

main()

