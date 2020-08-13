import random


class Card_game:
    '''''
    Обозначения карт: A - туз K - король; Q - дама; J - валет; 10; 9; 8; 7; 6;
    '''''

    def __init__(self):
        self.deck = ['A-пики', 'A-крести', 'A-червы', 'A-буби', 'K-пики', 'K-крести', 'K-червы', 'K-буби', 'Q-пики',
                     'Q-крести', 'Q-червы', 'Q-буби', 'J-пики', 'J-крести', 'J-червы', 'J-буби', '10-пики', '10-крести',
                     '10-червы', '10-буби', '9-пики', '9-крести', '9-червы', '9-буби', '8-пики', '8-крести', '8-червы',
                     '8-буби', '7-пики', '7-крести', '7-червы', '7-буби', '6-пики', '6-крести', '6-червы', '6-буби']

    @staticmethod
    def ranked_card(x):
        color = ['6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        value = 6
        for i in color:
            if x == i:
                return value
            value += 1

    def creation_deck_player(self):
        """Колода игрока
        Формирование колоды
        """
        self.deck_cards_player = []

        while len(self.deck_cards_player) < 6:
            i = random.choice(self.deck)
            self.deck_cards_player.append(i)
            self.deck.remove(i)

        return self.deck_cards_player

    def creation_deck_comp(self):
        """Колода компьютера
        Формирование колоды
        """
        self.deck_cards_comp = []

        while len(self.deck_cards_comp) < 6:
            i = random.choice(self.deck)
            self.deck_cards_comp.append(i)
            self.deck.remove(i)

        return self.deck_cards_comp

    def trump_card(self):
        """Козырная карта
        """
        self.trump_card = random.choice(self.deck)
        self.deck.remove(self.trump_card)
        print('Козырная карта:', self.trump_card)
        return self.trump_card

    def disunion_trump_card(self):
        """Разделение козырной карты
        Разделение на достоинство и масть
        """
        self.disunion_trump = self.trump_card.split('-')
        return self.disunion_trump

    def disunion_deck_player(self):
        """Разделение карт в колоде игрока
        Разделение на достоинство и масть
        """
        self.disunion_deck_player = []
        for i in self.deck_cards_player:
            disunion = i.split('-')
            self.disunion_deck_player.append(disunion)
        return self.disunion_deck_player

    def disunion_deck_comp(self):
        """Разделение карт в колоде компьютера
        Разделение на достоинство и масть
        """
        self.disunion_deck_comp = []
        for i in self.deck_cards_comp:
            disunion = i.split('-')
            self.disunion_deck_comp.append(disunion)
        return self.disunion_deck_comp

    @staticmethod
    def information():
        str = ''
        str += 'Раздача карт завершена\n'
        str += 'Выбор карты происходит по порядковому номеру карты в Вашей колоде, начиная с "0"\n'
        return str

    def step_player(self):
        """Ход игрока
        """
        self.cards_on_table = []

        print('Введите номер карты не больше:', len(self.disunion_deck_player) - 1, '\n')

        print('Ваша колода:', self.disunion_deck_player)
        index = int(input('Ваш ход. Выберите карту: '))
        self.cards_1 = self.disunion_deck_player[index]
        self.disunion_deck_player.remove(self.cards_1)
        self.cards_on_table.append(self.cards_1)

    def checkout_card(self):
        """Проверка возможности положить ещё карту
        Функция проверяет, существует ли карта с
        с достоинством как у выбранной для хода карты,
        и предлагает положить её и при положительном
        результате
        """
        mark_exit = False
        while mark_exit == False:
            for i in self.disunion_deck_player[:]:
                if self.cards_1[0] in i[0]:
                    answer = input('Положим ещё одну карту? (да/нет) ')
                    if answer == 'да':
                        print('Оставшиеся карты:', self.disunion_deck_player[:])
                        index = int(input('Выберите карту: '))
                        cards_next = self.disunion_deck_player[index]

                        while cards_next[0] not in self.cards_1[0]:
                            print('Выбрать нужно карту того же достоинства:')
                            index = int(input('Выберите карту ещё раз: '))
                            cards_next = self.disunion_deck_player[index]

                        self.disunion_deck_player.remove(cards_next)
                        self.cards_on_table.append(cards_next)

                        for k in self.disunion_deck_player:
                            if self.cards_1[0] not in k[0]:
                                mark_exit = True

                    elif answer == 'нет':
                        mark_exit = True
                        break
                else:
                    mark_exit = True

        print('Карты на столе:', self.cards_on_table, '\n')
        return self.cards_on_table

    def step_comp(self):
        """Ход компьютера
        Функция учитывает козырное старшинство,
        проверяет сходство мастей карт на столе
        и в колоде компьютера, сравнивает их
        достоинство. Если комьютер не смог покрыть
        карты, то происходит переход к функции
        забора карт со стола.
        """
        self.cards_placed = []  # список положенных компьютером карт
        self.step = 'comp'

        for i in self.cards_on_table:
            self.put_card = False  # метка для определения: компьютер НЕ покрыл карту - берет карты со стола
            flag_1 = 0  # метка для работы с козырными мастями стола
            mark_exit = False  # метка для определения: компьютер покрыл карту - выход из вложенного цикла

            if i[1] == self.disunion_trump[1]:
                card_table = Card_game.ranked_card(i[0])
                card_table += 1000
                flag_1 += 1
            else:
                card_table = Card_game.ranked_card(i[0])

            for k in self.disunion_deck_comp:
                flag_2 = 0  # метка для работы с козырными мастями компьютера
                if mark_exit == False:
                    if k[1] == self.disunion_trump[1]:
                        card_comp = Card_game.ranked_card(k[0])
                        card_comp += 1000
                        flag_2 += 1
                    else:
                        card_comp = Card_game.ranked_card(k[0])
                    #  Компьютер кладет карту если достоинство его карты больше И совпадают масти
                    if card_comp > card_table and i[1] == k[1]:
                        mark_exit = True
                        self.put_card = True
                        print('Компьютер покрывает Вашу карту {} картой {}'.format(i, k))
                        self.disunion_deck_comp.remove(k)
                        self.cards_placed.append(k)
                        continue
                    #  Компьютер НЕ кладет карту если козырная карта только на столе
                    elif flag_1 == 1 and flag_2 == 0:
                        continue
                    #  Компьютер кладет карту если козырная карта только у него в колоде
                    elif flag_1 == 0 and flag_2 == 1:
                        mark_exit = True
                        self.put_card = True
                        print('Компьютер покрывает Вашу карту {} картой {}'.format(i, k))
                        self.disunion_deck_comp.remove(k)
                        self.cards_placed.append(k)
                        continue
                    #  Компьютер кладет карту если козырная карта его колоды больше козырной карты на столе
                    elif flag_1 == 1 and flag_2 == 1 and card_comp > card_table:
                        mark_exit = True
                        self.put_card = True
                        flag = 0
                        print('Компьютер покрывает Вашу карту {} картой {}'.format(i, k))
                        self.disunion_deck_comp.remove(k)
                        self.cards_placed.append(k)
                        continue

                if k == self.disunion_deck_comp[-1] and mark_exit == False and len(self.cards_placed) != len(
                        self.cards_on_table):
                    self.step = 'player'
                    break

    def sort_card(self):
        """Сортировка карт
        Функция сортирует карты: если
        комьютер не смог покрыть карты
        со стола, то он их забирает;
        если покрыл - удаляются карты со
        стола и карты из колоды компьютера,
        положенные им
        """

        if self.put_card == True:
            print('Компьютер покрыл все Ваши карты')
            self.cards_on_table.clear()
        else:
            print('Компьютер не смог покрыть все Ваши карты')
            self.disunion_deck_comp += self.cards_on_table
            self.disunion_deck_comp += self.cards_placed
            self.cards_on_table.clear()

    def taking_cards(self):
        """Функция добора карт"""
        while len(self.deck_cards_player) < 6:
            i = random.choice(self.deck)
            disunion = i.split('-')
            self.disunion_deck_player.append(disunion)
            self.deck.remove(i)

        while len(self.disunion_deck_comp) < 6:
            i = random.choice(self.deck)
            disunion = i.split('-')
            self.disunion_deck_comp.append(disunion)
            self.deck.remove(i)
