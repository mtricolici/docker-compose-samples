import re
import logging
import http.server
import socketserver
import threading

from .config import AppConfig
from .jwt_helper import JWTHelper

class JWTHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        logging.debug("==> GET '%s'", self.path)
        logging.debug("headers: %s", self.headers)

        if self.path == "/healthz":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            return
        if self.path == "/auth":
            self.handle_auth()
            return

        self.send_response(501, "not implemented yet")
        self.end_headers()

    def handle_auth(self):
        try:
            if 'Authorization' not in self.headers:
                raise ValueError("Authorization header is missing")
            auth_header = self.headers['Authorization'].strip()
            if not re.match("^Bearer", auth_header):
                raise ValueError("Unsupporte authentication method")
            token = auth_header.removeprefix("Bearer").strip()
            logging.debug("auth. verify token: %s", token)
            helper = JWTHelper()
            helper.verify(token)

            self.send_response(200)
            self.end_headers()
        except Exception as e:
            logging.error("AuthError:%s", e)
            self.send_response(401)
            self.end_headers()

    def do_POST(self):
        if self.path == "/generate-token.exe":
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode("utf-8")
            logging.debug("POST data: '%s'", post_data)
            # post data should look like 'user=user1'. a dirty hack just for POC
            user_id = post_data.split("=")[1]
            
            #TODO: read email from ldap
            email = "{}@zuzu.com".format(user_id)

            #TODO: verify presence of the user ;)
            helper = JWTHelper()
            token = helper.generate(user_id, email)
            if token is None:
                self.send_response(200)
                self.end_headers()
                self.wfile.write(
                    "Error. cannot create a ticket for you. please try again never:D".encode("utf-8"))
            else:
                self.send_response(200)
                self.end_headers()
                self.wfile.write("preved '{}'!\n Please find your token:\n{}\n\n"
                    .format(user_id, token).encode("utf-8"))
                self.wfile.write("Usage example:\n".encode("utf-8"))
                self.wfile.write("curl -H \"Authorization: Bearer {}\" http://localhost:8888/admin".format(
                    token).encode("utf-8"))
            return;
        self.send_response(501, "not implemented yet")
        self.end_headers()


_jwt_handler = None

def run_jwt_handler():
    global _jwt_handler
    port = AppConfig.get['bind_port']
    _jwt_handler = socketserver.TCPServer(("0.0.0.0", port), JWTHandler)
    logging.info("Starting JWT handler on %d port ...", port)
    # serve_forever should not be in main thread!!!
    # shutdown will be called from the main thread while handling SIGTERM or SIGINT
    thr = threading.Thread(target = _jwt_handler.serve_forever)
    thr.start()
    thr.join()

def stop_jwt_handler():
    global _jwt_handler
    if _jwt_handler is not None:
        logging.info("Stopping JWT handler ...")
        _jwt_handler.shutdown()
