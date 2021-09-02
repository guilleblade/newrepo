import geocoder

#forward geocoding
g = geocoder.osm('Waco, Tx')
print(g.latlng)
print(g.postal)
print(g.country)
print("\n")

# reverse geocoding
print("Reverse Example")
g = geocoder.arcgis([45.15, -75.14], method='reverse')
print(g.city)
print(g.state)
print(g.country)
print("\n")

# IP address 1
print("IP Address Example 1")
g = geocoder.ip('199.7.157.0')
print(g.ip)
print(g.postal)
print(g.latlng)
print(g.city + " " + g.state)
print("\n")

# IP address 2
print("IP Address Example 2")
g = geocoder.ip('me')
print(g.ip)
print(g.postal)
print(g.latlng)
print(g.city + " " + g.state)
print("\n")

# house address
print("House Address")
g = geocoder.osm("453 Booth Street, Ottawa ON")
print(g.housenumber)
print(g.postal)
print(g.street)
print(g.city)
print(g.state)
print(g.country)