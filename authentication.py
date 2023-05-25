import sys
from config import Config
class Authentication:
	def __init__(self) -> None:
		self.username, self.password = Config().readAuthentication()
	def authenticate(self) -> bool:     
		if len(sys.argv) > 1:
			input_username = sys.argv[2]
			input_password = sys.argv[4]
			if self.username == input_username and self.password == input_password:
				return True
		else:
			return False