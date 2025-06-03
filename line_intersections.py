import phanim as p
import numpy as np
from geometry.geometry import check_line_intersects_polygon

line_start = (0.0, 0.0)
line_end = (5.0, 5.0)
polygon = [(1.0, 1.0), (4.0, 1.0), (4.0, 4.0), (1.0, 4.0)]

def calculate_polygon_bounds(point_list):
    min_x = min(point_list, key=lambda x: x[0])[0]
    min_y = min(point_list, key=lambda x: x[1])[1]
    max_x = max(point_list, key=lambda x: x[0])[0]
    max_y = max(point_list, key=lambda x: x[1])[1]
    return min_x, min_y, max_x, max_y

def create_grid_point_list(min_x, min_y, max_x, max_y, resolution):
    point_list = []
    for x in np.linspace(min_x, max_x, resolution):
        for y in np.linspace(min_y, max_y, resolution):
            point_list.append([x, y])
    return point_list

concave_decagon = [
    [0, 0],
    [2, 1],
    [4, 0],
    [5, 2],
    [4, 4],
    [3, 2.5],
    [2, 4],
    [0, 4],
    [-1, 2],
    [1, 1.5]
]


resolution = 10

screen = p.Screen(resolution=(800,600), fullscreen=False, grid=False)

edges = [[i,i+1] for i in range(len(concave_decagon)-1)]+[[len(concave_decagon)-1,0]]
polygon = p.Graph(len(concave_decagon), edges, initalPositions=concave_decagon)

screen.add(polygon)

line_points = [[0-2,3],[1,3]]

line = p.Graph(2, [[0,1]])
screen.add(line)
screen.makeInteractive(line)
screen.makeInteractive(polygon)

def update(s):
    if check_line_intersects_polygon(tuple(line.positions[0]), tuple(line.positions[1]), polygon.positions):
        line.groupObjects[0].color = (0, 255, 0)
    else:
        line.groupObjects[0].color = (255, 0, 0)

screen.addUpdater(update)

screen.run()
