import time
from termcolor import colored
from math import ceil
from data import JOURNEY_IN_DAYS,COST_FOOD_HORSE_COPPER_PER_DAY, COST_FOOD_HUMAN_COPPER_PER_DAY, COST_HORSE_SILVER_PER_DAY, COST_TENT_GOLD_PER_WEEK
##################### O03 #####################

def copper2silver(amount:int) -> float:
    return amount * 0.1

def silver2gold(amount:int) -> float:
    return amount * 0.2

def copper2gold(amount:int) -> float:
    return amount * 0.02

def platinum2gold(amount:int) -> float:
    return amount * 25

def getPersonCashInGold(personCash:dict) -> float:
    total_cash = 0

    total_cash += copper2gold(personCash.get('copper', 0))
    total_cash += silver2gold(personCash.get('silver', 0))
    total_cash += platinum2gold(personCash.get('platinum', 0))
    total_cash += personCash.get('gold', 0)

    return total_cash
    
    
    

##################### O05 #####################

def getJourneyFoodCostsInGold(people:int, horses:int) -> float:
    total_cost_food =copper2gold(people * COST_FOOD_HUMAN_COPPER_PER_DAY + horses *COST_FOOD_HORSE_COPPER_PER_DAY) * JOURNEY_IN_DAYS
    return round(total_cost_food,2)

##################### O06 #####################

def getFromListByKeyIs(list:list, key:str, value:any) -> list:
    friends = []
    for item in list:
        if item.get(key) == value:
            friends.append(item)
    return friends

def getAdventuringPeople(people:list) -> list:
    return getFromListByKeyIs(people, 'adventuring', True)

def getShareWithFriends(friends:list) -> list:
    return getFromListByKeyIs(friends, 'shareWith', True)


def getAdventuringFriends(friends:list) -> list:
    adventuring_friends = []
    adventuring_people = getAdventuringPeople(friends)
    share_with_friends = getShareWithFriends(friends)
    for friend in adventuring_people:
        if friend in share_with_friends:
            adventuring_friends.append(friend)
    return adventuring_friends   
##################### O07 #####################

def getNumberOfHorsesNeeded(people:int) -> int:
    return ceil(people / 2)

def getNumberOfTentsNeeded(people:int) -> int:
    return ceil(people / 3)

def getTotalRentalCost(horses:int, tents:int) -> float:
    total_cost_horses = (horses * COST_HORSE_SILVER_PER_DAY / 5) * JOURNEY_IN_DAYS
    total_cost_tents = (tents * COST_TENT_GOLD_PER_WEEK ) * ceil(JOURNEY_IN_DAYS / 7)
    return total_cost_horses + total_cost_tents


##################### O08 #####################

def getItemsAsText(items:list) -> str:
    items_in_text = []
    for item in items:
        items_in_text.append(f"{item['amount']}{item['unit']} {item['name']}")
    if len(items_in_text) > 1:
        return', '.join(items_in_text[:-1]) +' & '+ items_in_text[-1]
    else:
        return items_in_text[0]

def getItemsValueInGold(items: list) -> float:
    total_value = 0
    for item in items:
        price_amount = item['price']['amount']
        item_amount = item['amount']
        price_type = item['price']['type']
 
        if price_type == 'copper':
            total_value += copper2gold(price_amount) *  item_amount
        elif price_type == 'silver':
            total_value += silver2gold(price_amount) * item_amount
        elif price_type == 'platinum':
            total_value += platinum2gold(price_amount) * float(item_amount)
        else:
            total_value += price_amount * item_amount
    return total_value


##################### O09 #####################

def getCashInGoldFromPeople(people:list) -> float:
    total_cash_in_gold = 0
    for person in people:
        total_cash_in_gold += getPersonCashInGold(person['cash'])
    return total_cash_in_gold

##################### O10 #####################

def getInterestingInvestors(investors:list) -> list:
    interessante_investors = []
    for investor in investors:
        if investor['profitReturn'] < 11:
            interessante_investors.append(investor)
    return interessante_investors

def getAdventuringInvestors(investors:list) -> list:
    interessante_investors = getInterestingInvestors(investors)
    adventuring_investors = []
    for investor in interessante_investors:
        if investor['adventuring']:
            adventuring_investors.append(investor)
    return adventuring_investors

def getTotalInvestorsCosts(investors: list, adventurerGear: list) -> float:
    total_cost_investors = 0
    for investor in investors:
        if investor['adventuring']:
            for currency, amount in investor['cash'].items():
                if currency == 'gold':
                    total_cost_investors += amount
                elif currency == 'silver':
                    total_cost_investors += amount * 0.1  # Converteer naar gold
                elif currency == 'copper':
                    total_cost_investors += amount * 0.01  # Converteer naar gold
                elif currency == 'platinum':
                    total_cost_investors += amount * 10  # Converteer naar gold
    return round(total_cost_investors, 2)


##################### O11 #####################

def getMaxAmountOfNightsInInn(leftoverGold:float, people:int, horses:int) -> int:
    pass

def getJourneyInnCostsInGold(nightsInInn:int, people:int, horses:int) -> float:
    pass

##################### O13 #####################

def getInvestorsCuts(profitGold:float, investors:list) -> list:
    pass

def getAdventurerCut(profitGold:float, investorsCuts:list, fellowship:int) -> float:
    pass

##################### O14 #####################

def getEarnigs(profitGold:float, mainCharacter:dict, friends:list, investors:list) -> list:
    pass

##################### view functions #####################

def print_colorvars(txt:str='{}', vars:list=[], color:str='yellow') -> None:
    vars = map(lambda string, color=color: colored(str(string), color, attrs=['bold']) ,vars)
    print(txt.format(*vars))

def print_title(name:str) -> None:
    print_colorvars(vars=['=== [ {} ] ==='.format(name)], color='green')

def print_chapter(number:int, name:str) -> None:
    nextStep(2)
    print_colorvars(vars=['- CHAPTER {}: {} -'.format(number, name)], color='magenta')

def nextStep(secwait:int=1) -> None:
    print('')
    time.sleep(secwait)

def ifOne(amount:int, yes:str, no:str, single='een') -> str:
    text = yes if amount == 1 else no
    amount = single if amount == 1 else amount
    return '{} {}'.format(amount, text).lstrip()