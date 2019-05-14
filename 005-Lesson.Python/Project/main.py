import pandas as pd


def set_printing_options():
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', 200)


set_printing_options()
conversions_df = pd.read_csv("DataSet_1.csv")
conversions_df["last name"].fillna("", inplace=True)
conversions_df.at[8, "gender"] = "F"
conversions_df.at[14, "gender"] = "M"
conversions_df.at[29, "gender"] = "F"
conversions_df.at[37, "gender"] = "M"

for z in range(len(conversions_df)):
    if conversions_df.at[z, "seen count"] > 1e9:
        conversions_df.at[z, "seen count"] = 0
conversions_df.insert(conversions_df.columns.get_loc("last name"), "full name", None)
for z in range(len(conversions_df)):
    conversions_df.at[z, "full name"] = (conversions_df.at[z, "first name"] +
                                         " " + conversions_df.at[z, "last name"]).strip()
conversions_df.drop(columns=["first name", "last name"], inplace=True)

conversions_df.insert(conversions_df.columns.get_loc("month of birth"), "birth day", None)
for z in range(len(conversions_df)):
    conversions_df.at[z, "birth day"] = pd.Timestamp(day=conversions_df.at[z, "day of birth"],
                                                     month=conversions_df.at[z, "month of birth"],
                                                     year=conversions_df.at[z, "year of birth"])
conversions_df.drop(columns=["day of birth", "month of birth", "year of birth"], inplace=True)
conversions_df.insert(conversions_df.columns.get_loc("color scheme"), "age", None)
for z in range(len(conversions_df)):
    conversions_df.at[z, "age"] = (pd.Timestamp.now() - conversions_df.at[z, "birth day"]).days // 365
conversions_df.drop(columns=["birth day"], inplace=True)
print(conversions_df)
