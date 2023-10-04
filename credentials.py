import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "modules", "TwoNotesEcosystemPyTools", "src", "modules", ""))

from auth.service import Service


def get_credentials(service:str, user: str) -> tuple:
    service = Service.getTwoNotesIdentities().getServices()[service]
    account = service[user]
    return (account.login, account.password)


def get_db_credentials() -> tuple:
    return get_credentials("DNA_DB", "User")


def get_jenkins_credentials() -> tuple:
    return get_credentials("Jenkins", "User")
