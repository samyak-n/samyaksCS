import funcs_objects
import objects


def distance_all(list_of_points):
    return [funcs_objects.distance(point, objects.Point(0, 0)) for point in
            list_of_points]


def are_in_first_quadrant(list1):
    return [point for point in list1 if point.x > 0 and point.y > 0]
