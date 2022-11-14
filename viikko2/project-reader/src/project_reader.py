from urllib import request
from project import Project
import toml

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        content_parsed = toml.loads(content)["tool"]["poetry"]

        name = content_parsed["name"]
        description = content_parsed["description"]
        dependencies = content_parsed["dependencies"]
        devDependencies = content_parsed["dev-dependencies"]

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, description, dependencies, devDependencies)
