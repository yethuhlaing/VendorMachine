from menu import Menu
import configparser
from menu_vendorMachine import VendorMachine
class MenuMain(Menu): 
	coin_pouch: int
	inserted_coins: int
	def __init__(self) -> None:
		super().__init__(options=[
			{"description": "- View coins in pouch", "action": self.viewPouch },
			{"description": "- Go to vending machine", "action": self.toVendorMachine}
		])
		return None

	def viewPouch(self) -> None:
		self.config = configparser.ConfigParser()
		self.config.read('config.ini')     
		self.coin_pouch = self.config["Coins"]["coin_pouch"]
		self.inserted_coins = self.config["Coins"]["inserted_coins"]
		print(f"{self.coin_pouch} coins in pouch.")
		return None
	def toVendorMachine(self)-> None:
		VendorMachine().start()
		return None
                



