from app.new_cases_today import get_data

def test_get_data():
    x = get_data()
    assert (len(x) > 0)
