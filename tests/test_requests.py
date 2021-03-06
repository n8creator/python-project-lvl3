import pytest
import requests
import os


@pytest.mark.parametrize('fixture', [
    ('ru-hexlet-io-professions.html'),
    ])
def test_requests(requests_mock, fixture):

    # Generate Paths to Fixtures Files
    args_path = 'tests/fixtures/'
    data_file = os.path.join(args_path, fixture)

    # Load data from fixture file into variable
    with open(data_file, 'r') as f:
        data = f.read()

    requests_mock.get('https://ru.hexlet.io/professions', text=data)
    assert data == requests.get('https://ru.hexlet.io/professions').text
