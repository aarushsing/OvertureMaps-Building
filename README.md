# OvertureMaps-Building

This repository provides a Python script to retrieve building polygon data from the [Overture Maps](https://overturemaps.org) dataset based on specific coordinates. The script leverages the `overturemaps` command-line utility to download GeoJSON building data within a small bounding box around each coordinate.

## Installation

1. **Install the Overture Maps CLI**
   Ensure the `overturemaps` package is installed and accessible from the system's PATH.

   ```bash
   pip install overturemaps
   ```

2. **Clone the Repository**

   ```bash
   git clone https://github.com/aarushsing/OvertureMaps-Building.git
   cd OvertureMaps-Building
   ```

## Usage

The main script, `buildings.py`, downloads GeoJSON files containing building footprint data for given coordinates. It generates a bounding box around each coordinate and uses it to query the Overture Maps dataset.

### 1. Building a Bounding Box
The `generate_bbox` function in the script creates a small buffer (default: **0.0005 degrees**) around each coordinate to ensure that building data is captured even if the footprint is slightly offset from the specified point. With this buffer, the bounding box is approximately **50m x 50m** in area (depending on latitude), which typically limits the result to 4-10 polygons.

### 2. Downloading Polygon Data
The `download_polygon_data` function calls the `overturemaps` utility through `subprocess` to fetch building data for the bounding box. Each building's data is saved as a GeoJSON file named according to the building ID, e.g., `building_3071.geojson`.

## Running the Script

1. Ensure the `overturemaps` CLI is installed.
2. Run the script:

   ```bash
   python buildings.py
   ```

3. Output files will be generated in the same directory as the script, with names in the format `building_<ID>.geojson`.

## Examples

For reference, the `examples/` folder contains sample GeoJSON output files demonstrating the expected structure of the data.

## Explanation of the Code

- **generate_bbox**: Generates a small bounding box around each latitude and longitude pair.
- **download_polygon_data**: Uses the bounding box to download building data as GeoJSON files.
- **main**: Loops through a list of buildings, calling `download_polygon_data` for each.

## Contributing

Feel free to open issues or submit pull requests to improve this script. Contributions are welcome!
