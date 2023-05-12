import urllib3
urllib3.disable_warnings()

class GetMethod:
    def __init__(self, urlPath, thread):
        self.thread = thread
        self.urlPath = urlPath
        self.default_headers = {
            "User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; Tablet PC 2.0; wbx 1.0.0; wbxapp 1.0.0; Zoom 3.6.0)"
        }

    def get_method(self, url, session, payload, headers, keyword, status):
        try:
            if headers is None:
                headers = self.default_headers
            poc_url = url + payload
            resp = session.get(url=poc_url, headers=headers, verify=False, timeout=30, allow_redirects=False)
            if keyword is not None:
                if keyword in resp.text and resp.status_code == status:
                    return True
                else:
                    return False
            else:
                if resp.status_code == status:
                    return True
                else:
                    return False
        except:
            return False