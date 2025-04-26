import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import warnings

warnings.filterwarnings('ignore')

df = pd.read_csv('data/cars.csv')

print(df.head())

print(df.shape)

print(df.info())

print(df.describe())

print(df.nunique())

df.dropna(subset=list(df.columns), inplace=True)

df["Brand"].unique()

# Price distribution
plt.figure(figsize=(10, 6))
sns.histplot(df['Price'], kde=True, color='skyblue', bins=30)
plt.title('Distribution of Car Prices \n', fontweight="bold")
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.savefig("charts/price_distribution.png")
plt.close()


# car features_heatmap
plt.figure(figsize=(8, 6))
int_columns = df.select_dtypes(include='int').columns
corr = df[int_columns.drop('Car_ID')].corr()
sns.heatmap(corr, annot=True, cmap="YlGnBu", linewidths=0.5)
plt.title("Correlation Between Car Features and Price", fontweight="bold")
plt.tight_layout()
plt.savefig("charts/heatmap_correlation.png")
plt.close()


# Year_Price
plt.figure(figsize=(10, 6))
sns.boxplot(x='Year', y='Price', data=df)
plt.title("Price vs. Year \n", fontweight="bold")
plt.xticks(rotation=45)
plt.xlabel('Year')
plt.ylabel('Price')
plt.savefig("charts/price_year_boxplot.png")
plt.close()

plt.figure(figsize=(10, 6))
avg_price_year = df.groupby("Year")["Price"].mean().reset_index()
sns.lineplot(x="Year", y="Price", data=avg_price_year)
plt.title("Average Car Price Over Time \n", fontweight="bold")
plt.xlabel("Year")
plt.ylabel("Average Price")
plt.tight_layout()
plt.savefig("charts/price_year_lineplot.png")
plt.close()


# Power_Price
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Power', y='Price', data=df)
plt.title('Price vs. Power \n', fontweight="bold")
plt.xlabel('Power (bhp)')
plt.ylabel('Price')
plt.savefig("charts/power_price.png")
plt.close()


# Brands distribution
plt.figure(figsize=(10, 6))
brands = df["Brand"].value_counts()
sns.barplot(x=brands.values, y=brands.index, palette="Blues_d")
plt.title("Brands by Number of cars \n", fontweight='bold')
plt.xlabel("Number of cars")
plt.ylabel("Brand")
plt.savefig("charts/brands_by_number.png")
plt.close()


# Relationship Between Transmission Type, Kilometers Driven, and Car Price
sns.scatterplot(data = df, x="Kilometers_Driven", y="Price" ,hue='Transmission', style = "Transmission")
plt.title("Transmission Type, Kilometers Driven, and Price \n", fontweight="bold")
plt.tight_layout()
plt.savefig("charts/transmission_kmdriven_price.png")
plt.close()


# Average Mileage by Number of Seats and Transmission Type
plt.figure(figsize=(10, 6))
sns.catplot(
    data=df, x="Seats", y="Mileage", col="Transmission",
    kind="bar", height=4, aspect=.6,
)
plt.tight_layout()
plt.savefig("charts/seats_mileage_transmission.png")
plt.close()


# Car Price Distribution by Owner Type
plt.figure(figsize=(10, 6))
sns.displot(data=df, x="Price", hue="Owner_Type", kind="kde")
plt.title("Car Price Distribution by Owner Type \n", fontweight="bold")
plt.tight_layout()
plt.savefig("charts/price_ownerType.png")
plt.close()


# Bubble chart: engine size vs. price vs. fuel type ---
fig = px.scatter(
    df,
    x="Engine",
    y="Price",
    size="Power",
    color="Fuel_Type",
    hover_data=["Brand", "Model"],
    title="Engine Size vs Price vs Fuel Type"
)

fig.update_layout(
    title={
        'text': "Engine Size vs Price vs Fuel Type",
        'x': 0.5,
        'xanchor': 'center',
        'font': {
            'family': 'Arial Black',   # Use a bold font family
            'size': 20,
            'color': 'black'
        }
    }
)
fig.write_html("charts/bubble_chart.html")