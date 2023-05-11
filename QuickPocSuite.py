import argparse
from engine.getPoc import GetPoc

def main():
    parser = argparse.ArgumentParser(description="Run GetPoc function")
    parser.add_argument("-y", "--yaml", help="the YAML file containing the PoC")
    parser.add_argument("-l", "--list", help="the file containing target URLs")
    parser.add_argument("-t", "--thread", type=int, help="the maximum time in seconds for each request,default: 20", required=False, default=20)
    parser.add_argument("-o", "--output", help="the file to output the results, default: output.txt", required=False, default="output.txt")

    args = parser.parse_args()
    poc = GetPoc(args.yaml, args.list, args.thread, args.output)
    poc.get_poc_batch()


if __name__ == "__main__":
    main()