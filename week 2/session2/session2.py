'''
Problem 1: Most Endangered Species
Imagine you are working on a wildlife conservation database. Write a function named most_endangered()
 that returns the species with the highest conservation priority based on its population.

The function should take in a list of dictionaries named species_list as a parameter. 
Each dictionary represents data associated with a species, including its name, habitat, 
and wild population. The function should return the name of the species with the lowest population.

If there are multiple species with the lowest population, return the species with the lowest index.

'''

def most_endangered(species_list):
    most_endangered_animal = ""
    lowest_population = 1000000

    for species in species_list:
        if species["population"] < lowest_population:
           lowest_population = species["population"]
           most_endangered_animal = species["name"]
    return most_endangered_animal

species_list = [
    {"name": "Amur Leopard",
     "habitat": "Temperate forests",
     "population": 84
    },
    {"name": "Javan Rhino",
     "habitat": "Tropical forests",
     "population": 72
    },
    {"name": "Vaquita",
     "habitat": "Marine",
     "population": 10
    }
]

print(most_endangered(species_list))

# Problem 2
def count_endangered_species(endangered_species, observed_species):
    count_species = 0
    # using for loop, loop through observed_species 
    endangered_species = set(endangered_species)
    for species in observed_species:
       if species in endangered_species:
          count_species+=1
    return count_species
    
endangered_species1 = "aA"
observed_species1 = "aAAbbbb"

endangered_species2 = "z"
observed_species2 = "ZZ"

print(count_endangered_species(endangered_species1, observed_species1)) 
print(count_endangered_species(endangered_species2, observed_species2))  

# Problem 3
def navigate_research_station(station_layout, observations):
  pass
# enumerate()

station_layout1 = "pqrstuvwxyzabcdefghijklmno"
observations1 = "wildlife"

station_layout2 = "abcdefghijklmnopqrstuvwxyz"
observations2 = "cba"

print(navigate_research_station(station_layout1, observations1))  
print(navigate_research_station(station_layout2, observations2))

# Problem 4
def prioritize_observations(observed_species, priority_species):
  pass

observed_species1 = ["🐯", "🦁", "🦌", "🦁", "🐯", "🐘", "🐍", "🦑", "🐻", "🐯", "🐼"]
priority_species1 = ["🐯", "🦌", "🐘", "🦁"]  

observed_species2 = ["bluejay", "sparrow", "cardinal", "robin", "crow"]
priority_species2 = ["cardinal", "sparrow", "bluejay"]

print(prioritize_observations(observed_species1, priority_species1))
print(prioritize_observations(observed_species2, priority_species2)) 

# Problem 5
def distinct_averages(species_populations):
  pass

species_populations1 = [4,1,4,0,3,5]
species_populations2 = [1,100]

print(distinct_averages(species_populations1))
print(distinct_averages(species_populations2)) 

# Problem 6
def max_species_copies(raised_species, target_species):
    pass

raised_species1 = "abcba"
target_species1 = "abc"
print(max_species_copies(raised_species1, target_species1))  # Output: 1

raised_species2 = "aaaaabbbbcc"
target_species2 = "abc"
print(max_species_copies(raised_species2, target_species2)) # Output: 2

# Problem 7
def count_unique_species(ecosystem_data):
    pass

ecosystem_data1 = "f123de34g8hi34"
ecosystem_data2 = "species1234forest234"
ecosystem_data3 = "x1y01z001"

print(count_unique_species(ecosystem_data1))
print(count_unique_species(ecosystem_data2))
print(count_unique_species(ecosystem_data3))

# Problem 8
def num_equiv_species_pairs(species_pairs):
    pass

species_pairs1 = [[1,2],[2,1],[3,4],[5,6]]
species_pairs2 = [[1,2],[1,2],[1,1],[1,2],[2,2]]

print(num_equiv_species_pairs(species_pairs1))
print(num_equiv_species_pairs(species_pairs2))
