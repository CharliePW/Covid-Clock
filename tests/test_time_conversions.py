from app.time_conversions import minutes_to_seconds
from app.time_conversions import hours_to_minutes
from app.time_conversions import hhmm_to_seconds
from app.time_conversions import hhmmss_to_seconds
from app.time_conversions import current_time_hhmm

def test_minutes_to_seconds():
    assert (minutes_to_seconds("33") == 1980)

def test_hours_to_minutes():
    assert (hours_to_minutes("15") == 900)

def test_hhmm_to_seconds():
    assert (hhmm_to_seconds("12:35") == 45300)

def test_hhmmss_to_seconds():
    assert (hhmmss_to_seconds("12:35:12") == 45312)

def test_current_time_hhmm():
    assert (current_time_hhmm() == "10:21")
