#using regex

import re

def main():
    fh = open('names.txt')
    for line in fh:
        match = re.search('(Len|Neverm)ore', line)
        if match:
            print(match.group())

if __name__ == "__main__":
    main()
    
