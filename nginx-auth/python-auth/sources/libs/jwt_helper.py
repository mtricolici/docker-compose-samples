import logging
import jwt
import datetime

from .config import AppConfig

class JWTHelper:

    def __init__(self):
        self.alg = AppConfig.get['jwt']['alg']
        self.secret = AppConfig.get['jwt']['secret']
        self.expiration = AppConfig.get['jwt']['expiration_seconds']

    def verify(self, token):
        jwt.decode(token, self.secret, algorithms=[self.alg], verify=True)

    def refresh(self):
        raise NotImplementedError

    def generate(self, username, email):
        try:
            logging.debug("jtw:generate('%s','%s')", username, email)
            exp = datetime.datetime.utcnow() + datetime.timedelta(seconds=self.expiration)

            data = {'user': username, 'email': email, 'exp': exp}
            logging.debug("new generated token: %s", data)

            token = jwt.encode(data, self.secret, algorithm=self.alg)
            #TODO: generate a refresh token and add it to response? save this refresh code somewhere.
            return token
        except Exception as e:
            logging.error("JWT:generate failure: %s", e)
            return None


