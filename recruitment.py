

skills = ["Eating", "Sleeping", "Netflix", "Excell", "Lifting"]
cv = {}
cv ["name"] = input("What's your name? ")
cv ["age"] = int(input("How old are you? "))
cv ["experience"] = int(input("How many years of experience do you have? "))
cv ["skills"] = []

counter = 0
for skill in skills:
    print("%d. %s" %(counter+1, skill) )
    counter+=1

pick = input("Pick a skill: ")
if pick.isdigit():
    cv["skills"].append(skills[int(pick)-1])

print(cv)

pick = input("Pick another skill: ")
if pick.isdigit():
    cv["skills"].append(skills[int(pick)-1])

print(cv)

if cv["age"] < 30 and cv["experience"] >  3 and "Lifting" in cv["skills"] :
    print("Accepted")
    
else: 
    print("rejected")

    