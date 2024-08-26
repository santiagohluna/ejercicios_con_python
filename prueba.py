import pandas as pd
import pathlib as pl

files = [f for f in pathlib.Path().glob("out/*.out")]
