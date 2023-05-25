from pathlib import Path
from config import Config
from menu_main import MenuMain
from query import Query
# FILE_PATH_COIN_FLIP = Path("coin_flip.wav")
from authentication import Authentication
class Main:
	def __init__(self) -> None:
		self.initializeDB()
		print("Program starting.")
		if Authentication().authenticate():
			self.summarizeSales()
		else:
			main_menu = MenuMain()
			main_menu.start()
		print("\nProgram ending.")
	def initializeDB(self) -> None:
		with open("init.sql", 'r', encoding="UTF-8") as file_handle:
			DB_CONN = Config().databaseConnection()
			cursor = DB_CONN.cursor()
			sql_script = file_handle.read()
			cursor.executescript(sql_script)
			DB_CONN.commit()
		return None
	def summarizeSales(self)-> None:
		self.transactions = Query.selectTransactions()
		self.overall_price = 0
		self.overall_cost = 0
		for self.transaction in self.transactions:
			self.price = int(self.transaction[0])
			self.overall_price += self.price
			self.cost = int(self.transaction[1])
			self.overall_cost += self.cost
		self.overall_profit = self.overall_price - self.overall_cost
		print(f"Money collected: {str(self.overall_price)}\nOperating costs: {str(self.overall_cost)}\nProfit: {str(self.overall_profit)}")

# Money collected: 6
# Operating costs: 4
# Profit: 2
                
                

# Money collected: 6
# Operating costs: 4
# Profit: 2       
if __name__ == "__main__":
	app = Main()
