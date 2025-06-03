# cython: boundscheck=False, wraparound=False, cdivision=True
from cython cimport boundscheck, wraparound
from libc.math cimport fabs

cdef inline bint ccw(double x1, double y1, double x2, double y2, double x3, double y3):
    return (y3 - y1) * (x2 - x1) > (y2 - y1) * (x3 - x1)

cdef inline bint lines_intersect(double x1, double y1, double x2, double y2,
                                 double x3, double y3, double x4, double y4):
    return (ccw(x1, y1, x3, y3, x4, y4) != ccw(x2, y2, x3, y3, x4, y4) and
            ccw(x1, y1, x2, y2, x3, y3) != ccw(x1, y1, x2, y2, x4, y4))

def check_line_intersects_polygon(object line_start, object line_end, object polygon_points):
    cdef double ax = line_start[0]
    cdef double ay = line_start[1]
    cdef double bx = line_end[0]
    cdef double by = line_end[1]

    cdef int n = len(polygon_points)
    cdef int i
    cdef double x3, y3, x4, y4

    for i in range(n):
        x3 = polygon_points[i][0]
        y3 = polygon_points[i][1]
        x4 = polygon_points[(i + 1) % n][0]
        y4 = polygon_points[(i + 1) % n][1]
        if lines_intersect(ax, ay, bx, by, x3, y3, x4, y4):
            return True
    return False

def calculate_convexity(object polygon_points, object grid_points):
    cdef int intersecting_lines = 0
    cdef int total_comparisons = 0
    cdef int i, j

    for i in range(len(grid_points)):
        for j in range(i + 1, len(grid_points)):
            total_comparisons += 1
            if check_line_intersects_polygon(tuple(grid_points[i]), tuple(grid_points[j]), polygon_points):
                intersecting_lines += 1

    if total_comparisons == 0:
        return 1.0
    return 1.0 - intersecting_lines / total_comparisons
