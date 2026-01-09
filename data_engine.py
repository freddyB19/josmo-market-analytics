import pandas as pd
import random
from datetime import datetime, timedelta


def generate_bulk_market_data(days=7):
	brands = {
		'Josmo Kids': ['Walking Shoes', 'Classic Boot', 'School Uniform Shoe'],
		'Disney': ['Mickey Mouse Sneaker', 'Frozen Elsa Boot', 'Princess Glitter Shoe'],
		'Marvel': ['Spider-Man Light-up', 'Avengers Sport Shoe', 'Black Panther Sneaker'],
		'Laura Ashley': ['Floral Party Dress Shoe', 'Mary Jane Classic']
	}
    
	data = []
	today = datetime.now()

	for i in range(days):
		current_date = (today - timedelta(days=i)).strftime("%Y-%m-%d")

		for brand, products in brands.items():
			for product in products:
				base_price = 45.0 if brand == 'Josmo Kids' else 35.0
				official_price = round(base_price + random.uniform(-2, 5), 2)

				retail_price = round(official_price * random.uniform(0.80, 1.15), 2)

				stock_roll = random.random()
				if stock_roll < 0.15:
					stock_status = 'Out of Stock'
				elif stock_roll < 0.30:
					stock_status = 'Low Stock'
				else:
					stock_status = 'In Stock'

				canal = random.choice(['Amazon', 'Walmart', 'Target', 'Zappos'])

				data.append({
					'Fecha': current_date,
					'Marca': brand,
					'Producto': product,
					'Precio Oficial ($)': official_price,
					'Precio Retailer ($)': retail_price,
					'Diferencia (%)': round(retail_price - official_price, 2),
					'Stock': stock_status,
					'Canal': canal
				})

	return pd.DataFrame(data)

df = generate_bulk_market_data(days=7)
df.to_csv('market_data.csv', index=False)
print(f"Se han generado {len(df)} registros históricos en market_data.csv")
