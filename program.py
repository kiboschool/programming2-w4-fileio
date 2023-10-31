import json
import urllib.request 

map_city_to_coords = {
    'Abuja': 'lat=9.0764785&lon=7.398574',
    'Nairobi': 'lat=-1.2920659&lon=36.8219462',
    'Accra': "lat=5.6037168&lon=-0.1869644",
    'Seattle': 'lat=47.6061&long=122.3328'
}

map_abbreviation_to_direction = {
    'S': 'south',
    'SW': 'southwest',
    'SE': 'southeast',
    'N': 'north',
    'NW': 'northwest',
    'NE': 'northeast',
    'W': 'west',
    'E': 'east'
}

map_wind10m_to_speed = {
    1: 'Below 0.3m/s (calm)',
    2: '0.3-3.4m/s (light)',
    3: '3.4-8.0m/s (moderate)',
    4: '8.0-10.8m/s (fresh)',
    5: '10.8-17.2m/s (strong)',
    6: '17.2-24.5m/s (gale)',
    7: '24.5-32.6m/s (storm)',
    8: 'Over 32.6m/s (hurricane)'
}

def show_weather_to_user(weather_data_list):
    for weather_data in weather_data_list:
        hour_number = weather_data['timepoint']
        temperature = weather_data['temp2m']

        wind_direction = weather_data['wind10m']['direction']
        wind_direction = map_abbreviation_to_direction[wind_direction]
        wind_speed = weather_data['wind10m']['speed']
        wind_speed = map_wind10m_to_speed[wind_speed]

        print(f'On hour {hour_number},')
        if hour_number == 24:
            print('(in one day)')
        elif hour_number == 48:
            print('(in two days)')
        elif hour_number == 72:
            print('(in three days)')

        print(f'The temperature is {temperature} and the wind is approaching at {wind_speed} from the {wind_direction}')

def show_weather():
    city_name = input('Please type a city: ')
    if city_name not in map_city_to_coords:
        print('We do not have coordinates for that city.')
    else:
        weather_data_list = get_api_results(city_name)        
        show_weather_to_user(weather_data_list)

def get_api_results(city):
    coords = map_city_to_coords[city]
    url = ('https://www.7timer.info/bin/astro.php?' + 
        f'{coords}&ac=0&unit=metric&output=json')
    results = urllib.request.urlopen(url)
    json_content = results.read().decode('utf-8')
    return json.loads(json_content)['dataseries']

show_weather()