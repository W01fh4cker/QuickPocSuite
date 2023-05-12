import time

class PrintMessage:

    def __init__(self, lock, yamlName):
        self.lock = lock
        self.yamlName = yamlName
        self.currentTime = time.strftime("[%Y-%m-%d %H:%M:%S]")
        # color
        self.GREEN = "\033[32m"
        self.CYAN = "\033[36m"
        self.YELLOW = "\033[33m"
        self.RESET = "\033[0m"
        self.RED = "\033[31m"

    def print_message(self, msg):
        with self.lock:
            print(msg)

    def print_success(self, info, poc_url):
        output_text = f"{self.CYAN}{self.currentTime}{self.RESET} {self.YELLOW}[{self.yamlName}]{self.RESET}  {self.GREEN}[{info}]{self.RESET}  {self.YELLOW}[{poc_url}]{self.RESET}"
        self.print_message(output_text)

    def print_error(self, info, poc_url):
        output_text = f"{self.CYAN}{self.currentTime}{self.RESET} {self.YELLOW}[{self.yamlName}]{self.RESET} {self.RED}[{info}]{self.RESET} {self.YELLOW}[{poc_url}]{self.RESET}"
        self.print_message(output_text)

    def print_write_file_success(self, info):
        output_text = f"{self.CYAN}{self.currentTime}{self.RESET} {self.YELLOW}[{self.yamlName}]{self.RESET} {self.GREEN}[{info}]{self.RESET}"
        self.print_message(output_text)