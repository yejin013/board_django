from calendar import timegm
from datetime import datetime
import jwt

from rest_framework_jwt.compat import get_username_field
from rest_framework_jwt.settings import api_settings
from rest_framework_jwt.utils import jwt_get_secret_key


def jwt_payload_handler(user):
    username_field = get_username_field()
    payload = {'userID': user.userID, 'username':user.username,
               'exp': datetime.utcnow() + api_settings.JWT_EXPIRATION_DELTA}

    payload[username_field] = user.userID

    if api_settings.JWT_ALLOW_REFRESH:
        payload['orig_iat'] = timegm(
            datetime.utcnow().utctimetuple()
        )

    if api_settings.JWT_AUDIENCE is not None:
        payload['aud'] = api_settings.JWT_AUDIENCE

    if api_settings.JWT_ISSUER is not None:
        payload['iss'] = api_settings.JWT_ISSUER

    return payload

def jwt_encode_handler(payload):
    key = api_settings.JWT_PRIVATE_KEY or jwt_get_secret_key(payload)
    return jwt.encode(
        payload,
        key,
        api_settings.JWT_ALGORITHM
    ).decode('utf-8')