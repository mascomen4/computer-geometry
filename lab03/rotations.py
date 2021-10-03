# Main functions
# Imported from lab02

import numpy as np


def xy_rotation(points, xy, rad=None, deg=None):
    """
    Function to rotate an arbitrary polygon w.r.t. any point xy.
    :param points: np.array of points representing array; shape is [-1, 2]
    :param xy: np.array input point
    :param rad: angle in radians.
    :param deg: angle in degrees.
    :return: np.array of transformed points.
    """
    if rad:
        angle = rad
    elif deg:
        angle = deg * np.pi / 180
    else:
        print("Please, feed the angle in rad or deg!")
        return 1

    rot = np.array([[np.cos(angle), -np.sin(angle)],
                   [np.sin(angle), np.cos(angle)]])
    # User can forget that we need point as np.array
    xy = np.array(xy)
    # Rotate the polygon
    # print("Points are", points)
    # print("Translated points are", points - xy)
    rotated_points = (points - xy) @ rot
    # Go back to the origin
    rotated_points += xy

    return rotated_points


def center_rotation(points, rad=None, deg=None):
    """
    Function to rotate an arbitrary polygon around it's center.
    :param points: np.array of points representing array; shape is [-1, 2]. The last element has to be the same as the
    first element, to make a closure of the polygon.
    :param rad: angle in radians. If rad and ged are both passed, it will choose the rad.
    :param deg: angle in degrees
    :return: np.array of rotated points
    """
    if rad:
        angle = rad
    elif deg:
        angle = deg * np.pi / 180
    else:
        print("Please, feed the angle in rad or deg!")
        return 1

    # Take the average over all x, and the average over all y to find the center.
    # The last element is the first element -> do not consider it.
    x = np.mean(points[:-1, 0])
    y = np.mean(points[:-1, 1])
    # np.c_[] has the same effect as np.hstack()
    xy = np.c_[x, y]
    rotated_points = xy_rotation(points, xy, angle)

    return rotated_points


def vector_transl(points, vec, xy_transl):
    """
    Function to translate the polygon among the chosen vector.
    :param points: np.array of shape [-1, 2], of polygon points
    :param vec: np.array [x,y], representing the desired vector
    :param xy_transl: np.array [x,y], representing the x and y translation.
    :return: np.array of shape [-1, 2]
    """
    transl = vec * xy_transl
    points = points + transl
    return points


def bisector_mirror(points):
    """
    Mirrors the polygon w.r.t bisector of the 1 quarter of the Cartesian coordinate system.
    :param points: np.array of shape [-1, 2], of polygon points
    :return: np.array of shape [-1, 2]
    """
    # Matrix is obtained from the lectures.
    mir = np.array( [[0, 1],
                     [1, 0]] )
    return points @ mir

