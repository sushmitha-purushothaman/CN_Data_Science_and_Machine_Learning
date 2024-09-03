## Open and read data file as specified in the question
## Print the required output in given format
#import pandas as pd
#df = pd.read_csv(r"https://files.codingninjas.in/iris-8116.csv", encoding = 'utf-8')
#filtered_df = df[(df['variety'] == 'Iris-virginica') & (df['petal.length'] > 1.5)]
#print(filtered_df.to_string(header = False, index = False))



# Import pandas library as pd
import pandas as pd

# Read the dataset from the given URL
df = pd.read_csv("https://files.codingninjas.in/iris-8116.csv")

# Filter the rows having variety as "Iris-virginica" and petal length greater than 1.5
filtered_df = df[(df['variety'] == 'Iris-virginica') & (df['petal.length'] > 1.5)]


## changes required ##
# Loop through each row of the filtered dataframe
for i in filtered_df.values:
    # Loop through each element in the row and print it with a space separator
    for j in i:
        print(j, end=" ")
    # Print a new line at the end of each row
    print()