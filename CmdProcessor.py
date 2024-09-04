from errno import WSAECONNABORTED

from Scraper import Scraper
from WordChecker import WordChecker


class CmdProcessor:

    def __init__(self) -> None:
        self.words = []
        self.checker = WordChecker(self.words)

    def processHelp(self):
        print("process command 'help'")

    def processAdd(self, args=None):
        if args is None or args == "":
            print("\x1b[31m[ERROR] ", end="")
            print("The Add function was not given a parameter")
            print("\x1b[0m")
            exit(-1)

        txt = Scraper(args)

        words = txt._text.split()

        myDict = {}

        lastWord = ""

        for word in words:
            word = ''.join(
                ch.lower() for ch in word if ch.isalnum or ch == '-' or ch == '\'')
            if len(word) == 5 and word.isalpha():
                self.words.append(word)

        self.checker = WordChecker(self.words)

        return self.words

    def processMatch(self, args=None):
        words = self.checker.check(args)

        print("\x1b[33m[INFO] ", end="")
        print("\x1b[32m{words} words remaining".format(words=len(words)))
        print("\x1b[0m", end="")

        for i in range(min(5, len(words))):
            print(words[i])

    def processReset(self, args=None):
        self.checker = WordChecker(self.words)
        print("\x1b[33m[INFO] ", end="")
        print("\x1b[32mSuccessfully reset hints")
        print("\x1b[0m")

