import unittest
from unittest import mock
from unittest.mock import patch, MagicMock, mock_open
import json


from gradescope_utils.autograder_utils.decorators import weight

with mock.patch('builtins.input', return_value="Abuja"):
    from program import *

TEST_API_RESPONSE = b'{\n\t"product" : "astro" ,\n\t"init" : "2023103018" ,\n\t"dataseries" : [\n\t{\n\t\t"timepoint" : 3,\n\t\t"cloudcover" : 2,\n\t\t"seeing" : 4,\n\t\t"transparency" : 2,\n\t\t"lifted_index" : 2,\n\t\t"rh2m" : 6,\n\t\t"wind10m" : {\n\t\t\t"direction" : "NE",\n\t\t\t"speed" : 2\n\t\t},\n\t\t"temp2m" : 27,\n\t\t"prec_type" : "none"\n\t}\n\t]\n}\n'
TEST_WEATHER_DATA_LIST = json.loads(TEST_API_RESPONSE.decode('utf-8'))['dataseries']

class TestProgram(unittest.TestCase):

    mock_response = MagicMock()
    mock_response.getcode.return_value=200
    mock_response.read.return_value = TEST_API_RESPONSE
    mock_response.__enter__.return_value = mock_response

    @weight(4)
    def test_map_city_to_coords(self):
        assert len(map_city_to_coords) > 3, "Didn't add new city to list."

    @weight(3)
    @patch('builtins.print')
    @patch('builtins.input', return_value="Abuja")
    @patch('builtins.open', mock_open())
    @patch('urllib.request.urlopen', return_value=mock_response)
    def test_show_weather_not_read_from_file(self, _, __, ___):
        show_weather()
        assert not open.called, "Attempting to open a file when you shouldn't be"

    @weight(4)
    @patch('builtins.print')
    @patch('builtins.input', return_value="Invalid_City")
    @patch('builtins.open', mock_open())
    @patch('urllib.request.urlopen', return_value=mock_response)
    def test_show_weather_invalid_city(self, _, __, mock_print):
        show_weather()
        response = mock_print.call_args[0][0]
        assert "We do not have coordinates for that city" in response, "Expecting different response for invalid city."

    @weight(4)
    @patch('builtins.print')
    @patch('urllib.request.urlopen', return_value=mock_response)
    def test_show_weather_to_user_temperature(self, _, mock_print):
            show_weather_to_user(TEST_WEATHER_DATA_LIST)
            response = mock_print.call_args[0][0]
            assert "The temperature is" in response, "Temperature not printed in show_weather"

    @weight(3)
    @patch('builtins.print')
    @patch('urllib.request.urlopen', return_value=mock_response)
    def test_show_weather_to_user_wind_approaching(self, _, mock_print):
        show_weather_to_user(TEST_WEATHER_DATA_LIST)
        response = mock_print.call_args[0][0]
        assert "the wind is approaching" in response, "wind information not printed in required format"
    
    @weight(3)
    @patch('builtins.print')
    @patch('urllib.request.urlopen', return_value=mock_response)
    def test_show_weather_to_user_wind_direction(self, _, mock_print):
        show_weather_to_user(TEST_WEATHER_DATA_LIST)
        response = mock_print.call_args[0][0]
        assert "northeast" in response, "wind direction not translated to friendly format (e.g., `northeast`)"

    @weight(3)
    @patch('builtins.print')
    @patch('urllib.request.urlopen', return_value=mock_response)
    def test_show_weather_to_user_wind_speed(self, _, mock_print):
        show_weather_to_user(TEST_WEATHER_DATA_LIST)
        response = mock_print.call_args[0][0]
        assert "light" in response, "wind speed not translated to friendly format based on API documentation (e.g., `0.3-3.4m/s (light)`)"

    @weight(3)
    @patch('urllib.request.urlopen', return_value=mock_response)
    def test_get_api_result_return_type(self, _):
        result = get_api_results("Abuja")
        assert result is not None, "get_api_results returning nothing"
        assert type(result) is list or type(result) is str, "get_api_results doesn't seem to return correct type"

    @weight(3)
    @patch('builtins.open', mock_open())
    @patch('urllib.request.urlopen', return_value=mock_response)
    def test_get_api_result_not_write_file(self, _, ):
        get_api_results("Abuja")
        assert not open.called, "Attempting to open a file when you shouldn't be"


if __name__ == "__main__":
    unittest.main()
