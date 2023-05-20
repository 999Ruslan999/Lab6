students_languages = {
    "Alice": ["English", "French", "Spanish"],
    "Bob": ["German", "Italian", "English"],
    "Charlie": ["Chinese", "Japanese"],
    "Dave": ["Spanish", "Portuguese"],
    "Eve": ["Chinese", "Korean", "Japanese"]
}


all_languages = set()
for languages in students_languages.values():
    all_languages.update(languages)

print("Всего различных языков:", len(all_languages))
print("Список языков:", sorted(all_languages))


chinese_speakers = []
for name, languages in students_languages.items():
    if "Chinese" in languages:
        chinese_speakers.append(name)

print("Студенты, знающие китайский язык:", chinese_speakers)