#function returning another function
#this uses the volume of a cylinder
#created by ikon beth
#DevCUyo100DaysOfCode


#define a function
def cylinder_vol(r):
    pi = 3.141
    def get_vol(h):
        return pi * r**2*h
    return get_vol

#define a radius and get vol function
radius = 10
find_volume = cylinder_vol(radius)
height = 10
print("Volume of cylinder of radius %d and height %d = %.2f cubic units" \
      %(radius, height, find_volume(height)))
height = 20
print("Volume of cylinder of radius %d and height %d = %.2f cubic units" \
      %(radius, height, find_volume(height)))
