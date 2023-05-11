class getUrl():
    def __init__(self, urlPath):
        self.urlPath = urlPath

    def get_url(self):
        with open(self.urlPath, "r") as urlFile:
            urls = urlFile.readlines()
            for url in urls:
                url = url.strip()
                yield url
