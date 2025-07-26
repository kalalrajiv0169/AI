'''states={
    "Home":["Bus stop"],
    "Bus Stop":["Home","station","college"],
    "Station":["Bus stop"],
}
print("state- Space Representation of the Problem:")
for state in states:
 print(F"{state}--->{states[state]}")'''

# State-space representation of a problem
#Write a program to take a user problem (e.g., travel route) and display state-space representation.

states = {
    "Home": ["Bus Stop"],
    "Bus Stop": ["Home", "Station", "College"],
    "Station": ["Bus Stop"],
}

print("State-Space Representation of the Problem:")
print("------------------------------------------")
for state in states:
    connections = ', '.join(states[state])
    print(f"{state} --> {connections}")
