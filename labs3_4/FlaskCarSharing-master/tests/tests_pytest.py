def test_new_car(new_car):
    assert new_car.autoName == "Renault"
    assert new_car.autoModel == "Logan"
    assert new_car.engine == "1.3"
    assert new_car.passengers == "7"


def test_car_id(new_car):
    new_car.id = 17
    assert isinstance(new_car.get_id(), str)
    assert not isinstance(new_car.get_id(), int)
    assert new_car.get_id() == "17"


def test_main_page(test_client):
    response = test_client.get('/')
    assert response.status_code == 200
    assert b"Car Sharing Service" in response.data
    assert b"Welcome to the Car Sharing Page! Choose your level: " in response.data


def test_user_page(test_client):
    response = test_client.get('/user')
    assert response.status_code == 200
    assert b"User Page" in response.data


def test_admin_page(test_client):
    response = test_client.get('/admin')
    assert response.status_code == 200
    assert b"Admin Page" in response.data


def test_booking_page(test_client):
    response = test_client.get('/booking')
    assert response.status_code == 200
    assert b"Booking" in response.data


def test_showlist_page(test_client):
    response = test_client.get('/showList')
    assert response.status_code == 200
    assert b"Cars" in response.data
    assert b"Done!" not in response.data


def test_return_page(test_client):
    response = test_client.get('/return')
    assert response.status_code == 200
    assert b"Done!" in response.data