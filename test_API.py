import API
import pytest


@pytest.mark.parametrize(
    'pURL, pName, pId, pCountry, pLatitude, pLongitude',
    [
        ('https://samples.openweathermap.org/data/2.5/weather?q=London,uk&appid=b6907d289e10d714a6e88b30761fae22',
         'London', 2643743, 'MX', 51.51, -0.13)
    ])
def test_API(pURL, pName, pId, pCountry, pLatitude, pLongitude):
    data = API.getData(pURL)
    assert data['name'] == pName
    assert data['id'] == pId
    assert data['sys']['country'] == pCountry
    assert data['coord']['lat'] == pLatitude
    assert data['coord']['lon'] == pLongitude
