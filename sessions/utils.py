from __future__ import annotations

def read_rain_data() -> dict[str, list[int] | list[float] | list[bool]]:
    rain = {}
    rain["min"] = []
    rain["max"] = []
    rain["prcp"] = []
    rain["is_raining"] = []
    rain_file = open("../data/rain.csv")
    rain_str = rain_file.read()
    lines = rain_str.split("\n")
    lines = lines[1:] # skip header row
    for line in lines:
        values = line.split(",")[1:]
        
    rain_file.close()
    return rain