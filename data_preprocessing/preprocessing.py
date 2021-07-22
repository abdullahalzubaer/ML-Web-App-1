import pandas as pd
import pickle
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error


df = pd.read_csv('PATH_TO_THE_DATASET')


df = df[["Country", "EdLevel", "YearsCodePro", "Employment",
         "ConvertedComp"]]  # Features we are going to utilize
df = df.rename({"ConvertedComp": "Salary"}, axis=1)  # Column renaming
# Drop rows which contain missing values (i.e. drop all rows that containst NaN)
df = df.dropna(axis=0)
# Keeping the users that has been "Employed full-time" only
df = df[df["Employment"] == "Employed full-time"]
df = df.drop(labels="Employment", axis="columns")  # Now dropping the column of Employment
# Remove countries that are present less than 400 times in the dataset (Treating them as outlier)
df = df.groupby('Country').filter(lambda x: len(x) > 400)

# To inspct the salary range using boxplot and removing those samples that has below or above a threshold - this is used to remove outlier.
# plt.style.use('ggplot')
# df.boxplot('Salary', 'Country', figsize=(12,7), rot = 90,)
# Inspect the salary range and remove the outliers.

# Keeping only the persons that has salaries bigger than and smaller than a threshold.
df = df[df["Salary"] <= 250000]
df = df[df["Salary"] > 10000]


# df['YearsCodePro'].unique()


# Creating a function so that we can apply to YearsCodePro attributes value and convert
# them into float (including the two string that it has)

def clean_experience(x):
    if x == "More than 50 years":
        return 50
    elif x == "Less than 1 year":
        return 0.5
    else:
        return float(x)

# apply this to "YearsCodePro" column


df['YearsCodePro'] = df['YearsCodePro'].apply(clean_experience)


# for EdLevel convert to int from string

def clean_education(x):
    if "Bachelor’s degree" in x:
        return "Bachelor’s degree"
    elif "Master’s degree" in x:
        return "Master’s degree"
    elif "Professional degree" in x or "Other doctoral degree" in x:
        return "Post grad"
    else:
        return "Less than a Bachelors"

# apply this to "EdLevel"


df['EdLevel'] = df['EdLevel'].apply(clean_education)

# Label Encoding
# For predicting from user input we need to use the same encoding mechanism we are using here
le_education = LabelEncoder()
df['EdLevel'] = le_education.fit_transform(df['EdLevel'])

le_country = LabelEncoder()
df['Country'] = le_country.fit_transform(df['Country'])


# Creating x and y

X = df.drop("Salary", axis="columns")  # axis = 1
Y = df['Salary']


X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.33, random_state=42)


random_forest_regressor = RandomForestRegressor(random_state=0)

parameter = {'max_depth': [2, 4, 6, 8, 10, 12],
             'n_estimators': [10, 30, 60, 80, 100, 200],
             'min_samples_leaf': [5, 10, 20, 30, 60]}

# we are doing CV for X_train and y_train (Not on the whole dataset, we can do that also then we have to pass all the data - but we kept it for testing)
gs = GridSearchCV(random_forest_regressor, param_grid=parameter, cv=5)
gs.fit(X_train, y_train)

# Final model
regressor = gs

# y_predict = gs.best_estimator_.predict(X_test)
# error = mean_absolute_error(y_true = y_test,y_pred=y_predict)
# print((error))


# Save model and the label encoders also since they will be needed to encode the user input in the app

data = {"model": regressor, "le_country": le_country, "le_education": le_education}
path_save_pickle = PATH_TO_PICKLE_DESTINATION
with open(path_save_pickle, 'wb') as file:
    pickle.dump(data, file)

# Open the file
# with open(path_save_pickle, 'rb') as file:
#     data = pickle.load(file)
