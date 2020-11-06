import geopandas as gpd

geo_data = 'data/older_seoul.geojson'

df = gpd.read_file(geo_data)
df.head()