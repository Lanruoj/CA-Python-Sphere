import math

#Welcome message
welcome = "\nHello! This program will ask for you to provide a length (in metres). It will then give you three results:\n- The surface area and volume of a cube with that side length\n- The surface area and volume of a regular pyramid with that side length\n- The surface area and volume of a sphere with that radius.\n"
print(welcome)
# Ask for radius
prompt = "Type length here:  "
# Store response to prompt as "radius"
length = float(input(prompt))
# Constants
pi = 3.1416
# Formulae
## Cube
cube_surface_area = 6 * (length**2)
cube_volume = length**3
## Pyramid
pyramid_surface_area = (length**2) + (2 * length) * math.sqrt((length**2)/4 + (length**2))
pyramid_volume = length **3 / 3
## Sphere
sphere_surface_area = 4 * pi * (length**2)
sphere_volume =  4/3 * pi * length**3
# Print results
print("\n---RESULTS---")
## Cube results
print("\n---CUBE---" + "\nSurface area: " + str(cube_surface_area) + "\nVolume: " + str(cube_volume) + "\n")
## Pyramid results
print("\n---PYRAMID---" + "\nSurface area: " + str(pyramid_surface_area) + "\nVolume: " + str(pyramid_volume) + "\n")
## Sphere results
print("\n---SPHERE---" + "\nSurface area: " + str(sphere_surface_area) + "\nVolume: " + str(sphere_volume) + "\n")
