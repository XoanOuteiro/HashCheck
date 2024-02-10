import argparse
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style
from Compute import Compute
from ResponseCodes import R

def buildArgs():

    parser = argparse.ArgumentParser(description="HashCheck")

    parser.add_argument("-v", "--version", action="version", version="HashCheck 0.0.1")

    parser.add_argument("-pF", "--parseFile", help="Get a hash for a single specified file")
    parser.add_argument("-f", "--file", help="Specify a file for the hash check")
    #  In the future i may add an option to check entire folders
    parser.add_argument("-tF", "--toFile", help="Specify a secondary file to hash and check to the -f file")
    parser.add_argument("-tH", "--toHash", help="Specify a hash to be checked against the -f file (NOTE: This program uses MD5)")

    return parser.parse_args()

def parseInput(args):

    colorama_init()
    compute = Compute()

    if args.parseFile:

        file = args.parseFile

        result = compute.monoFile(file)
        if result == R.RESPONSE_CHECK_FILE_1_NOTFOUND:
            parseResponseCode(result)

        else:
            print(f'{Fore.GREEN}[+] Hash for {file}{Style.RESET_ALL} = ' + result)

    elif args.file and args.toFile or args.toHash:

        file = args.file
        
        if args.toFile:
            secondFile = args.toFile
            parseResponseCode(compute.fileToFile(file, secondFile))

        elif args.toHash:
            givenHash = args.toHash
            parseResponseCode(compute.fileToHash(file, givenHash))

    else:

        parseResponseCode(R.RESPONSE_CODE_USAGE_ERROR)

def parseResponseCode(responseCode):

    colorama_init()

    # Error Template = f'{Fore.Color} [][] msg {Style.RESET_ALL}\t|\t code \t|\t type \t|\t msg'

    codeResDict = {

        R.RESPONSE_CODE_USAGE_ERROR : f'{Fore.RED}[-] ERROR {Style.RESET_ALL}\t|\t{Fore.RED} 800 {Style.RESET_ALL}\t|\t Usage Incorrect! \t|\t Please check -h/--help for instructions',
        R.RESPONSE_CHECK_FILE_1_NOTFOUND : f'{Fore.RED}[-] ERROR {Style.RESET_ALL}\t|\t{Fore.RED} 201 {Style.RESET_ALL}\t|\t File Not Valid \t|\t The first given file was invalid (not found or not file entity)',
        R.RESPONSE_CHECK_FILE_2_NOTFOUND : f'{Fore.RED}[-] ERROR {Style.RESET_ALL}\t|\t{Fore.RED} 202 {Style.RESET_ALL}\t|\t File Not Valid \t|\t The second given file was invalid (not found or not file entity)',
        R.RESPONSE_CHECK_VALID : f'{Fore.GREEN}[+][+] Check Run {Style.RESET_ALL}\t|\t{Fore.GREEN} 200 {Style.RESET_ALL}\t|\t The given input match',
        R.RESPONSE_CHECK_INVALID : f'{Fore.GREEN}[+][-] Check Run {Style.RESET_ALL}\t|\t{Fore.RED} 000 {Style.RESET_ALL}\t|\t The given data did NOT input match'

    }

    print(codeResDict.get(responseCode))


def main():
    args = buildArgs()
    parseInput(args)

if __name__ == "__main__":
    main()