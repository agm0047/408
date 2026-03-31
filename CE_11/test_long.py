import numpy
def normalize_longitude(lon: float) ->float:
    """ Normalize a longitude value to be in a range of (-180, 180)."""
    if lon > 180:
        return lon - 360
    elif lon < -180:
        return lon + 360
    else:
        return lon  