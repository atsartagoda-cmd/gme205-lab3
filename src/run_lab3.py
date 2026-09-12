import json
from pathlib import Path

import matplotlib.pyplot as plt
from shapely.geometry import Polygon

from spatial import Point, Parcel

def main():
    # construct / load objects
    point = Point("A", 121.0, 14.6, name="Gate", tag="POI")

    geom = Polygon([
        (0, 0),
        (10, 0),
        (10, 5),
        (0, 5)
    ])

    parcel = Parcel(
        101,
        geom,
        {
            "area": 50.0,
            "zone": "Residential",
            "is_active": True
        }
    )

    inside = Point("IN", 2, 2)
    outside = Point("OUT", 12, 2)

    # evaluate relationships
    inside_intersects = inside.intersects(parcel)
    outside_intersects = outside.intersects(parcel)

    # build report dictionary
    report = {
    "point": point.as_dict(),
    "parcel": parcel.as_dict(),
    "relationships": {
        "inside_intersects_parcel": inside_intersects,
        "outside_intersects_parcel": outside_intersects,
    }
}
    # write JSON
    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)

    report_path = output_dir / "lab3_report.json"

    with open(report_path, "w") as f:
        json.dump(report, f, indent=2)

    # create preview figure
    fig, ax = plt.subplots()
    x, y = parcel.geometry.exterior.xy
    ax.plot(x, y)
    ax.scatter([inside.lon, outside.lon],
               [inside.lat, outside.lat])
    ax.set_aspect("equal")
    ax.set_title("Lab 3 Spatial Objects Preview")

    preview_path = output_dir / "lab3_preview.png"
    fig.savefig(preview_path)
    plt.close(fig)

if __name__ == "__main__":
    main()