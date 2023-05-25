from product_handling import ProductHandling
from config import Config
from query import Query
class Product:
        def __init__(self, productList, headers, inserted_coins, coin_pouch) -> None:
                self.productList = productList
                self.inserted_coins = inserted_coins
                self.coin_pouch = coin_pouch
                self.headers =  headers
                print("\nProducts:")
                for i, product in enumerate(self.productList):
                        product_brand = product[2]
                        product_price = product[3]
                        print(f"{i+1} - {product_brand}, {product_price} coin(s)") 
                print("0 - Previous")
        def purchase(self) -> None:
                option = int(input("Select product: "))
                self.product = self.productList[option-1]
                self.product_amount = int(self.product[1])
                self.product_price = int(self.product[3])
                self.product_brand = self.product[2]
                if self.product_amount < 0:
                        print("Product is sold out!")
                else:
                        if self.inserted_coins < self.product_price:
                                print("Not enough coins! Insert more.")
                        else:
                                self.product[1] = self.product_amount - 1 #decreaseAmount
                                self.inserted_coins -= self.product_price
                                print(f"Sihh...\nGlunk Glunk! mm. taste like {self.product_brand}")
                                Config().writeCoins( self.coin_pouch, self.inserted_coins )
                                ProductHandling.writeProduct(self.productList, self.headers)
                                self.product_cost = Query().selectProductCost(self.product_brand)
                                Query().insertTransactions(self.product_brand, self.product_price, self.product_cost)
                return None