#the list of dicts
voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, {"county": "Denver", "registered_voters":463353}, {"county":"Jefferson", "registered_voters":432438}]

#iterate through list of dictionaries
# for dicts in voting_data:
#     print(f"{dicts['county']} county has {dicts['registered_voters']:,} registered voters.")
#get values 1 & 2 in list of dicts
for value1 in voting_data:
    value_of_Key1 = value1['county']
    print(value_of_Key1)
for value2 in voting_data:
    value_of_Key2 = value2['registered_voters']
     
#print message with the values of Key1 and Key1 for every dictionary
    message=(f"{value_of_Key1} county has {value_of_Key2:,} registered voters.")
    print(message)