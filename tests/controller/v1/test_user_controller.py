from flask.testing import FlaskClient


def test_add_user(client: FlaskClient):
    x = client.post(
        "/v1/user",
        json={
            "username": "gal",
            "password": "1234",
            "fullname": "Gal Rabin",
            "email": "galrabin@gmail.com",
        },
    )
    print(x)
    pass
