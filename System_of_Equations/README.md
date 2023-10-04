## System of Equations Self-Directed Learning Project

When I first started working on the system of equations, I always questioned how a computer would be able to find out the answers to this problem. So, for my self-directed learning project I decided to investigate the matter a little further. I wanted to find a way of solving 3x3 system of equation with Python.

When I started my research, I found the determinant method, it uses matrices to solve the system of equations. It took me to understand how it worked and how I would be able to implement it into code. The majority of my information about the determinant method came from this website [here](https://pressbooks.bccampus.ca/algebraintermediate/chapter/solve-systems-of-equations-using-determinants/).

### Code

When I first started developing this program, I made a chart that would help me visualize the matrix and the naming of the variable that I would be using in my program. I would use this to then create the math equation to D, DX, DY and DZ. These values will be used to find the X, Y and Z location of the final intersecting point or determine of the equation is an infinite solution or no solution.

```python
# X1,Y1,Z1  X
# X2,Y2,Z2  Y
# X3,Y3,Z3  Z

# D = X1*((Y2*Z3)-(Y3*Z2))-X2*((Y1*Z3)-(Y3*Z1))+X3*((Y1*Z2)-(Y2*Z1))
# DX = X*((Y2*Z3)-(Y3*Z2))-Y*((Y1*Z3)-(Y3*Z1))+Z*((Y1*Z2)-(Y2*Z1))
# DY = -X*((X2*Z3)-(X3*Z2))+Y*((X1*Z3)-(X3*Z1))-Z*((X1*Z2)-(X2*Z1))
# DZ = X*((X2*Y3)-(X3*Y2))-Y*((X1*Y3)-(X3*Y1))+Z*((X1*Y2)-(X2*Y1))

```

I first had to ask the user to enter in the coefficients and constants of each of the equations.As an example if I have the equation 3x - 5y + 4z = 5, my coefficients would be 3, -5, 4 and my constant would be 5. The coefficients would be separated by commas to make it easier for to separate the values.

```python
r1 = input("Enter the first equation's coefficients separtaed by commas: \n")
r2 = input("Enter the second equation's coefficients separtaed by commas: \n")
r3 = input("Enter the third equation's coefficients separtaed by commas: \n")
con = input("Enter in the constants of the equations separted by commas: \n")
r1 = r1.split(",")
r2 = r2.split(",")
r3 = r3.split(",")
con = con.split(",")

```

After the values were entered in, I was able to separate the information and reassign them to their respective variables.

```Python
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

```

Once everything was set up, I would run it through my equations. Then DX, DY and DZ would be checked to see if any of their values were zero. If they were then the program would display infinite solutions, then end the program.

```python
D = X1*((Y2*Z3)-(Y3*Z2))-X2*((Y1*Z3)-(Y3*Z1))+X3*((Y1*Z2)-(Y2*Z1))
DX = X*((Y2*Z3)-(Y3*Z2))-Y*((Y1*Z3)-(Y3*Z1))+Z*((Y1*Z2)-(Y2*Z1))
DY = -X*((X2*Z3)-(X3*Z2))+Y*((X1*Z3)-(X3*Z1))-Z*((X1*Z2)-(X2*Z1))
DZ = X*((X2*Y3)-(X3*Y2))-Y*((X1*Y3)-(X3*Y1)) +Z*((X1*Y2)-(X2*Y1))


if DX == 0 or DY == 0 or DZ == 0:
    print("This equation has infinant solutions")
    return
```

The program is then designed to try to find X, Y and Z but if D is a zero then normally you could get a ZeroDivisionError that would abruptly end the program. In my code if this error does accrue then it would display that this equation has no solution. If this does not accrue then the X, Y and Z would be displayed to the user.

```python
try:
    X = DX/D
    Y = DY/D
    Z = DZ/D
    print(f"({X}, {Y}, {Z})")
except ZeroDivisionError:
    print("This equation has no solution.")
```

If you would like to see the code file click [here](https://github.com/Jase-Dryden/Math/blob/main/System_of_Equations/Math_109_01.py).