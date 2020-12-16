voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, {"county": "Denver", "registered_voters":463353}, {"county":"Jefferson", "registered_voters":432438}]
#loop through elements in list of dicts
for element in voting_data:
    print(element)

#isolate the values for Key1 and Key1 in every element and assign them to variables "value_of_Key1" and "value_of_Key2"
    #Notes:
        #for Key1 in element.get("county"):  did't work.
     
        #for key, value in element.items(): didn't work.
        
        #maybe try splicing to isolate each dictionary in each element before trying to isolate each key's value
    

#print message with the values of Key1 and Key1 for every dictionary
    message=(f"{value_of_Key1} county has {value_of_Key2:,} registered voters.")
    print(message)