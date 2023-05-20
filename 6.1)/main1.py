countries = {"Россия": "Москва", "Франция": "Париж", "Германия": "Берлин", "Италия": "Рим", "Япония": "Токио"}

# a)
for country, capital in countries.items():
    print(country, "-", capital)

# b)
print("Столица России:", countries["Россия"])

# c)
sorted_countries = sorted(countries.keys())
print("Список стран в алфавитном порядке:")
for country in sorted_countries:
    print(country, "-", countries[country])