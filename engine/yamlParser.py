import yaml

class yamlParser:
    def __init__(self, yamlPath):
        self.yamlPath = yamlPath

    def parse_yaml(self):
        with open(self.yamlPath, 'r') as yamlFile:
            data = yaml.safe_load(yamlFile)
        payload = data['payload']
        keyword = data['keyword']
        yamlJson = {"payload": payload, "keyword": keyword}
        return yamlJson


