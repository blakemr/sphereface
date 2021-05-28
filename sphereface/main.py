from typing import Tuple


def dms2dd(d: float, m: float, s: float, sign: bool) -> float:
    '''Converts degree, minutes, seconds coordinates to decimal degree format

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
