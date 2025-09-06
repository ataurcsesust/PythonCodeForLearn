customers ={
    "name":"Ataur",
    "age":23,
    "is_varified":True
}

for key ,value in customers.items():
     print(key,value)
for val in customers.values():
    print(val)                 # only values
for key in customers.keys():
    print(key)                 # only keys

print(customers.keys())
print(customers.values())
print(customers.items())

print(customers["name"])
print(customers.get("name"))
print(customers.get("id"))
print(customers.get("id",101))
del customers["name"]    # delete specific key
print(customers)
customers["age"]=21      # update existing key
customers["university"]="sust"  #add new key
print(customers)
verr = customers.pop("university")     # remove key, returns value
print(verr)
customers.popitem()      # remove last inserted key-value


d = {"a": 1, "b": 2}
print("a" in d)       # True
print("z" not in d)   # True