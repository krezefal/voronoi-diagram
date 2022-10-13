import math
import PIL
from PIL import Image

from base_station import *

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


def calc_distance(*, x1, y1, x2, y2):
    distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    return distance


print("Enter field size (height, width) and number of base stations:")
height, width, stations_number = [int(num) for num in input().split()]

voronoi_diag = PIL.Image.new(mode="RGB", size=(width, height), color=WHITE)
base_stations = []

random_fill_mode = input("Do you want to enter coordinates manually? [y/n]\n")

for i in range(stations_number):
    print(f"Coordinates of base station #{i+1}: ", end='')
    if random_fill_mode != "y":
        x, y = randint(0, width - 1), randint(0, height - 1)
        print(x, y)
    else:
        x, y = [int(coord) for coord in input().split()]
    base_stations.append(BaseStation(x=x, y=y, rand_color=True))

for i in range(height):
    for j in range(width):
        min_distance = math.inf
        nearest_station = None
        for base_station in base_stations:
            cur_distance = calc_distance(x1=j, y1=i, x2=base_station.x, y2=base_station.y)
            if cur_distance <= min_distance:
                min_distance = cur_distance
                nearest_station = base_station
        voronoi_diag.putpixel((j, i), nearest_station.color)

for base_station in base_stations:
    voronoi_diag.putpixel((base_station.x, base_station.y), BLACK)

voronoi_diag.show()
