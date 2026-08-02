import csv

prices = []

with open("house_prices.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        prices.append(int(row["Price"]))

average_price = sum(prices) / len(prices)

print("House Price Prediction Project")
print("-" * 30)
print(f"Average House Price: KSh {average_price:,.0f}")
print(f"Highest Price: KSh {max(prices):,}")
print(f"Lowest Price: KSh {min(prices):,}")
