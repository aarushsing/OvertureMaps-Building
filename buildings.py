import subprocess

def generate_bbox(lat, lon, buffer=0.0005):
    west = lon - buffer
    south = lat - buffer
    east = lon + buffer
    north = lat + buffer
    return (west, south, east, north)

def download_polygon_data(lat, lon, building_id, buffer=0.0005):
    bbox = generate_bbox(lat, lon, buffer)
    output_file = f"building_{building_id}.geojson"
    
    try:
        command = [
            "overturemaps", "download",
            f"--bbox={','.join(map(str, bbox))}",
            "-f", "geojson",
            "-t", "building",
            "-o", output_file
        ]
        
        print(f"Downloading data for Building ID {building_id}...")
        subprocess.run(command, check=True)
        print(f"Polygon data for Building ID {building_id} saved to {output_file}")

    except subprocess.CalledProcessError as e:
        print(f"Error downloading data for Building ID {building_id}: {e}")
    except FileNotFoundError:
        print("Error: Make sure the 'overturemaps' utility is installed and available in PATH.")

def get_building_details(building_id):
    query = f"""
    SELECT names.primary AS name,
           height,
           level
    FROM buildings
    WHERE id = {building_id};
    """
    # Execute the query and return the results (assuming you have database connection code here)
    # For example: 
    # results = execute_query(query)
    # return results

def main():
    buildings = [
        {"id": 3071, "lat": 29.1489, "lon": -82.174222},
        {"id": 3072, "lat": 42.696799, "lon": -84.43616},
        {"id": 3073, "lat": 42.681351, "lon": -84.438764},
        {"id": 3074, "lat": 29.2039, "lon": -82.082178},
        {"id": 3075, "lat": 29.167645, "lon": -82.116866},
        {"id": 3076, "lat": 29.18853, "lon": -82.11497},
        {"id": 3077, "lat": 29.165995, "lon": -82.17293},
        {"id": 3078, "lat": 29.170519, "lon": -82.175797},
        {"id": 3079, "lat": 26.200383, "lon": -80.13317}
    ]
    
    for building in buildings:
        download_polygon_data(building["lat"], building["lon"], building["id"])
        # Optionally retrieve building details
        # details = get_building_details(building["id"])
        # print(details)

if __name__ == "__main__":
    main()
