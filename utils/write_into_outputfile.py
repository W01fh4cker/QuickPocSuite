class WriteIntoOutputFile:
    def __init__(self, outputFile, existurls):
        self.outputFile = outputFile
        self.existurls = existurls

    def write_into_outputfile(self):
        with open(self.outputFile, "a+") as of:
            for existurl in self.existurls:
                of.write(existurl + "\n")
            of.close()