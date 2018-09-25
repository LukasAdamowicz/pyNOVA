# pyNOVA

Python library for calculating Analysis of Variance statistics.

## Use

```Python
import pyNOVA
```
or
```Python
from pyNOVA import RM_ANOVA
```

Currently the only implemented variation is the repeated measures ANOVA (`RM_ANOVA`).

### Repeated Measures ANOVA

Calculates the _F-statistic_, _p-value_, and &eta;<sup>2</sup><sub>partial</sub> with the specified sphericity correction 
(_Greenhouse-Geissler_, _Huynh-Feldt_, the average of the two, or none).  Will also display a table of statistics.

![Repeated Meaures Display Output](https://github.com/LukasAdamowicz/pyNOVA/blob/master/output_table.PNG "Repeated Meaures Display Output")
