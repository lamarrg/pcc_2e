def city_and_country(city, country, population=''):
    if population == '':
        return f'{city}, {country}'
    else:
        return f'{city}, {country} - population={population}'



