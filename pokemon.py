"""
    This is the pokemon file with pokemon and move class.
    It defines the two objects with their various methods to extract and calculate data.
"""

from random import randint


#DO NOT CHANGE THIS!!!
# =============================================================================
is_effective_dictionary = {'bug': {'dark', 'grass', 'psychic'},
                           'dark': {'ghost', 'psychic'},
                           'dragon': {'dragon'},
                           'electric': {'water', 'flying'},
                           'fairy': {'dark', 'dragon', 'fighting'},
                           'fighting': {'dark', 'ice', 'normal', 'rock', 'steel'},
                           'fire': {'bug', 'grass', 'ice', 'steel'},
                           'flying': {'bug', 'fighting', 'grass'},
                           'ghost': {'ghost', 'psychic'},
                           'grass': {'water', 'ground', 'rock'},
                           'ground': {'electric', 'fire', 'poison', 'rock', 'steel'},
                           'ice': {'dragon', 'flying', 'grass', 'ground'},
                           'normal': set(),
                           'poison': {'fairy', 'grass'},
                           'psychic': {'fighting', 'poison'},
                           'rock': {'bug', 'fire', 'flying', 'ice'},
                           'steel': {'fairy', 'ice', 'rock'},
                           'water': {'fire', 'ground', 'rock'}
                           }

not_effective_dictionary = {'bug': {'fairy', 'flying', 'fighting', 'fire', 'ghost','poison','steel'},
                            'dragon': {'steel'},
                            'dark': {'dark', 'fairy', 'fighting'},
                            'electric': {'dragon', 'electric', 'grass'},
                            'fairy': {'fire', 'poison', 'steel'},
                            'fighting': {'bug', 'fairy', 'flying', 'poison', 'psychic'},
                            'fire': {'dragon', 'fire', 'rock', 'water'},
                            'flying': {'electric', 'rock', 'steel'},
                            'ghost': {'dark'},
                            'grass': {'bug', 'dragon', 'grass', 'fire', 'flying', 'poison', 'steel'},
                            'ground': {'bug','grass'},
                            'ice': {'fire', 'ice', 'steel', 'water'},
                            'normal': {'rock', 'steel'},
                            'poison': {'ghost', 'ground', 'poison', 'rock'},
                            'psychic': {'psychic', 'steel'},
                            'rock': {'fighting', 'ground', 'steel'},
                            'steel': {'electric', 'fire', 'steel', 'water'},
                            'water': {'dragon','grass', 'ice'}
                            }

no_effect_dictionary = {'electric': {'ground'},
                        'dragon': {'fairy'},
                        'fighting': {'ghost'},
                        'ghost': {'normal', 'psychic'},
                        'ground': {'flying'},
                        'normal': {'ghost'},
                        'poison': {'steel'},
                        'psychic': {'dark'},

                        'bug': set(), 'dark': set(), 'fairy': set(),'fire': set(),
                        'flying': set(), 'grass': set(), 'ice': set(),
                        'rock': set(), 'steel': set(), 'water': set()
                        }

#Dictionaries that determine element advantages and disadvantages
# =============================================================================

class Move(object):
    def __init__(self, name = "", element = "normal", power = 20, accuracy = 80,
                 attack_type = 2):
        """ Initialize attributes of the Move object """

        self.name = name
        self.element = element
        self.power = power
        self.accuracy = accuracy
        self.attack_type = attack_type                                         #attack_type is 1, 2 or 3
        # 1 - status moves, 2 - physical attacks, 3 - special attacks

    def __str__(self):

        '''
            Returns name of the move for printing
        '''
        return ('{}').format(self.name)


    def __repr__(self):
        '''
            Returns __str__ method
        '''
        return self.__str__()

    def get_name(self):
        '''
            Returns name of the move
        '''
        return self.name

    def get_element(self):
        '''
            Returns the element of the move
        '''
        return self.element

    def get_power(self):
        '''
            Returns the power of the move
        '''
        return self.power

    def get_accuracy(self):
        '''
            Returns the accuracy of the move
        '''
        return self.accuracy

    def get_attack_type(self):
        '''
            Returns attack type of the move
        '''
        return self.attack_type

    def __eq__(self,m):
        '''return True if all attributes are equal; False otherwise'''
        return self.name == m.get_name() and self.element == m.get_element() and\
                self.power == m.get_power() and self.accuracy == m.get_accuracy() and\
                self.attack_type == m.get_attack_type()


