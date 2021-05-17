from mymodule.helper_functions import Helper
import numpy as np
import pandas as pd

def test_helper_is_null():
    df = pd.DataFrame(np.random.randint(0, 10, size=(10, 2)), columns=list('AB'))
    y = Helper(df)
    x = y.null_count()
    assert(type(x) == np.int64)









