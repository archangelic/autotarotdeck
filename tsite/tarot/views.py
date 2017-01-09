from collections import OrderedDict
from django.shortcuts import render

card_names = [
    'the fool',
    'the magician',
    'the high priestess',
    'the empress',
    'the emperor',
    'the hierophant',
    'the lovers',
    'the chariot',
    'strength',
    'the hermit',
    'wheel of fortune',
    'justice',
    'the hanged man',
    'death',
    'temperance',
    'the devil',
    'the tower',
    'the star',
    'the moon',
    'the sun',
    'judgement',
    'the world',
    'one of wands',
    'two of wands',
    'three of wands',
    'four of wands',
    'five of wands',
    'six of wands',
    'seven of wands',
    'eight of wands',
    'nine of wands',
    'ten of wands',
    'page of wands',
    'queen of wands',
    'king of wands',
    'one of swords',
    'two of swords',
    'three of swords',
    'four of swords',
    'five of swords',
    'six of swords',
    'seven of swords',
    'eight of swords',
    'nine of swords',
    'ten of swords',
    'page of swords',
    'queen of swords',
    'king of swords',
    'one of pentacles',
    'two of pentacles',
    'three of pentacles',
    'four of pentacles',
    'five of pentacles',
    'six of pentacles',
    'seven of pentacles',
    'eight of pentacles',
    'nine of pentacles',
    'ten of pentacles',
    'page of pentacles',
    'queen of pentacles',
    'king of pentacles',
    'one of cups',
    'two of cups',
    'three of cups',
    'four of cups',
    'five of cups',
    'six of cups',
    'seven of cups',
    'eight of cups',
    'nine of cups',
    'ten of cups',
    'page of cups',
    'queen of cups',
    'king of cups'
]

# Create your views here.
def home(request):
    cards = OrderedDict()
    for name in card_names:
        cards[name] = 'no card found'
    print(cards)
    return render(request, 'tarot/home.html', {'cards': cards})

