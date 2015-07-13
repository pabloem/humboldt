from DataManager import DataManager
import json

conf = json.load(open('config.json','r'))

dm = DataManager(conf)

dm.getData()
