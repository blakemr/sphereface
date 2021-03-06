from typing import Tuple
from math import radians, sin, cos

EARTH_RADIUS_METERS = 6371000


def dms2dd(d: float, m: float, s: float, sign: bool) -> float:
    ''' Converts degree, minutes, seconds coordinates to decimal degree format

    args:
        d, m, s (float): degrees, minutes, seconds
        sign (bool): hemisphere. N or E should be True, S or W should be False

    return:
        float: input returned in decimal degree format
    '''
    dd = d
    dm = m / 60.0
    ds = s / 3600.0
    dh = 1 if sign else -1

    return (dd + dm + ds) * dh


# def dd2cart(p: Tuple[float, float]) -> Tuple[float, float, float]:
#     ''' Convert decimal degrees to cartesian coordinates

#     args:
#         p (tuple): lat/long coordinate pair
    
#     return:
#         Tuple representing the x, y, z coordinates
#     '''
#     lat, lon = p

#     x = sin(lat) * cos(lon)
#     y = sin(lat) * sin(lon)
#     z = cos(lat)

#     return x, y, z


def great_circle_length(
    p1: Tuple[float, float],
    p2: Tuple[float, float]
) -> float:
    ''' Returns the shortest distance between two points on a sphere

    args:
        p1, p2 (lat, lon): latitude, longitude tuples for
            each point in decimal degrees

    return:
        distance between the two points in meters
    '''
    lat1, lon1 = p1
    lat2, lon2 = p2

    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)

    # Haversine
    dla = lat1 - lat2
    dlo = lon1 - lon2

    h = sin(dla / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlo / 2) ** 2

    r2 = 2 * EARTH_RADIUS_METERS

    return h * r2

# TODO: Put together a function to work in rotations.  
# Things get much easier. Pretty sure I'm missing something obvious.

# def slerp(p1: float, p2: float, t: float) -> Tuple[float, float]

# Planned:
# terminal coordinates
# projection point
# line of sight
# Vertical angle
# bearing-angles
# point-along-line
# surface centroid
# point-circle around target
# normals
