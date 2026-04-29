import pandas as pd

class Ingredient:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def use_item(self, amount):
        self.quantity -= amount


df = pd.read_csv("Shop.csv")

df = df.rename(columns={"Qty_kg": "Current_Quantity"})

df["Current_Quantity"] = df["Current_Quantity"].astype(float)

coffee_row = df[df["Ingredient"] == "Coffee Beans"].iloc[0]

ingredient_obj = Ingredient(coffee_row["Ingredient"], coffee_row["Current_Quantity"])

ingredient_obj.use_item(2.5)

df.loc[df["Ingredient"] == "Coffee Beans", "Current_Quantity"] = ingredient_obj.quantity

df.to_csv("Shop.csv", index=False)

print("Evening stock report created successfully!")