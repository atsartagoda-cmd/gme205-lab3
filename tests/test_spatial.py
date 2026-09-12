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

def test_point_bbox():
    point = Point("A", 121.0, 14.6)
    assert point.bbox() == (121.0, 14.6, 121.0, 14.6)

def test_parcel_bbox():
    geometry = Polygon([
        (0, 0),
        (10, 0),
        (10, 5),
        (0, 5)
    ])
    parcel = Parcel(101, geometry, {"zone": "Residential"})

    assert parcel.bbox() == (0.0, 0.0, 10.0, 5.0)

def test_as_dict_contains_no_shapely_objects():
    point = Point("A", 121.0, 14.6, name="Gate", tag="POI")
    point_result = point.as_dict()

    assert isinstance(point_result["geometry"], list)
    assert point_result["geometry"] == [121.0, 14.6]

    geometry = Polygon([
        (0, 0),
        (10, 0),
        (10, 5),
        (0, 5)
    ])
    parcel = Parcel(101, geometry, {"zone": "Residential"})
    parcel_result = parcel.as_dict()

    assert isinstance(parcel_result["bbox"], list)
    assert parcel_result["bbox"] == [0.0, 0.0, 10.0, 5.0]