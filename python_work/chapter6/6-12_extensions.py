# We’re now working with examples that are complex enough that they can be extended in any number of ways. Use one of the example pro- grams from this chapter, and extend it by adding new keys and values, chang- ing the context of the program or improving the formatting of the output.

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
    'teddy': ['drupal']
}

for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")
