# import pytest
from left_join import join

@pytest.fixture
city_population = {
    "New York City" : 8550405,
    "Los Angeles" : 3971883,
    "Toronto" : 2731571,
    "Chicago" : 2720546,
    "Houston" : 2296224,
    "Montreal" : 1704694,
    "Calgary" : 1239220,
    "Vancouver" : 631486,
    "Boston" : 667137,
    "Bellevue" : 273983,
    "Seattle" : 8292211111,
}

@pytest.fixture
city_walkability_score = {
    "New York City" : 88,
    "Los Angeles" : 44,
    "Toronto" : 82,
    "Chicago" : 78,
    "Houston" : 4,
    "Montreal" : 99,
    "Calgary" : 33,
    "Vancouver" : 93,
    "Boston" : 21,
    "Vancouver" : 95,
    "Auburn" : 0,
}

