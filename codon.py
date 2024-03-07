import os, sys

def toRNA(string: str):
    result = ""
    string = string.upper()
    for char in string:
        if char == 'A':
            result += 'U'
        elif char == 'T':
            result += 'A'
        elif char == 'C':
            result += 'G'
        elif char == 'G':
            result += 'C'
        elif char == '-':
            result += char
    return result

def main(argv):
    os.system('clear')
    while True:
        string = str(input("Enter RNA: "))
        if string == "":
            return
        print(toRNA(string))



if __name__ == "__main__":
    main(sys.argv)