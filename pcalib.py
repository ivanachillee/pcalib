
#PCAlib by Ivan Achille.
#external packages needed: sklearn
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler



class dpca():
    def __init__(self, dataset, features, label, components, comp_col_names):
        """
        ENTRY VARIABLES
        
        dataset: pandas df var
        features: array of features of df.     i.e: ["a","b","c"]
        label: label column of df       i.e: ["d"]
        components: n of final principal components
        comp_col_names: array of new columns name of the final principal components     i.e: ["p1","p2"]

        function returns new dataset with final principal components and label column.
        """
        super(pca, self).__init__()
        self.dataset = dataset
        self.features = features
        self.label = label

        #Gather values from entered features
        x = dataset.loc[:, features].values

        #Gather values from entered label (Y)
        y = dataset.loc[:,[label]].values

        #Standarize the feature data
        x = StandardScaler().fit_transform(x)

        pca = PCA(n_components=components)

        pComponents = pca.fit_transform(x)
        pDf = pd.DataFrame(data = pComponents
             , columns = [comp_col_names])

        fDf = pd.concat([pDf, dataset[[label]]], axis = 1)
