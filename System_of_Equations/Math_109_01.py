def Large():
    r1 = input("Enter the first equation's coeficents separtaed by commas: \n")
    r2 = input("Enter the second equation's coeficents separtaed by commas: \n")
    r3 = input("Enter the third equation's coeficents separtaed by commas: \n")
    con = input("Enter in the constants of the equations separted by commas: \n")
    r1 = r1.split(",")
    r2 = r2.split(",")
    r3 = r3.split(",")
    con = con.split(",")

    # X1,Y1,Z1  X
    # X2,Y2,Z2  Y
    # X3,Y3,Z3  Z

    # D = X1*((Y2*Z3)-(Y3*Z2))-X2*((Y1*Z3)-(Y3*Z1))+X3*((Y1*Z2)-(Y2*Z1))
    # DX = X*((Y2*Z3)-(Y3*Z2))-Y*((Y1*Z3)-(Y3*Z1))+Z*((Y1*Z2)-(Y2*Z1))
    # DY = -X*((X2*Z3)-(X3*Z2)) +Y*((X1*Z3)-(X3*Z1)) -Z*((X1*Z2)-(X2*Z1))
    # DZ = X*((X2*Y3)-(X3*Y2)) -Y*((X1*Y3)-(X3*Y1)) +Z*((X1*Y2)-(X2*Y1))

    X1=int(r1[0])
    Y1=int(r1[1])
    Z1=int(r1[2])
    X2=int(r2[0])
    Y2=int(r2[1])
    Z2=int(r2[2])
    X3=int(r3[0])
    Y3=int(r3[1])
    Z3=int(r3[2])

    X=int(con[0])
    Y=int(con[1])
    Z=int(con[2])

    D = X1*((Y2*Z3)-(Y3*Z2))-X2*((Y1*Z3)-(Y3*Z1))+X3*((Y1*Z2)-(Y2*Z1))
    DX = X*((Y2*Z3)-(Y3*Z2))-Y*((Y1*Z3)-(Y3*Z1))+Z*((Y1*Z2)-(Y2*Z1))
    DY = -X*((X2*Z3)-(X3*Z2))+Y*((X1*Z3)-(X3*Z1))-Z*((X1*Z2)-(X2*Z1))
    DZ = X*((X2*Y3)-(X3*Y2))-Y*((X1*Y3)-(X3*Y1))+Z*((X1*Y2)-(X2*Y1))

    # check to see if there is an infinant solution 
    if DX == 0 or DY == 0 or DZ == 0:
        print("This equation has infinant solutions")
        return
    try:
        X = DX/D
        Y = DY/D
        Z = DZ/D
        print(f"({X}, {Y}, {Z})")
    except ZeroDivisionError:
        print("This equation has no solution.")

def Small():
    r1 = input("Enter the first equation's coeficents separtaed by commas: \n")
    r2 = input("Enter the second equation's coeficents separtaed by commas: \n")
    con = input("Enter in the constants of the equations separted by commas: \n")

    r1 = r1.split(",")
    r2 = r2.split(",")
    con = con.split(",")

    

    # XA,YA   XC
    # XB,YB   YC
    # D = (XA*YB)-(XB*YA)
    # DX = (XC*YB)-(YC*YA)
    # DY = (XA*YC)-(XB*XC)

Large()


