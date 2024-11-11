from sqlalchemy import create_engine
import pandas as pd

engine = create_engine("sqlite:///mydatabase.db")
data = {
    "column1": [1, 2, 3],
    "column2": ["A", "B", "C"]
}
df = pd.DataFrame(data)
df.to_sql("my_table", engine, if_exists="replace", index=False)
