import pytest
from routes import NewCar, db, app


@pytest.fixture(scope='module')
def new_car():
    new_car = NewCar(autoName="Renault", autoModel="Logan",
                     engine="1.3", passengers="7")
    return new_car


@pytest.fixture(scope='module')
def test_client():
    # Flask provides a way to test your application by exposing the Werkzeug test Client
    # and handling the context locals for you.
    testing_client = app.test_client()

    # Establish an application context before running the tests.
    ctx = app.app_context()
    ctx.push()

    yield testing_client  # this is where the testing happens!

    ctx.pop()

"""
@pytest.fixture(scope='module')
def init_database():
    # Create the database and the database table
    db.create_all()

    # Insert user data
    new_car1 = NewCar(autoName="Mercedes", autoModel="S500", engine="2.1", passengers="5")
    db.session.add(new_car1)
    db.session.commit()

    yield db  # this is where the testing happens!

    db.drop_all()
"""