"""
    This is a pokemon battle game.
    All necessary functions like read files, turn, add moves are defined
    The main function runs the game, it asks 2 players to choose their pokemons
    and then runs the game turn by turn, where each player has four moves.
    It stops if one player's pokemon faints or the player quits.
"""
import csv
import copy
from random import randint
from random import seed
from copy import deepcopy
from pokemon import Pokemon
from pokemon import Move

seed(1)                                                                        #Set the seed so that the same events always happen


#DO NOT CHANGE THIS!!!
# =============================================================================
element_id_list = [None, "normal", "fighting", "flying", "poison", "ground", "rock",
                   "bug", "ghost", "steel", "fire", "water", "grass", "electric",
                   "psychic", "ice", "dragon", "dark", "fairy"]

#Element list to work specifically with the moves.csv file.
#   The element column from the moves.csv files gives the elements as integers.
#   This list returns the actual element when given an index
# =============================================================================


def read_file_moves(fp):
    '''
        This function reads the moves.csv file and extracts all moves with their
        data, adds them to a list and returns it.
    '''
    reader = csv.reader(fp)                                                    # initiate reader
    next(reader, None)
    lst = []
    for line in reader:                                                        # for every line
        name = line[1]
        try:
            element = element_id_list[int(line[3])]                            # sets element
        except:
            element = None
        attack_type = int(line[9])                                             # extracts attack type

        if attack_type!=1 and line[2]=='1' and line[4]!='' and line[6]!='' and element!=None: # if valid, add to list and return it
            lst.append(Move(name, element, int(line[4]), int(line[6]), attack_type))
    return lst

def read_file_pokemon(fp):
    '''
        This function reads the pokemon.csv file and extracts all pokemons with
        their data, adds them to a list and returns it.
    '''
    reader = csv.reader(fp)                                                    # initiate reader
    next(reader, None)
    lst = []                                                                   # initiate empty lists
    ID_lst = []
    for line in reader:                                                        # for every line
        if line[0] not in ID_lst:                                              # extracts all elements
            name = line[1].lower()
            element1 = line[2].lower()
            element2 = line[3].lower()
            hp = int(line[5])
            patt = int(line[6])
            pdef = int(line[7])
            satt = int(line[8])
            sdef = int(line[9])
            if line[11] == '1':                                                # if valid, add to list and return it
                lst.append(Pokemon(name, element1, element2, None, hp, patt, pdef, satt, sdef))
                ID_lst.append(line[0])
    return lst

def choose_pokemon(choice,pokemon_list):
    '''
        This functions takes a choice int or string and tries to return the pokemon
        with that index or name, if failed it returns None
    '''
    if choice.isdigit():                                                       # if choice is a number
        choice = int(choice)-1
        try:
            return copy.deepcopy(pokemon_list[choice])                         # return pokemon for that index
        except:
            return None
    else:
        for index, i in enumerate(pokemon_list):                               # if its a string, find that pokemon and return it
            if i.get_name()==choice:
                return copy.deepcopy(pokemon_list[index])
        return None

def add_moves(pokemon, moves_list):
    '''
        This functions generates random integers and adds moves to a pokemon indexed
        at that integer in the moves list. It adds four moves in total and checks
        for matching elements for the last three moves.
        It stops once it has added four moves.
    '''
    pokemon.add_move(moves_list[randint(0, len(moves_list)-1)])                # adds one random move to the pokemon
    for i in range(200):                                                       # loop 200 times
        for x in range(3):                                                     # generate random integers
            r = moves_list[randint(0, len(moves_list)-1)]
            if r.get_element() == pokemon.get_element1() or r.get_element()==pokemon.get_element2():    # if elements match, add to moves
                if r not in pokemon.get_moves():
                    pokemon.add_move(r)
            if len(pokemon.get_moves())==4:                                    # if 4 moves successfully added, break
                return True
    return False

