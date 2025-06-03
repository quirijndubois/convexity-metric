import phanim as p
import numpy as np
from geometry.geometry import check_line_intersects_polygon, calculate_convexity

def calculate_convexity(polygon_points, grid_points):
    polygon_points = [tuple(x) for x in polygon_points]

    intersecting_lines = 0
    total_comparisons = 0
    for i in range(len(grid_points)):
        for j in range(i+1, len(grid_points)):
            total_comparisons += 1
            if check_line_intersects_polygon(tuple(grid_points[i]), tuple(grid_points[j]), polygon_points):
                intersecting_lines += 1
    return 1 - intersecting_lines / total_comparisons

def calculate_polygon_bounds(point_list):
    min_x = min(point_list, key=lambda x: x[0])[0]
    min_y = min(point_list, key=lambda x: x[1])[1]
    max_x = max(point_list, key=lambda x: x[0])[0]
    max_y = max(point_list, key=lambda x: x[1])[1]
    return min_x, min_y, max_x, max_y

def create_grid_point_list(min_x, min_y, max_x, max_y, resolution, polygon_points):
    point_list = []
    for x in np.linspace(min_x, max_x, resolution):
        for y in np.linspace(min_y, max_y, resolution):
            if p.is_point_in_polygon([x,y], polygon_points):
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
screen.makeInteractive(polygon)

def update(s):
    grid = create_grid_point_list(*calculate_polygon_bounds(polygon.positions), resolution, polygon.positions)
    for point in grid:
        screen.draw(p.Node(radius=.1,pos=point))
    print(calculate_convexity(polygon.positions, grid))

screen.addUpdater(update)

screen.run()
