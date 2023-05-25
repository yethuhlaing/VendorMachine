from config import Config
class Query:
	@staticmethod
	def insertTransactions(commodity_brand: str, price: int, cost: int):
		transaction = (commodity_brand, price, cost)
		DB_CONN = Config().databaseConnection()
		cursor = DB_CONN.cursor()
		sql_statement = "INSERT INTO sale(commodity_brand, price, cost) VALUES (?,?,?)"
		cursor.execute(sql_statement, transaction)
		DB_CONN.commit()
		cursor.close()
	# def insertTransactions(table_name: str, column_names: tuple, sql_params: tuple) -> None:
	# 	# ...
	# 	sql_statement = f"INSERT INTO {table_name}({','.join(column_names)}) VALUES ({','.join(['?']*len(sql_params))})"
	# 	# print(sql_statement)
	# 	return None
	# insertTransactions("sale", ("brand", "price", "cost",), ("cola", "2", "1",))
	@staticmethod
	def selectTransactions():
		DB_CONN = Config().databaseConnection()
		cursor = DB_CONN.cursor()
		sql_statement = "SELECT price, cost FROM sale"
		cursor.execute(sql_statement)
		result = cursor.fetchall()
		DB_CONN.commit()
		cursor.close()
		return result
        
	@staticmethod
	def selectProductCost(product_name):
		DB_CONN = Config().databaseConnection()
		cursor = DB_CONN.cursor()
		sql_statement = "SELECT cost FROM commodity WHERE brand = ?"
		cursor.execute(sql_statement, (product_name,))
		result = cursor.fetchall()[0]
		product_cost = result[0]
		DB_CONN.commit()
		cursor.close()
		return product_cost