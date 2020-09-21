#!/usr/bin/python

import requests
from hand import *
from collections import Counter

class Deck:
    # Borrow a deck object from deckofcardsapi
    def __init__(self):
        resp = API.get("https://deckofcardsapi.com/api/deck/new/")
        self.deckId = resp['deck_id']
        self.countRemaining = resp['remaining']
    def shuffle(self):
        shuffleURL = 'https://deckofcardsapi.com/api/deck/{}/shuffle/'.format(self.deckId)
        resp = API.get(shuffleURL)
        self.countRemaining = resp['remaining']
    def draw(self, count):
        drawURL = 'https://deckofcardsapi.com/api/deck/{}/draw/?count={}'.format(self.deckId, count)
        resp = API.get(drawURL)
        self.countRemaining = resp['remaining']
        hand = Hand(resp['cards'])
        return hand


class API:
    def __init__(self):
        pass
    def get(url):
        resp = requests.get(url)
        if(resp.status_code != 200):
            raise requests.ConnectionError("GET request unsuccessful. Status Code {}".format(resp.status_code))
        return resp.json()
