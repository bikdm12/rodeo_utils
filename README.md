# rodeo_utils
python 2.7 package for parsing [RODEO2](https://github.com/the-mitchell-lab/rodeo2) output
## Installation
`pip install rodeo-utils`
## Requirements
* biopython
## Usage
```python
import rodeo_utils

rod_dir = 'output/' # Directory with RODEO output
bgcs = rodeo_utils.rodeo_output_iterator(rod_dir)

queries = [x.query for x in bgcs]
```
Please refer to [the online documentation](https://rodeo-utils.readthedocs.io) for more information
