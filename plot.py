import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data1=['M','F','F','M','F','M']
data2=['Neel','Khushi','Tupu','Yug','Esha','Nilesh']
data3=[20,18,38,11,11,40]
data4=['Mumbai','Mumbai','Dubai','Dubai','London','Dubai']
data5=[90,92,80,85,90,95]
df=pd.DataFrame(data1,columns=['Sex'])
df['Name']=data2
df['Age']=data3
df['Place']=data4
df['Percentage']=data5
a=np.asarray(df.Age)
b=np.asarray(df.Percentage)
c=np.asarray(df.Place)
#after=sns.scatterplot(a,b)
#after=sns.countplot(b)
#after=sns.displot(b,rug=True)
final=sns.boxplot(b,c)
plt.show()

