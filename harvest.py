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
    #print(musk.pairings)
        
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
    #print(casaba.pairings)

    crenshaw = MelonType(    
        "cren",
        "1996",
        "green",
        False, 
        False,
        "Crenshaw"
    )
    crenshaw.add_pairing("proscuitto")
    #print(crenshaw.pairings)

    yellow_watermelon = MelonType(    
        "yw",
        "2013",
        "yellow",
        False, 
        True,
        "Yellow Watermelon"
    )
    yellow_watermelon.add_pairing("ice cream")
    #print(yellow_watermelon.pairings)

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
        all_melons[key] = {} # nested dictionary with attributes

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

    def __init__(self, code, shape_rating, color_rating, field, harvester): 
        """Initialize a melon."""

        # assign passed-in args as attributes
        self.code = code
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.field = field
        self.harvester = harvester

    def is_sellable(self, shape_rating, color_rating, field):
        return self.shape_rating > 5 and self.color_rating > 5 and self.field != 3

def make_melons(melon_types):
    """Returns a list of Melon objects."""
    melons_by_id = make_melon_type_lookup(melon_types)
    melons = []

    melon_1 = Melon(melons_by_id['yw'], 8, 7, 2, 'Sheila')
    melon_2 = Melon(melons_by_id['yw'], 3, 4, 2, 'Sheila')
    melon_3 = Melon(melons_by_id['yw'], 9, 8, 3, 'Sheila')
    melon_4 = Melon(melons_by_id['cas'], 10, 6, 35, 'Sheila')
    melon_5 = Melon(melons_by_id['cren'], 8, 9, 35, 'Michael')
    melon_6 = Melon(melons_by_id['cren'], 8, 2, 35, 'Michael')
    melon_7 = Melon(melons_by_id['cren'], 2, 3, 4, 'Michael')
    melon_8 = Melon(melons_by_id['musk'], 6, 7, 4, 'Michael')
    melon_9 = Melon(melons_by_id['yw'], 7, 10, 3, 'Michael')

    melons.extend([melon_1, melon_2, melon_3, melon_4, melon_5,
                   melon_6, melon_7, melon_8, melon_9])
        
    

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""
    # Fill in the rest 
    for melon in melons:
            harvester = f'Harvested by {melon.harvester}'
            field_number = f'Field #{melon.field}'
            sell_status = 'CAN BE SOLD' if melon.is_sellable() else 'NOT SELLABLE'
            print(f'{harvester} from {field_number} {sell_status}')


