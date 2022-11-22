united_kingdom = [
  {
    "name": "Scotland",
    "population": 5295000,
    "capital": "Edinburgh"
  },
  {
    "name": "Wales",
    "population": 3063000,
    "capital": "Swansea"
  },
  {
    "name": "England",
    "population": 53010000,
    "capital": "London"
  }
]

# 1. Change the capital of Wales from `"Swansea"` to `"Cardiff"`.
united_kingdom[1]['capital'] = 'Cardiff'
# 2. Create a dictionary for Northern Ireland and add it to the `united_kingdom` list (The capital is Belfast, and the population is 1,811,000).
Northern_ireland = {'name' : 'Northern Ireland', 'population' : '1,811,000', 'capital' : 'belfast'}
# 3. Use a loop to print the names of all the countries in the UK.
for names in united_kingdom:
  print(f'{names["name"]}')
# 4. Use a loop to find the total population of the UK.
total_population = sum(d['population'] for d in united_kingdom)

print(total_population)
print(united_kingdom)