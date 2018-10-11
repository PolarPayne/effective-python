from collections import defaultdict, Counter

from .scryfall import search


if __name__ == "__main__":
    grouped = defaultdict(list)
    for i in search():
        # saves typing of
        # if i.rarity not in grouped:
        #     grouped[i.rarity] = []
        grouped[i.rarity].append(i)

    print("RARES")
    for rare in grouped["rare"]:
        print(rare)

    print()

    # with defauldict this would
    # counted = defaultdict(int)
    # for i in data:
    #     counted[i.rarity] += 1
    counted = Counter(i.rarity for i in search())
    for k, v in counted.items():
        print(f"there are {v} {k} card(s)")
