import logging
import jwt
import datetime
import redis
import random, string

from .config import AppConfig

class JWTHelper:

    def __init__(self):
        self.alg = AppConfig.get['jwt']['alg']
        self.secret = AppConfig.get['jwt']['secret']
        self.expiration = AppConfig.get['jwt']['expiration_seconds']

    def verify(self, token, options={"verify_signature": True, "verify_exp": True}):
        return jwt.decode(token, self.secret, algorithms=[self.alg], options=options)

    def refresh(self):
        raise NotImplementedError

    def __generate_refresh_token(self):
        s=string.ascii_lowercase+string.digits
        return ''.join(random.sample(s,32))

    def generate(self, username, email):
        try:
            logging.debug("jtw:generate('%s','%s')", username, email)
            exp = datetime.datetime.utcnow() + datetime.timedelta(seconds=self.expiration)

            data = {'user': username, 'email': email, 'exp': exp}
            logging.debug("new generated token: %s", data)

            token = jwt.encode(data, self.secret, algorithm=self.alg)
            refresh_token = self.__generate_refresh_token()
            logging.debug("refresh tokenq: %s", refresh_token)
            logging.debug("redis host is '%s'", AppConfig.get['redis']['host'])
            logging.debug("redis port is '%d'", AppConfig.get['redis']['port'])
            r = redis.Redis(
                decode_responses=True,
                host=AppConfig.get['redis']['host'],
                port=AppConfig.get['redis']['port'], db=0)
            r.set(username, refresh_token)
            return token, refresh_token
        except Exception as e:
            logging.error("JWT:generate failure: %s", e)
            raise # I don't want to check for None when I call this :)


