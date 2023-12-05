import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

#reading file
df = pd.read_csv(r"\python\cancer_deathRate.csv")
column_names = list(df.columns)

#cleaning data by dropping the duplicates
df = df.drop_duplicates()

#Counties Meeting Objective

#cleaning data
df = df[df['Met Objective of 45.5? (1)'] != "*"]
counts = df['Met Objective of 45.5? (1)'].value_counts()


plt.pie(counts, labels=counts.index, autopct='%1.1f%%', startangle=90)

# Equal aspect ratio ensures that pie is drawn as a circle
plt.axis('equal')  
plt.title('Distribution of Met Objective of 45.5 Column')
plt.show()

#Analyze Age-Adjusted Death Rates:
# cleaning data
df = df[df['Age-Adjusted Death Rate'] != "*"]
df['County'] = df['County'].astype('category')


#converting it to json format for visualisation
json_data = df[['County', 'Age-Adjusted Death Rate']].to_json(orient='records')

# Average Deaths per Year
# df['Average Deaths per Year']
# df.rename(columns={'Average Deaths per Year': 'AvgDeath'}, inplace=True)
# Plotting
plt.figure(figsize=(10, 6))
plt.xticks(rotation=45, ha='right')
sns.lineplot(data=df, x='Age-Adjusted Death Rate', y='County', marker='o', label='Cancer')
plt.title('Average Deaths per Year - Cancer')
plt.ylabel('Country')
plt.xlabel('Average Deaths')
plt.legend()
plt.show()


# Interactive plot with hover
fig = px.line(df, x='County', y='Average Deaths per Year', labels={'County': 'Average Deaths per Year'},
              title='Average Deaths per Year - Cancer', markers=True, line_shape='linear')

fig.update_layout(hovermode='x')

# Show the plot
fig.show()