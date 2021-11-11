import pandas as pd

if pd.__version__ != "1.3.1":
    print(f"You didn't load the version! It should be 1.3.1; you loaded {pd.__version__}")
else:
    print(f"Good job! You loaded version {pd.__version__}")
