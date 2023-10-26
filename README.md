# Weather API Exercise

## Setup

Click Open Project here to get a copy of the code. Just like the videos, we will be adding to the weather API example! You should aim to complete all the following exercises:

<a href="https://classroom.github.com/a/PCUb7tFJ" target="_blank"><img src="https://img.shields.io/static/v1?label=Open%20Project&message=Weather%20API%20Exercise&color=blue" alt="weather-api-exercise" /></a>

<!-- link to https://github.com/kibo-programming-2-jan-23/show-weather-from-api-exercise -->

## Weather API Part 1

Add a new city. You can usually find the coordinates for a city on the wikipedia page for a city, then look on the panel on the right side for "coordinates".

Once you have the coordinates, format them the same way that the existing entries are written. Note that "S" or "south" is negative and "N" or "north" is positive. Add the new city to the list in `map_city_to_coords` and try it.

## Weather API Part 2

Add a feature to the program, so that it shows the wind direction alongside the temperature. Show the wind direction in a descriptive way, for example display "From the southwest" instead of "SW" and "From the north" instead of "N".

Hint: open the `api_output.json` file and look for wind. Remember that a dictionary can contain other dictionaries. It's sometimes easier to get the data in two steps.

## Weather API Part 3

Currently the program saves the json information to a file, and then reads the information back in from the file. This is unnecessary - isn't there a way to get the information without needing to save to a file first? Modify the program so that it doesn't save to a file.

Hints:

- Right now the `get_api_results` function does not need to return anything, but you can change it so that it will `return` a value at the end.
- The data type returned by the `decode()` method is a string.
- And remember that there is a function `json.loads()` that loads from a string instead of a file.

