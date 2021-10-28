import logging
import threading

from .data import LdapData
from ..config import AppConfig

_sync_thread = None

def _run_ldap_synchronization():
    logging.debug("starting ldap synchronization")
    LdapData.fetch_data()
    start_ldap_synchronization_job()

def start_ldap_synchronization_job():
    global _sync_thread
    sync_seconds = AppConfig.get['ldap']['sync_seconds']
    _sync_thread = threading.Timer(sync_seconds, _run_ldap_synchronization)
    _sync_thread.start()

def stop_synchronization_job():
    global _sync_thread
    if _sync_thread is not None:
        logging.info("Stopping ldap synchronization thread")
        _sync_thread.cancel()
