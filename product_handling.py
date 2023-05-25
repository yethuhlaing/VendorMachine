import csv
class ProductHandling:

	@staticmethod                
	def readProductList() -> list:
		products: list = []
		with open('products.csv', 'r') as file:
			reader = csv.reader(file)
			headers = next(reader)
			for row in reader:                      
				products.append(row)
		return products, headers 
	     
	@staticmethod 
	def writeProduct(rows, header) -> None:
		rows: list[str]
		with open('products.csv', 'w', newline='') as file:
			writer = csv.writer(file)
			writer.writerow(header)
			for row in rows:
				writer.writerow(row)
		return None