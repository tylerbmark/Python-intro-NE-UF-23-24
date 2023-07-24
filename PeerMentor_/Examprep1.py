
def unit_vector():

    n = 3
    for i in range(n):
        x_1,y_1,z_1 = eval(input("Enter the first point in 3d plane:x,y,z"))
        x_2,y_2,z_2 = eval(input("Enter second point in 3d plane:x,y,z"))
        e_1 = (x_2-x_1)
        e_2 = (y_2 -y_1)
        e_3 = (z_2-z_1)
        mag = magnitude(e_1,e_2,e_3)
        vec1 = vec(e1,mag)
        vec2 = vec(e2,mag)
        vec3 = vec(e3,mag)
        print("E1:",e_1 ,"Unit:",vec1)
        print("E2:", e_2, "Unit:", vec2)
        print("E3:", e_3, "Unit:", vec3)
        print("Magnitude:", mag)

def vec(e,mag):
    return e/mag
def magnitude(e_1,e_2,e_3):
    return (e_1 ** 2 + e_2 ** 2 + e_3 ** 2) ** .5

def crossproduct():
    x1,y1,z1 = eval(input("Enter first Unit vector: "))
    x2,y2,z2 = eval(input("Enter second Unit vector: "))
    e1 = (y1*z2-z1*y2)
    e2 = -(x1*z2-x2*z1)
    e3 =(x1*y2-x2*y1)
    print("The Unit vector cross product is: ",e1,"e1", e2, "e2", e3,"e3" )