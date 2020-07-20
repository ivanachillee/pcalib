# PCAlib
PCAlib is a standarized library built in Python 3 for fast and easy-to-use Principal Component Analysis (PCA) data transformation. It will help you to reduce high-dimensional data into a N amount of components.

Given a collection of points in two, three, or higher dimensional space, a "best fitting" line can be defined as one that minimizes the average squared distance from a point to the line. The next best-fitting line can be similarly chosen from directions perpendicular to the first. Repeating this process yields an orthogonal basis in which different individual dimensions of the data are uncorrelated. These basis vectors are called principal components, and several related procedures principal component analysis (PCA). ([Wikipedia](https://en.wikipedia.org/wiki/Principal_component_analysis))

## Requirements
You will need the following packages to run PCAlib:
<br>
<br><b>- sklearn</b><br>
<b>- pandas</b>

## Usage
PCAlib works with Pandas dataframes, to use it you just have to import the library and create a dpca object to apply the transformations.<br>

```python
from pcalib import dpca
newdf = dpca(df, features, label, 2, ["pc1","pc2"])
newdf = newdf.apply()
```
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[Apache-2.0](https://opensource.org/licenses/Apache-2.0)