def turn (player_num, player_pokemon, opponent_pokemon):
    '''
        This function executes a player's turn. It first prints the pokemon and its
        moves and then prompts for an input. If it is valid then it does the necessary
        command. It prints damage and hp after the move.
    '''
    if player_num == 1:                                                        # sets player numbers
        opp_num = 2
    else:
        opp_num = 1
    print("Player {}'s turn".format(player_num))
    print(player_pokemon)
    while 1:                                                                   # create loop
        print("Show options: 'show ele', 'show pow', 'show acc'")
        choice = input("Select an attack between 1 and 4 or show option or 'q': ")      # prompt for input
        if choice == 'q':
            print("Player {} quits, Player {} has won the pokemon battle!".format(player_num, opp_num)) # return false if player quits
            return False
        elif choice.isdigit():
            choice = int(choice)
            m = player_pokemon.get_moves()[choice-1]                           # show selected move
            print('selected move:', m)
            print("\n{} hp before:{}".format(opponent_pokemon.get_name(), opponent_pokemon.get_hp()))       # print hp before move
            player_pokemon.attack(m, opponent_pokemon)                         # execute attack
            print("{} hp after:{}".format(opponent_pokemon.get_name(), opponent_pokemon.get_hp()))          # printy hp after move
            print()
            if opponent_pokemon.get_hp()==0:                                   # if hp = 0, print message and end battle
                print("Player {}'s pokemon fainted, Player {} has won the pokemon battle!".format(opp_num, player_num))
                return False
            else:
                if player_num == 2:
                    print('Player 1 hp after: {}'.format(opponent_pokemon.get_hp()))
                    print('Player 2 hp after: {}'.format(player_pokemon.get_hp()))
                    print()
                return True
        else:                                                                  # shows stats as demanded by user
            if choice[-3:] == 'ele':
                print("{:<15}{:<15}{:<15}{:<15}".format(player_pokemon.get_moves()[0].get_element(),player_pokemon.get_moves()[1].get_element(),player_pokemon.get_moves()[2].get_element(),player_pokemon.get_moves()[3].get_element()))
            elif choice[-3:] == 'pow':
                print("{:<15}{:<15}{:<15}{:<15}".format(player_pokemon.get_moves()[0].get_power(),player_pokemon.get_moves()[1].get_power(),player_pokemon.get_moves()[2].get_power(),player_pokemon.get_moves()[3].get_power()))
            elif choice[-3:] == 'acc':
                print("{:<15}{:<15}{:<15}{:<15}".format(player_pokemon.get_moves()[0].get_accuracy(),player_pokemon.get_moves()[1].get_accuracy(),player_pokemon.get_moves()[2].get_accuracy(),player_pokemon.get_moves()[3].get_accuracy()))

def main():
    '''
        This function is the main function. It calls all other functions to run the game.
    '''
    fp1 = open('moves.csv', 'r', encoding = 'utf-8')                           # open and read files
    fp2 = open('pokemon.csv', 'r', encoding = 'utf-8')

    m_list = read_file_moves(fp1)                                              # create lists
    poke_list = read_file_pokemon(fp2)

    usr_inp = input("Would you like to have a pokemon battle? ").lower()       # prompt for input
    while usr_inp != 'n' and usr_inp != 'q' and usr_inp != 'y':                # loop if choice is invalid
        usr_inp = input("Invalid option! Please enter a valid choice: Y/y, N/n or Q/q: ").lower()

    if usr_inp != 'y':                                                         # end if user quits
        print("Well that's a shame, goodbye")
        return

    else:

# Loop: Both users are prompted to select their pokemons, if invalid, keep looping till valid
# Create pokemons, add moves to them and print them
        while 1:
            poke1 = None
            poke2 = None
            while poke1 == None:
                poke1 = input("Player 1, choose a pokemon by name or index: ").lower()
                poke1 = choose_pokemon(poke1, poke_list)
                if type(poke1) == Pokemon:
                    print("pokemon1:")
                    print(poke1)
                    add_moves(poke1, m_list)
                    break

            while poke2 == None:
                poke2 = input("Player 2, choose a pokemon by name or index: ").lower()
                poke2 = choose_pokemon(poke2, poke_list)
                if type(poke2) == Pokemon:
                    print("pokemon2:")
                    print(poke2)
                    add_moves(poke2, m_list)
                    break

            p = 1                                                              # create flag
            while p == 1:
                y = turn(1, poke1, poke2)                                      # execute turn for player 1
                if y == False:
                    usr_inp = input("Battle over, would you like to have another? ").lower()        # reprompt for another battle
                    while usr_inp != 'n' and usr_inp != 'q' and usr_inp != 'y':
                        usr_inp = input("Invalid option! Please enter a valid choice: Y/y, N/n or Q/q: ").lower()       # loop for valid input

                    if usr_inp != 'y':
                        print("Well that's a shame, goodbye")                  # end if user quits
                        return
                    p = 0
                else:
                    t = turn(2, poke2, poke1)                                  # execute turn for player 2
                    if t == False:
                        usr_inp = input("Battle over, would you like to have another? ").lower()        # reprompt for another battle
                        while usr_inp != 'n' and usr_inp != 'q' and usr_inp != 'y':
                            usr_inp = input("Invalid option! Please enter a valid choice: Y/y, N/n or Q/q: ").lower()       # loop for valid input

                        if usr_inp != 'y':
                            print("Well that's a shame, goodbye")              # end if user quits
                            return
                        p = 0

if __name__ == "__main__":
    main()
# End of program
