side1 = int(input("Enter side 1 of tringle:"))
side2 = int(input("Enter side 2 of tringle:"))
side3 = int(input("Enter side 3 of tringle:"))

if (side1 < side2 + side3) & (side2 < side1 + side3) & (side3 < side1 + side2) :
    print("We can have this triangle :) ")

else:
    print("Not a triangle :( ")