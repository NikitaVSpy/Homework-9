from game import Card_game

game = Card_game()
game.creation_deck_player()
game.creation_deck_comp()
game.trump_card()
game.disunion_trump_card()
game.disunion_deck_player()
game.disunion_deck_comp()
print(game.information())

game.step_player()
game.checkout_card()
game.step_comp()
game.sort_card()
game.taking_cards()



