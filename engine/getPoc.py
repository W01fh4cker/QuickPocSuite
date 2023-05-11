import time
import requests
import threading
from engine.getUrl import getUrl
from engine.yamlParser import yamlParser
from concurrent.futures import ThreadPoolExecutor

class GetPoc():
    def __init__(self, yamlPath, urlPath, thread, outputFile):
        self.lock = threading.Lock()
        self.outputFile = outputFile
        parser = yamlParser(yamlPath)
        self.yamlName = str(yamlPath).split("/")[-1].replace(".yaml", "").replace(".\\", "")
        self.yamlJson = parser.parse_yaml()
        self.thread = thread
        self.urlPath = urlPath
        self.existurls = []
        self.GREEN = "\033[32m"
        self.CYAN = "\033[36m"
        self.YELLOW = "\033[33m"
        self.RESET = "\033[0m"
        self.RED = "\033[31m"

    def print_message(self, msg):
        with self.lock:
            print(msg)

    def get_poc_one(self, url):
        try:
            payload = self.yamlJson["payload"]
            keyword = self.yamlJson["keyword"]
            headers = {
                "User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; Tablet PC 2.0; wbx 1.0.0; wbxapp 1.0.0; Zoom 3.6.0)"
            }
            poc_url = url + payload
            resp = requests.get(url=poc_url, headers=headers, verify=False, timeout=30, allow_redirects=False)
            if keyword in resp.text:
                current_time = time.strftime("[%Y-%m-%d %H:%M:%S]")
                status = "存在漏洞"
                output_text = f"{self.CYAN}{current_time}{self.RESET} {self.YELLOW}[{self.yamlName}]{self.RESET}  {self.GREEN}[{status}]{self.RESET}  {self.YELLOW}[{poc_url}]{self.RESET}"
                self.existurls.append(poc_url)
                self.print_message(output_text)
            else:
                current_time = time.strftime("[%Y-%m-%d %H:%M:%S]")
                status = "不存在漏洞"
                output_text = f"{self.CYAN}{current_time}{self.RESET} {self.YELLOW}[{self.yamlName}]{self.RESET} {self.RED}[{status}]{self.RESET} {self.YELLOW}[{poc_url}]{self.RESET}"
                self.print_message(output_text)
        except:pass
        # except FileNotFoundError as err:
        #     current_time = time.strftime("[%Y-%m-%d %H:%M:%S]")
        #     status = "发生错误"
        #     errText = f"错误内容：{err}"
        #     output_text = f"{self.CYAN}{current_time}{self.RESET} {self.CYAN}[{self.yamlName}]{self.RESET} {self.RED}[{status}]{self.RESET} {self.YELLOW}[{errText}]{self.RESET} {self.YELLOW}[{poc_url}]{self.RESET}"
        #     print(output_text)

    def write_into_outputfile(self):
        with open(self.outputFile, "a+") as of:
            for existurl in self.existurls:
                of.write(existurl + "\n")
            of.close()
        current_time = time.strftime("[%Y-%m-%d %H:%M:%S]")
        info = f"扫描完毕，结果保存至{self.outputFile}。"
        output_text = f"{self.CYAN}{current_time}{self.RESET} {self.YELLOW}[{self.yamlName}]{self.RESET} {self.GREEN}[{info}]{self.RESET}"
        self.print_message(output_text)

    def get_poc_batch(self):
        urls = getUrl(self.urlPath).get_url()
        with ThreadPoolExecutor(max_workers=self.thread) as executor:
            executor.map(lambda url: self.get_poc_one(url), urls)
        self.write_into_outputfile()
