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


def great_circle_distance(p1: Tuple, p2: Tuple) -> float:
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
