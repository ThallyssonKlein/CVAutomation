from notion.client import NotionClient
from dotenv import load_dotenv
load_dotenv()

from os import getenv
client = NotionClient(token_v2=getenv('TOKEN_V2'),monitor=True,start_monitoring=True,enable_caching=False)

from data import Data
data = Data()

from .monitors.my_description import MyDescriptionMonitor

my_description = MyDescriptionMonitor(data, client)
print("Ready and watching!")

input()
