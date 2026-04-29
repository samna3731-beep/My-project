import pandas as pd

class Product:
    def __init__(self, prod_id, price):
        self.prod_id = prod_id
        self.price = price

    def apply_discount(self, percent_off):
        self.price = self.price * (1 - percent_off / 100)


df = pd.read_csv("Products.csv")

electronics_df = df[df["Category"] == "Electronics"].copy()

updated_prices = []

for _, row in electronics_df.iterrows():
    product = Product(row["Product_ID"], row["Price"])
    product.apply_discount(20)
    updated_prices.append(product.price)

electronics_df["Price"] = updated_prices

electronics_df["Promo_Active"] = "Yes"

electronics_df.to_csv("holiday_promos.csv", index=False)

print("Holiday promo file created successfully!")