# https://youtu.be/4rmBOxn0PdI?si=r9awpxU9MbBgHsUi
import json
from pprint import pprint

with open('catalog.json', "r") as file:
    catalog = json.load(file)

# pprint(catalog["products"], width=40)
# print("")
#
# for x in range(2):
#     print(catalog["products"][x]["name"])
#     print(catalog["products"][x]["price"])
#     print(catalog["products"][x]["stock"])
#     print("")

# for product in catalog["products"]:
#     print(product)

# for product in catalog["products"]:
#     print(product.get("sale_price")) # or use the normal way like product["sale_price"] but it has to be consistent across fields so put null there if absent value. .get() does it automatically, useful for json without a consistent structure

catalog["products"][0].get("sizes").append("extra_large")

with open("catalog.json", "w") as file:
    json.dump(catalog, file, indent=2)