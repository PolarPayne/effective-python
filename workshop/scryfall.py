import json
from collections import namedtuple

_fields = ["name", "mana_cost", "oracle_text", "rarity"]
Card = namedtuple("Card", _fields)  # TODO use a data class?


def search():
    with open("data.json") as fp:
        data = json.load(fp)

    # this data is from https://api.scryfall.com/cards/search?q=c%3Awhite+cmc%3D1
    # the API documentation is at https://scryfall.com/docs/api
    # feel free to use any other data set you might have
    # TODO get data from URL
    # TODO allow defining search parameter
    # TODO get all pages of data (the API is paged)

    for i in data["data"]:
        yield Card(**{k: i.get(k, "") for k in _fields})
