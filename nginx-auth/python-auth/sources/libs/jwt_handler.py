import logging
import http.server
import socketserver
import threading

from .config import AppConfig

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
        self.send_response(200)
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
