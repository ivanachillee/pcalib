
#PCAlib by Ivan Achille.
#external packages needed: sklearn, pandas

from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import pandas as pd

class dpca():
    def __init__(self, dataset, features, label, components, comp_col_names):
        """
        ENTRY VARIABLES

        dataset: pandas df var
        features: array of features of df.     i.e: ["a","b","c"]
        label: label column of df       i.e: ["d"]
        components: n of final principal components
        comp_col_names: array of new columns name of the final principal components     i.e: ["p1","p2"]

        Function returns new dataset with final principal components and label column.
        """
        self.dataset = dataset
        self.features = features
        self.label = label
        self.components = components
        self.comp_col_names = comp_col_names

        #Gather values from entered features
        self.x = self.dataset.loc[:, self.features].values

        #Gather values from entered label (Y)
        self.y = self.dataset.loc[:,self.label].values

    def apply(self):
        
        #Standarize the feature data
        ft = StandardScaler().fit_transform(self.x)

        pca = PCA(n_components=self.components)

        pComponents = pca.fit_transform(ft)
        pDf = pd.DataFrame(data = pComponents
             , columns = [self.comp_col_names])

        pca_dataset = pd.concat([pDf, self.dataset[self.label]], axis = 1)

        return pca_dataset #returns pca transformed dataset
