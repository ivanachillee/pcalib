# PCAlib
PCAlib is a micro-library built in Python 3 for fast and easy-to-use Principal Component Analysis (PCA) data transformation. It will help you to reduce high-dimensional data into a N amount of components with a simplified class function.

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
