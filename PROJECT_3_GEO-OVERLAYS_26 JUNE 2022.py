import folium
import folium as fl
import pandas as pd
import warnings
warnings.filterwarnings(("ignore"))
country_geo = (r'C:\Users\Home\Desktop\DATA SCIENCE CLASS\26th JUNE 2022\EXTRACT\Projects\data\world-countries.json')

data = pd.read_csv(r'C:\Users\Home\Desktop\DATA SCIENCE CLASS\26th JUNE 2022\data\Indicators.bz2',compression='bz2')
print("Data Shape: ",data.shape)
print("Sample Data: ",data.head())

hist_indicator = 'CO2 emissions \(metric'
hist_year = 1980
mask1 = data['IndicatorName'].str.contains(hist_indicator)
mask2 = data['Year'].isin([hist_year])

stage = data[mask1 & mask2]
stage.head()

plot_data = stage[['CountryCode', 'Value']]
plot_data.head()

hist_indicator = stage.iloc[0]['IndicatorName']
print(hist_indicator)

map = fl.Map(location=[100,0], titles="CO2 Emissions by Country", zoom_start=1.5)
map.choropleth(geo_data = country_geo, data=plot_data, columns=['CountryCode','Value'],
               key_on='feature.id',fill_color='YlGnBu', fill_opacty=0.7, line_opacity=0.1,
               legend_name=hist_indicator)

map.save(r'C:\Users\Home\Desktop\DATA SCIENCE CLASS\26th JUNE 2022\saved_info\plot_data2.html')

from IPython.display import HTML
HTML('<iframe src=saved_info/plot_data.html width=700 height=450></iframe>')