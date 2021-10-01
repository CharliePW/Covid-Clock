from tests.new_weather_update import get_weather

def test_get_weather_cod():
    weather_dict = get_weather()
    assert(weather_dict["cod"] == 200)

def test_get_weather():
    weather_dict = get_weather()
    weather = weather_dict["weather"]
    assert(len(weather) > 0)
