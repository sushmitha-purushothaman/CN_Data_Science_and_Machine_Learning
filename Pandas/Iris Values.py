import pandas as pd

# Step 1: Define the column names to be used when loading the dataset
column_name = ['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth', 'variety']

# Step 2: Load the Iris dataset from the given URL into a DataFrame
# The 'names' parameter assigns the specified column names to the dataset
df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data', names=column_name)

# Step 3: Filter the DataFrame for each variety of iris and use the 'describe()' method
# This generates descriptive statistics for each variety (Iris-setosa, Iris-versicolor, Iris-virginica)
# The 'describe()' method returns a DataFrame that includes count, mean, std, min, 25%, 50%, 75%, and max values
set = df[df['variety'] == 'Iris-setosa'].describe()
ver = df[df['variety'] == 'Iris-versicolor'].describe()
vir = df[df['variety'] == 'Iris-virginica'].describe()

# Step 4: Extract and print the minimum values (3rd row of 'describe()' output) for Iris-setosa
for i in set.iloc[[3]].values[0]:
    print(format(i, '.2f'), end=" ")  # Print each value formatted to 2 decimal places
print('Iris-setosa')  # Print the variety name after the values

# Step 5: Extract and print the maximum values (7th row of 'describe()' output) for Iris-setosa
for i in set.iloc[[7]].values[0]:
    print(format(i, '.2f'), end=" ")
print('Iris-setosa')

# Step 6: Extract and print the mean values (1st row of 'describe()' output) for Iris-setosa
for i in set.iloc[[1]].values[0]:
    print(format(i, '.2f'), end=" ")
print('Iris-setosa')

# Repeat Steps 4-6 for the other varieties (Iris-versicolor and Iris-virginica)

# Step 7: Extract and print the minimum values for Iris-versicolor
for i in ver.iloc[[3]].values[0]:
    print(format(i, '.2f'), end=" ")
print('Iris-versicolor')

# Step 8: Extract and print the maximum values for Iris-versicolor
for i in ver.iloc[[7]].values[0]:
    print(format(i, '.2f'), end=" ")
print('Iris-versicolor')

# Step 9: Extract and print the mean values for Iris-versicolor
for i in ver.iloc[[1]].values[0]:
    print(format(i, '.2f'), end=" ")
print('Iris-versicolor')

# Step 10: Extract and print the minimum values for Iris-virginica
for i in vir.iloc[[3]].values[0]:
    print(format(i, '.2f'), end=" ")
print('Iris-virginica')

# Step 11: Extract and print the maximum values for Iris-virginica
for i in vir.iloc[[7]].values[0]:
    print(format(i, '.2f'), end=" ")
print('Iris-virginica')

# Step 12: Extract and print the mean values for Iris-virginica
for i in vir.iloc[[1]].values[0]:
    print(format(i, '.2f'), end=" ")
print('Iris-virginica')
