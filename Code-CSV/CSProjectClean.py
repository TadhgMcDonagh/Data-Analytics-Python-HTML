#Importing necessary plug-ins and modules
import pandas as pd

#Reading the csv file and turning it into a dataframe
df = pd.read_csv('StudentMentalHealth.csv')

#Error checking
print(df)

#Cleaning data
#Making the strings Upper-Case
df['Choose your gender'] = df['Choose your gender'].str.upper()
df['What is your course?'] = df['What is your course?'].str.upper()
df['Do you have Depression?'] = df['Do you have Depression?'].str.upper()
df['Do you have Anxiety?'] = df['Do you have Anxiety?'].str.upper()
df['Do you have Panic attack?'] = df['Do you have Panic attack?'].str.upper()
#Eliminating Empty Cells
x = df["Age"].mode()[0]

df["Age"].fillna(x, inplace = True)

#Making a smaller dataframe with only necessary data
neededData = df[['Choose your gender', 'Age', 'What is your course?', 'What is your CGPA?', 'Do you have Depression?', 'Do you have Anxiety?', 'Do you have Panic attack?']]

#Error checking
print(neededData)

#Making a new csv file with only necessary data
neededData.to_csv('CleanData.csv', index=False)