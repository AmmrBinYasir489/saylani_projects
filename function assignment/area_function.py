def area_of_circle(radius):
    area = 3.14*(radius**2)
    return area

radius_of_circle = int(input("enter the radius of circle: "))
output_area = area_of_circle(radius_of_circle)
print(f"The area of the circle is {output_area}")