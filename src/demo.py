from spatial import Point

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