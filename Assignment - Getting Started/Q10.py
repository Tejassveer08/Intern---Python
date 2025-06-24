population = 80000

# Men = 52% of population
men = 0.52 * population
women = population - men

# Literate = 48%, Literate men = 35%
literate = 0.48 * population
literate_men = 0.35 * population
illiterate_men = men - literate_men
literate_women = literate - literate_men
illiterate_women = women - literate_women

print("Illiterate Men:", int(illiterate_men))
print("Illiterate Women:", int(illiterate_women))
