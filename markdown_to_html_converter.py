import os
import sys
import markdown

def markdownConvert(input_file: str, output_file: str):
    if input_path_validator(input_file) and output_path_validator(output_file):
        contents = ''
        with open(input_file, 'r', encoding="utf-8") as f:
            contents = f.read()
        with open(output_file, 'w', encoding="utf-8") as f:
            html = markdown.markdown(contents)
            f.write(html)


COMMAND = {
    "markdown": markdownConvert,
}

ARGUMENT_AMOUNT = {
    "markdown": 2,
}

def input_path_validator(input_path: str):
    if not input_path.endswith(".md"):
        print("Input file should be markdown file(.md).")
        return False
    if not os.path.isfile(input_path):
        print("Input file does not exist. Or it is not a file.")
        return False
    return True

def output_path_validator(output_path: str):
    if not output_path.endswith(".html"):
        print("Output file should be html(.html).")
        return False
    return True

def validator(args):
    if not args[0] in COMMAND:
        print("This is not a valid command.")
        return False
    if len(args)-1 != ARGUMENT_AMOUNT[args[0]]:
        print("Argument amount is not valid.")
        return False
    return True

## ここから実行プログラム

if validator(sys.argv[1:]):
    command = sys.argv[1]
    if(ARGUMENT_AMOUNT[command]==2):
        COMMAND[command](sys.argv[2], sys.argv[3])