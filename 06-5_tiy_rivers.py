rivers = {
    'nile': 'egypt',
    'ohio': 'united states',
    'amazon': 'south america',
}

for name, place in rivers.items():
    print(f"The {name.title()} runs through {place.title()}.")

for name in rivers.keys():
    print(name.title())

for place in rivers.values():
    print(place.title())