import random

values = [
    'Cub Scout Motto',
    'Trustworthy',
    'Loyal',
    'Helpful',
    'Friendly',
    'Courteous',
    'Obedient',
    'Thrifty',
    'Brave',
    'Clean',
    'To do my duty to God and my country',
    'The Scout Law',
    'mentally awake, and morally straight',
    'other people at all times',
    'Cub scout sign',
    'Cub scout handshake',
    'Cub scout salute',
    'Webelos',
    'First Aid Kit',
    'Flashlight',
    'Filled Water Bottle',
    'Trail Food',
    'Sun Protection',
    'Whistle',
]

num_cards = 10
cards = []

for i in range(0, num_cards):
    card = []
    temp_values = [] + values
    for j in range(0, 5):
        card.append([])
        for k in range(0, 5):
            if j == 2 and k == 2:
                card[j].append("Free")
            else:
                index = random.randint(0, temp_values.__len__()-1)
                card[j].append(temp_values[index])
                del temp_values[index]
    cards.append(card)
    print "######"
    for r in card:
        print r
    print "######"
