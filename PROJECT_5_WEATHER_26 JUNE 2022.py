import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

data = pd.read_csv(r'C:\Users\Home\Desktop\DATA SCIENCE CLASS\26th JUNE 2022\data\data_weather.csv')
print(data)

print('Columns are: ',data.columns)
print("NULL DATA: \n",data[data.isnull().any(axis=1)])

del data ['number']

before_rows = data.shape[0]
print(before_rows)
data = data.dropna()
after_rows = data.shape[0]
print(after_rows)
print("TOTAL ROWS DROPPED: ",before_rows-after_rows)


clean_data = data.copy()
clean_data['high_humidity_label'] = (clean_data['relative_humidity_3pm'] >24.99)*1
print(clean_data['high_humidity_label'])

y=clean_data[['high_humidity_label']].copy()
clean_data['relative_humidity_3pm'].head()
print("Y Data: \n",y.head(7))


morning_features = ['air_pressure_9am', 'air_temp_9am', 'avg_wind_direction_9am',
       'avg_wind_speed_9am', 'max_wind_direction_9am', 'max_wind_speed_9am',
       'rain_accumulation_9am', 'rain_duration_9am', 'relative_humidity_9am',
       'relative_humidity_3pm']

x = clean_data[morning_features].copy()
print('Columns in x: ',x.columns)
print('Columns in y: ',y.columns)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=324)
print("X_TRAIN is as Under: ")
print(x_train.head())
print("X_TEST is as Under: ")
print(x_test.head())
print("Y_TRAIN IS AS UNDER: ")
print(y_train.head())
print("Y TEST IS AS UNDER: ")
print(y_test.head())
print("LET US DESCRIBE Y_TRAIN")

y_train.describe()
humidity_classifier = DecisionTreeClassifier(max_leaf_nodes=10, random_state=0)
humidity_classifier.fit(x_train, y_train)
type(humidity_classifier)


predictions = humidity_classifier.predict(x_test)
print("Sample Predictions: \n",predictions[:10])
print("SAMPLE Y TEST(Actual Data): \n",y_test['high_humidity_label'][:10])

print("Accuracy: \n",accuracy_score(y_true= y_test, y_pred=predictions))




