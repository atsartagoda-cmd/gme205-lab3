# GmE 205 Laboratory Exercise 3: Spatial Object Systems in Python

## Description

This laboratory exercise explores how spatial entities can be represented as Python objects and how geometric relationships can be evaluated using Shapely. It demonstrates the use of Point and Parcel objects, coordinate validation, spatial intersection, and the conversion of input data into spatial objects for analysis.

## Getting Started

### Dependencies
- Python 3.14.7
- pandas
- matplotlib
- Shapely
- pytest

### Installing

Create and activate a virtual environment, then install the required dependencies:

```powershell
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

### Executing Program

Run the main laboratory script:

```powershell
python src/run_lab3.py
```

### Tests

Run the test suite using pytest:

```powershell
$env:PYTHONPATH = "src"
pytest
```

## Outputs

Running the main laboratory script generates the following files in the `output/` folder:

- `lab3_report.json` – contains the computed results for the spatial objects and operations.
- `lab3_preview.png` – provides a visual preview of the Point and Parcel objects used in the exercise.

## Help

If the program does not run correctly, make sure the virtual environment is activated and all required dependencies have been installed from `requirements.txt`.

For test-related issues, make sure the `PYTHONPATH` is set to `src` before running `pytest`.

## Author

Airah Shayne T. Sartagoda

## Version History

- 0.1
  - Initial project setup

## License

Not applicable for this laboratory exercise.

## Acknowledgements

- GmE 205 Laboratory Exercise 3 instructions

## Reflections

### 1. Refactoring
What changed in the internal representation of Point? What remained stable for code using the object?

`Point` now uses a Shapely geometry to represent its location instead of relying only on separate longitude and latitude values. Even with this change, properties like `lon`, `lat`, `id`, `name`, and `tag` can still be used the same way.

### 2. Responsibility
Which behavior now belongs to Shapely, which belongs to SpatialObject, and which remains specific to Point or Parcel?

Shapely handles the geometry and spatial operations. `SpatialObject` provides shared behaviors like `bbox()` and `intersects()`, while `Point` and `Parcel` handle the details specific to each type of spatial object.

### 3. Data Boundary
Why should from_dict() delegate validation to the constructor?

`from_dict()` should let the constructor handle validation so the same rules are applied whenever a `Point` is created. This also avoids repeating validation code in different parts of the program.

### 4. Output Boundary
Why should as_dict() return primitive / JSON-ready values rather than Shapely geometry objects?

`as_dict()` returns simple, JSON-ready values because Shapely geometry objects cannot be stored directly in JSON. This also makes the output easier to save, read and reuse.

### 5. Inheritance
Why does intersects() belong in SpatialObject instead of being duplicated in Point and Parcel?

`intersects()` belongs in `SpatialObject` because both `Point` and `Parcel` can use it. Keeping it in one shared class avoids repeating the same code.

### 6. Coordinate Meaning
Why is geometry.distance() not automatically a real-world distance in meters for longitude/latitude data?

`geometry.distance()` uses the units of the coordinates provided. Since longitude and latitude are measured in degrees, the result should not automatically be interpreted as meters.

### 7. Scale
If the system grows to millions of objects, what part of this design helps maintainability, and what performance problems would still require different techniques?

The class structure makes the program easier to maintain and expand because shared and object-specific behaviors are clearly separated. However, handling millions of spatial objects would still require more efficient approaches, such as spatial indexing, databases, or batch processing.