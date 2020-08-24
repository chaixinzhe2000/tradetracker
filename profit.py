import pandas as pd
from interface_with_excel import get_df

def profit():
    df = get_df()
    profit = df["REALIZED_PROFIT"].sum()
    print("\n--------------------------------------------------------------------")
    print(f"Your total realized profit for all past trades is {profit} dollars.")
    print("--------------------------------------------------------------------")