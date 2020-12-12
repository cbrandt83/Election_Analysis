voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, {"county": "Denver", "registered_voters":463353}, {"county":"Jefferson", "registered_voters":432438}]
#print all the values in a list of dictionaries
for i in voting_data:
    for new in i.values():
        print(new)
        