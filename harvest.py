############
# Part 1   #
############

# 
class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, 
                 name):
        """Initialize a melon."""

        self.pairings = []

        # assign passed-in args as attributes
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name


    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        # overwrites existing attributes using self
        #self.pairings = [pairing] 
        self.pairings.append(pairing) # we missed an s in self.pairing(s) and appended it to list

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        # overwrites existing attributes using self
        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""
    
    # instantiates the class MelonType for each above mleon type
    musk = MelonType(
        "musk",
        1998,
        "green",
        True,
        True,
        "Muskmelon"
    )
    musk.add_pairing("mint")
    print(musk.pairings)
        
    casaba = MelonType(    
        "cas",
        "2003",
        "orange",
        False, 
        False,
        "Casaba"
    )
    casaba.add_pairing("strawberries")
    casaba.pairings.append("mint")    
    
    print(casaba.pairings)

    crenshaw = MelonType(    
        "cren",
        "1996",
        "green",
        False, 
        False,
        "Crenshaw"
    )
    crenshaw.add_pairing("proscuitto")
    print(crenshaw.pairings)

    yellow_watermelon = MelonType(    
        "yw",
        "2013",
        "yellow",
        False, 
        True,
        "Yellow Watermelon"
    )
    yellow_watermelon.add_pairing("ice cream")
    print(yellow_watermelon.pairings)

    all_melon_types = [musk, casaba, crenshaw, yellow_watermelon]

    return all_melon_types

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    for melon in melon_types: 
        print(f'\n{melon.name} pairs with ')
        for pairing in melon.pairings:  # changed from "for pairing in melon.pairings, print melon.pairings"
            print(f'- {pairing}')    

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""
    all_melons = {}
    
    for melon in melon_types:
        key = melon.code    # should this be melon.new_code?????????
        all_melons[key] = {} # nested dict with attributes

        # can this be done in a for loop?
        all_melons[key]['first_harvest'] = melon.first_harvest
        all_melons[key]['color'] = melon.color
        all_melons[key]['is_seedless'] = melon.is_seedless
        all_melons[key]['is_bestseller'] = melon.is_bestseller
        all_melons[key]['name'] = melon.name
    
    # for melon_code, attributes in all_melons.items():
    #     print('\n' + melon_code.upper())
    #     for attribute, value in attributes.items(): 
    #         print(f'{attribute}: {value}')
    
    return all_melons
    

############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods

def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # Fill in the rest

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest 



