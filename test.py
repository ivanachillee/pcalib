from pcalib import dpca
import pandas as pd

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
df = pd.read_csv(url, names=['sepal length','sepal width','petal length','petal width','target'])

features = ['sepal length', 'sepal width', 'petal length', 'petal width']
label = ['target']

newdf = dpca(df, features, label, 2, ["pc1","pc2"])
newdf = newdf.apply()

print(newdf.head(5))
