person = {"first_name":"asna","last_name":"shameel","uid":290419,"friends":["abc","cdf"],
          "skills":{
              "backend_skills":["nodejs","ruby"],
              "databases":["redis","mysql","postgres"]
          }}
print(len(person))
print(person.get("skills").get("backend_skills"))

# person["address"]="manjeri"
# print(person.get("address"))
# print("address" in person)
# print(person.pop("address"))
# print("address" in person)
# print(len(person))
# del person["friends"]
# print(len(person))
# print(person["skills"]["backend_skills"])
# person["skills"]["databases"].append("mongodb")
# print(person["skills"]["databases"])

print(person.items())
person_copy = person.copy()
del person
print(person_copy)
keys=person_copy.keys()
for i in keys:
    print(person_copy[i])
    print("\n")