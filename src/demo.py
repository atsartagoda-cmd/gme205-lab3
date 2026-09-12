from spatial import Point, Parcel
from shapely.geometry import Polygon

p = Point("A", 121.0, 14.6, name="Gate", tag="POI")

print(p.id)
print(p.lon, p.lat)
print(p.to_tuple())
print(p.geometry.geom_type)

print()
print(p.as_dict())

d = {
    "id": "B",
    "lon": 121.05,
    "lat": 14.65,
    "name": "Library",
    "tag": "POI",
}

q = Point.from_dict(d)

print()
print(q.id)
print(q.lon, q.lat)
print(q.name)
print(q.is_poi())
print()
print("Inherited bbox:", p.bbox())

r = Point("C", 121.1, 14.7)

print("Intersects different location:", p.intersects(r))

attributes = {
    "area": 50.0,
    "zone": "Residential",
    "is_active": True
}

geom = Polygon([
    (0, 0),
    (10, 0),
    (10, 5),
    (0, 5)
])

parcel = Parcel(101, geom, attributes)

print(parcel.bbox())
print(parcel.as_dict())

inside = Point("IN", 2, 2)
outside = Point("OUT", 12, 2)

print(inside.intersects(parcel))   # True
print(outside.intersects(parcel))  # False