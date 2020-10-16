from suds.client import Client
from suds import WebFault


class SoapHelper:
    def __init__(self, app):
        self.app = app

    def take_array_project(self, username, password):
        client = Client("http://localhost/mantisbt/api/soap/mantisconnect.php?wsdl")
        try:
            client.service.mc_projects_get_user_accessible(username, password)
            return list(client.service.mc_projects_get_user_accessible(username, password))
        except WebFault:
            return False

