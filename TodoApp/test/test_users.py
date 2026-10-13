from .utils import *
from ..routers.users import get_db, get_current_user
from fastapi import status

app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user] = override_get_current_user


def test_return_user(test_user):
    response = client.get('/user')
    assert response.status_code == status.HTTP_200_OK
    assert response.json()['username'] == 'hal_jordan_test'
    assert response.json()['email'] == 'haljordantest@email.com'
    assert response.json()['first_name'] == 'Hal'
    assert response.json()['last_name'] == 'Jordan'
    assert response.json()['role'] == 'admin'
    assert response.json()['phone_number'] == '9999999999'


def test_change_password_success(test_user):
    response = client.put('/user/password', json={'password': 'testpassword',
                                                  'new_password': 'newpassword'})
    assert response.status_code == status.HTTP_204_NO_CONTENT


def test_change_password_invalid(test_user):
    response = client.put('/user/password', json={'password': 'wrongpassword',
                                                  'new_password': 'newpassword'})
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert response.json() == {'detail': 'Incorrect Password!'}

def test_change_phone_number_success(test_user):
    response = client.put('/user/phonenumber/8888888888')
    assert response.status_code == status.HTTP_204_NO_CONTENT
