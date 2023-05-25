# import simpleaudio
import pathlib
from config import Config
from menu import Menu
from product_handling import ProductHandling
from product import Product
class VendorMachine(Menu):
	coin_pouch: int
	inserted_coins: int
	# INSERT_COIN = simpleaudio.WaveObject.from_wave_file(pathlib.Path("./insert_coin.wav").__str__())
	# COIN_LAND = simpleaudio.WaveObject.from_wave_file(pathlib.Path("./coin_land.wav").__str__())
	def __init__(self) -> None:
		super().__init__(options = [
			{"description": "- Insert coin", "action": self.insertCoin },
			{"description": "- View inserted coins", "action": self.viewInsertedCoins},
			{"description": "- View products", "action": self.viewProducts},
			{"description": "- Buy product","action": self.purchaseProducts },
			{"description": "- Return coins","action": self.returnCoins }
		], submenu= True)
		self.configuration =  Config()
		self.inserted_coins = self.configuration.readInsertedCoins()
		self.coin_pouch = self.configuration.readCoinPouch()
		self.productList, self.headers = ProductHandling.readProductList()
	def purchaseProducts(self)-> None:
		purchaseProduct = Product(self.productList, self.headers, self.inserted_coins, self.coin_pouch)
		purchaseProduct.purchase()
		return None     
	def viewInsertedCoins(self) -> None:
		print(f"{self.inserted_coins} coin(s) in vending machine.")        
		return None
	def playSound(self, sound) -> None:
		self.play_obj = sound.play()
		self.play_obj.wait_done()
		return None
	def insertCoin(self) -> None:
		self.coin_pouch -= 1
		self.inserted_coins += 1
		self.configuration.writeCoins( self.coin_pouch, self.inserted_coins )
		self.playSound(self.INSERT_COIN)
		return None
	def returnCoins(self) -> None:
		self.coin_pouch += self.inserted_coins
		self.inserted_coins = 0               
		self.configuration.writeCoins(self.coin_pouch, self.inserted_coins)
		self.playSound(self.COIN_LAND)
		return None
	def viewProducts(self) -> None:
		print("\nProducts in vending machine:")
		# for header in self.headers:
		#    print(f"|{header}", end="")
		print("| opt | qty |     brand     |price|")
		print("|-----|-----|---------------|-----|")
		for product in self.productList:
			print("|"+ "{:<5}".format(product[0]) + "|"+"{:<5}".format(product[1])+ "|"+ "{:<15}".format(product[2]) +"|"+"{:<5}".format(product[3])+"|")