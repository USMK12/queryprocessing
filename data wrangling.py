import pandas as pd
data = {'Name': ['Jai', 'Princi', 'Gaurav',
				'Anuj', 'Ravi', 'Natasha', 'Riya'],
		'Age': [17, 17, 18, 17, 18, 17, 17],
		'Gender': ['M', 'F', 'M', 'M', 'M', 'F', 'F'],
		'Marks': [90, 76, 'NaN', 74, 65, 'NaN', 71]}
df = pd.DataFrame(data)
c = avg = 0
for ele in df['Marks']:
	if str(ele).isnumeric():
		c += 1
		avg += ele
avg /= c
df = df.replace(to_replace="NaN",value=avg)
df['Gender'] = df['Gender'].map({'M': 0,'F': 1, }).astype(float)
df = df[df['Marks'] >= 75].copy()
df.drop('Age', axis=1, inplace=True)
df
print(df)
