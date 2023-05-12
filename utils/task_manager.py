import os
import yaml
import requests
import threading
from engine.getUrl import getUrl
from engine.getMethod import GetMethod
from engine.postMethod import PostMethod
from utils.print_message import PrintMessage
from concurrent.futures import ThreadPoolExecutor
from utils.write_into_outputfile import WriteIntoOutputFile

class TaskManager:
    def __init__(self, yamlPath, urlPath, thread, outputFile):
        self.yamlPath = yamlPath
        self.yamlName = os.path.basename(yamlPath).replace(".yaml", "")
        self.urlPath = urlPath
        self.thread = thread
        self.outputFile = outputFile
        self.urls = getUrl(self.urlPath).get_url()
        self.session = requests.Session()
        self.yamlJson = self.yaml2json()
        self.lock = threading.Lock()
        self.message_print = PrintMessage(self.lock, self.yamlName)
        self.existurls = []

    def yaml2json(self):
        with open(self.yamlPath, 'r', encoding="utf-8") as yamlFile:
            self.yamlJson = yaml.safe_load(yamlFile)
        return self.yamlJson

    def task_assignment(self, url):
        self.reqs = self.yamlJson["request"]
        self.results = []
        for req in self.reqs:
            self.payload = req["payload"]
            self.headers = req["headers"]
            self.keyword = req["keyword"]
            self.status = req["status"]
            if req["method"] == "GET":
                result = GetMethod(self.urlPath, self.thread).get_method(url, self.session, self.payload, self.headers, self.keyword, self.status)
                self.results.append(result)
            if req["method"] == "POST":
                self.data = req["data"]
                result = PostMethod(self.urlPath, self.thread).post_method(url, self.session, self.payload, self.headers, self.keyword, self.data, self.status)
                self.results.append(result)
        self.session.close()
        if all(self.results):
            self.existurls.append(url)
            info = "存在漏洞"
            self.message_print.print_success(info, url + self.payload)
        else:
            info = "不存在漏洞"
            self.message_print.print_error(info, url + self.payload)

    def task_apply(self):
        with ThreadPoolExecutor(max_workers=self.thread) as executor:
            executor.map(lambda url: self.task_assignment(url), self.urls)
        self.opFile = WriteIntoOutputFile(self.outputFile, self.existurls)
        self.opFile.write_into_outputfile()
        info = f"扫描完毕，结果保存至{self.outputFile}。"
        self.message_print.print_write_file_success(info)