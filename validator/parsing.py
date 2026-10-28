def parse_reading(line):
    sensor_id, value, unit = line.split(",")
    return sensor_id, float(value), unit


#example
#print(parse_reading("id:0192,92,F"))