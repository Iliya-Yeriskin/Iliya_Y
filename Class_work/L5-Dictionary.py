#dictionary

my_dict={"www.google.com":"8.8.8.8","www.facebook.com":"7.7.7.7" ,"www.youtube.com":["5.5.5.5","4.4.4.4"]}
print(my_dict)
#update entry in dict
my_dict.update({"www.net4uc.com":"33.33.33.33"})
print(my_dict)
#update entry by adding a dict
my_dict={"www.google.com":"8.8.8.8","www.facebook.com":"7.7.7.7","www.youtube.com":["5.5.5.5","4.4.4.4"]}
my_dict2=({"www.net4uc.com":"33.33.33.33"})
my_dict.update(my_dict2)
print(my_dict)
#len of dict and specific & all values
print("Number of Entries in the dictionary: " + str(len(my_dict)))
print(my_dict["www.google.com"])
print(my_dict.values())
#change a specific entry in dict or add new if enrty is new
my_dict["www.google.com"]="8.8.4.4"
my_dict["www.yahoo"]="2.2.2.2"
print(my_dict["www.google.com"])
print(my_dict)
#check if an entry is in the dict by keys
print("www.google.com" in my_dict)
#check if an entry is in the dict by values
print("8.8.4.4" in my_dict.values())
