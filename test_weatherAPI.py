import pytest

from weatherAPI import weather_data_download

def test1():
  assert weather_data_download((42.3656,71.0096),"us") == True
  assert weather_data_download("London", "us") == True
  assert weather_data_download(65201, "us") == True