class Pokemon(object):
    def __init__(self, name = "", element1 = "normal", element2 = "", moves = None,
                 hp = 100, patt = 10, pdef = 10, satt = 10, sdef = 10):
        ''' initializes attributes of the Pokemon object '''

        self.name = name
        self.element1 = element1
        self.element2 = element2

        self.hp = hp
        self.patt = patt
        self.pdef = pdef
        self.satt = satt
        self.sdef = sdef

        self.moves = moves

        try:
            if len(moves) > 4:
                self.moves = moves[:4]

        except TypeError: #For Nonetype
            self.moves = list()

    def __eq__(self,p):
        '''return True if all attributes are equal; False otherwise'''
        return self.name == p.name and \
            self.element1 == p.element1 and \
            self.element2 == p.element2 and \
            self.hp == p.hp and \
            self.patt == p.patt and \
            self.pdef == p.pdef and \
            self.satt == p.satt and \
            self.sdef == p.sdef and \
            self.moves == p.moves

    def __str__(self):
        '''
            Returns pokemon with data for printing
        '''
        # create formatted string for printing data
        a = str(('{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}\n{:<15}{:<15}\n').format(self.name,self.hp,self.patt,self.pdef,self.satt,self.sdef,self.element1,self.element2))
        x = ''
        for m in self.moves:                                                   # add move name to string
            x += ("{:<15}".format(m.get_name()))
        r = a + x                                                              # concatenate strings and return
        return r

    def __repr__(self):
        '''
            Return __str__ method
        '''
        return self.__str__()

    def get_name(self):
        '''
            Returns name of the pokemon
        '''
        return self.name

    def get_element1(self):
        '''
            Returns element 1
        '''
        return self.element1

    def get_element2(self):
        '''
            Returns element 2
        '''
        return self.element2

    def get_hp(self):
        '''
            Returns hp
        '''
        return self.hp

    def get_patt(self):
        '''
            Returns patt attribute
        '''
        return self.patt

    def get_pdef(self):
        '''
            Returns pdef attribute
        '''
        return self.pdef

    def get_satt(self):
        '''
            Returns satt attribute
        '''
        return self.satt

    def get_sdef(self):
        '''
            Returns sdef attribute
        '''
        return self.sdef

    def get_moves(self):
        '''
            Returns the pokemon's moves
        '''
        return self.moves

    def get_number_moves(self):
        '''
            Returns the number of moves
        '''
        return len(self.moves)

    def choose(self,index):
        '''
            Returns selected move
        '''
        try:
            return (self.moves[index])
        except:
            return None


    def show_move_elements(self):
        '''
            Returns move elements
        '''
        for i in self.moves:
            print('{:<}'.format(i.get_element()))

    def show_move_power(self):
        '''
            Returns move power
        '''
        for i in self.moves:
            print('{:<}'.format(i.get_power()))

    def show_move_accuracy(self):
        '''
            Returns move accuracy
        '''
        for i in self.moves:
            print('{:<}'.format(i.get_accuracy()))

    def add_move(self, move):
        '''
            Adds moves to pokemon
        '''
        if len(self.moves)<=3:
            self.moves.append(move)

    def subtract_hp(self, damage):
        '''
            Subtracts damage from hp.
        '''
        self.hp = self.hp - damage                                             # subtract damage from hp
        if self.hp < 0:                                                        # if hp is becomes negative, set it to 0.
            self.hp = 0

    def attack(self, move, opponent):
        '''
            Attack method: Checks for attack type and validity.
            Creates and modifies a modifier value based on the move's and  opponent's
            element. It also shows if the move was effective or not.
        '''
        mp = move.get_power()
        move_type = move.get_attack_type()
        x = 0
        if move_type == 2:
            A = self.get_patt()
            D = opponent.get_pdef()
            x = 1
        elif move_type == 3:
            A = self.get_satt()
            D = opponent.get_sdef()
            x = 1
        else:
            print('Invalid attack_type, turn skipped.')                        # skip turn for invalid attack_type
        while x == 1:                                                          # create random integer for accuracy
            r_accuracy = randint(0,100)
            accuracy = move.get_accuracy()
            if r_accuracy>accuracy:                                            # compare random int to move accuracy, if random is bigger, move missed
                print('Move missed!')
                break
            modifier = 1.0                                                     # create modifier
            opp_el1 = opponent.get_element1()                                  # extract data
            opp_el2 = opponent.get_element2()
            att_el1 = self.get_element1()
            att_el2 = self.get_element1()
            move_el = move.get_element()

# compares player and opponent elements, and changes modifier according to the data
# given in the dictionaries
            if opp_el1 in is_effective_dictionary[move_el]:
                modifier *= 2
            elif opp_el1 in not_effective_dictionary[move_el]:
                modifier *= 0.5
            elif opp_el1 in no_effect_dictionary[move_el]:
                modifier = 0

            if opp_el2 in is_effective_dictionary[move_el]:
                modifier *= 2
            elif opp_el2 in not_effective_dictionary[move_el]:
                modifier *= 0.5
            elif opp_el2 in no_effect_dictionary[move_el]:
                modifier = 0

# Print special messages according to the effectiveness of the move
            if modifier == 0:
                print("No effect!")
            elif modifier > 1:
                print("It's super effective!!!!")
            elif modifier < 1:
                print("Not very effective...")

            if move_el == att_el1 or move_el == att_el2:                       # if move element matches player element, increase modifier
                modifier*=1.5

            damage = int(((mp*A*20)/(D*50) + 2)*modifier)                      # calculate damage
            opponent.subtract_hp(damage)                                       # subtract hp
            x = 2
