import pytest
import os.path
import jsonpickle
from fixture.application import Application
from fixture.orm import ORMFixture

fixture = None
target = None


def load_config(file):
    global target
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(config_file) as f:
            target = jsonpickle.decode(f.read())
    return target


@pytest.fixture  # init fixture one time
def app(request):
    global fixture
    browser = request.config.getoption("--browser")
    web_config = load_config(request.config.getoption("--target"))['web']
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, base_url=web_config['baseUrl'], login=web_config['login'],
                              password=web_config['password'])
    fixture.session.ensure_login(login=web_config['login'], password=web_config['password'])  # check for login logic
    return fixture


@pytest.fixture(scope="session", autouse=True)  # destroy fixture for all session
def stop(request):
    def fin():
        fixture.session.ensure_logout()  # check for logout logic
        fixture.destroy()
    request.addfinalizer(fin)


@pytest.fixture(scope="session")
def db(request):
    db_config = load_config(request.config.getoption("--target"))['db']
    dbfixture = ORMFixture(host=db_config['host'], name=db_config['name'], user=db_config['user'],
                          password=db_config['password'])
    return dbfixture


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--target", action="store", default="target.json")


def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith("json_"):
            test_data = load_from_json(fixture[5:])
            metafunc.parametrize(fixture, test_data, ids=[str(x) for x in test_data])


def load_from_json(file):
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/{0}.json".format(file))) as f:
        return jsonpickle.decode(f.read())
