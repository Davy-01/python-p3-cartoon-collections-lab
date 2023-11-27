def roll_call_dwarves(names):
    index=0
    for name in names:
        print(f"{index + 1}. {name}")
        index+=1


def summon_captain_planet(planeteer_calls):
    new_call = [call.capitalize() + "!" for call in planeteer_calls]
    return new_call

def long_planeteer_calls(calls):
    for call in calls:
        if len(call)>4:
            return True
    else:
        return False

def find_the_cheese(food):
    cheese=["cheddar", "gouda", "camembert"]
    for item in food:
        if item in cheese:
            return item
    else:
        return None
        