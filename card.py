class CardStatus:
    '''enum for card state'''
    back, front, solved = range(3)
    # _unused, back, front, solved = range(4)

class Card:
    def __init__(self):
        self.status = CardStatus.back

    '''def __init__(self, *args, **kwargs)'''
    
    '''def __init__(self, imageClass()):
        self.isFaceUp = False
        self.image = imageClass()'''

    '''https://www.geeksforgeeks.org/working-images-python/'''

    def display(self):
        '''show card to user'''
        pass

#test code
if __name__ == "__main__":
    newCard = Card()
    print(CardStatus.back)
    print(CardStatus.front)
    print(CardStatus.solved)
