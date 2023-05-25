import configparser
import sqlite3
from sqlite3 import Connection
from typing import Union
class Config:
	def __init__(self) -> None:
		self.config = configparser.ConfigParser()
		self.config.read('config.ini')   

	def databaseConnection(self)-> Connection:
		DB_FILEPATH = self.readFilePath()
		DB_CONN: Connection = sqlite3.connect(DB_FILEPATH)
		return DB_CONN

	def readCoinPouch(self) -> int:
		return int(self.config["Coins"]["coin_pouch"])

	def readInsertedCoins(self) -> int:
		return int(self.config["Coins"]["inserted_coins"])

	def writeCoins(self, coin_pouch, inserted_coins) -> None:
		with open('config.ini', 'w') as configfile:
			self.config["Coins"]["coin_pouch"] = str(coin_pouch)
			self.config["Coins"]["inserted_coins"] = str(inserted_coins)
			self.config.write(configfile)
			return None

	def readFilePath(self) -> str:
		return self.config["SQLite"]["filepath"]          

	def readAuthentication(self) -> tuple[str, str]:
		username = self.config["Admin"]["username"] 
		password = self.config["Admin"]["password"]    
		return username, password


