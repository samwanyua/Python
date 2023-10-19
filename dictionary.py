#Dictionary

capitals = {'USA':'New YOrk',
            'India':'New Dehli',
            'China': 'Berlin',
            'Russia': 'Moscow'}
capitals.update({'China':'HongKong'})
capitals.update({'Kenya':'Nairobi'})
capitals.pop('China')

print(capitals.keys())
print(capitals.values())
print(capitals.get('Germany'))
print(capitals.items())