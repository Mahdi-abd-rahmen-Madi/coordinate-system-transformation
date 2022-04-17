import math
def arc_to_deg(arc):
    """convert spherical arc length [m] to great circle distance [deg]"""
    return float(arc)/6371/1000 * 180/math.pi

def deg_to_arc(deg):
    """convert great circle distance [deg] to spherical arc length [m]"""
    return float(deg)*6371*1000 * math.pi/180

def latlon_to_xyz(lat,lon):
    """Convert angluar to cartesian coordiantes

    latitude is the 90deg - zenith angle in range [-90;90]
    lonitude is the azimuthal angle in range [-180;180] 
    """
    r = 6371 # https://en.wikipedia.org/wiki/Earth_radius
    theta = math.pi/2 - math.radians(lat) 
    phi = math.radians(lon)
    x = r * math.cos(theta) * math.cos(phi) # bronstein (3.381a) # the x-axis goes through long,lat (0,0), so longitude 0 meets the equator
    y = r * math.sin(theta) * math.cos(phi) # the y-axis goes through (0,90)
    z = r * math.sin(theta) # and the z-axis goes through the poles.
    return [x,y,z]

def xyz_to_latlon (x,y,z):
    """Convert cartesian to angular lat/lon coordinates"""
    r = math.sqrt(x**2 + y**2 + z**2)
    theta = math.asin(z/r) # https://stackoverflow.com/a/1185413/4933053
    phi = math.atan2(y,x)
    lat = math.degrees(theta)
    lon = math.degrees(phi)
    return [lat,lon]
