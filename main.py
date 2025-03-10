mission_names = ['Apollo 11', 'Challenger', 'Curiosity Rover', 'Viking 1', 'Mars Pathfinder', 'Hubble Telescope', 'Apollo 13']
mission_years = [1969, 1986, 2012, 1975, 1996, 1990, 1970]
mission_success = [True, False, True, True, True, True, False]

for i in mission_names: # loop through list and print the number of missions
    print(mission_names.index(i)+1)

print()  # Blank line for better readability

for i in mission_success: # loop through list and print the number of missions
    if mission_success[i] == True:
        print(mission_success.index(i))

