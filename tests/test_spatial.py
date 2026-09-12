import pytest
from shapely.geometry import Polygon

from spatial import Point, Parcel
def test_valid_point():
    point = Point("A", 121.0, 14.6, name="Gate", tag="POI")

    assert point.id == "A"
    assert point.lon == 121.0
    assert point.lat == 14.6

def test_invalid_longitude():
    with pytest.raises(ValueError):
        Point("B", 200.0, 14.6)

def test_point_intersects_parcel():
    geom = Polygon([
        (0, 0),
        (10, 0),
        (10, 5),
        (0, 5)
    ])

    parcel = Parcel(101, geom, {})
    point = Point("P1", 2, 2)

    assert point.intersects(parcel) is True

def test_point_outside_parcel():
    geom = Polygon([
        (0, 0),
        (10, 0),
        (10, 5),
        (0, 5)
    ])

    parcel = Parcel(101, geom, {})
    point = Point("P2", 12, 2)

    assert point.intersects(parcel) is False

def test_from_dict_valid():
    record = {
        "id": "C",
        "lon": 121.05,
        "lat": 14.65,
        "name": "Library",
        "tag": "POI",
    }

    point = Point.from_dict(record)

    assert point.id == "C"
    assert point.lon == 121.05
    assert point.lat == 14.65
    assert point.name == "Library"
    assert point.tag == "POI"

def test_from_dict_invalid():
    record = {
        "id": "D",
        "lon": 200.0,
        "lat": 14.65,
        "name": "Invalid Point",
        "tag": "POI",
    }

    with pytest.raises(ValueError):
        Point.from_dict(record)