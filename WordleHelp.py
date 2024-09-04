###
# Main code for WordleHelper program
# Implements the command loop and uses a CmdProcessor
# object to process each of the supported commands
import CmdProcessor as cp

wordsDict = {}

if __name__ == "__main__":

    cmdProcessor = cp.CmdProcessor()

    line = input("Command?> ").lower()
    while(line != "quit" and line != "exit"):
        if line == "?" or line == "help":
            cmdProcessor.processHelp()
        elif line.startswith("add"):
            wordsDict = cmdProcessor.processAdd(line[4:])
            print("\x1b[33m[INFO] ", end="")
            print("\x1b[32mSuccessfully loaded {count} words".format(
                count=len(wordsDict)))
            print("\x1b[0m")
        elif line.startswith("match"):
            cmdProcessor.processMatch(line[6:])
        elif line.startswith("reset"):
            cmdProcessor.processReset(line)
        elif line.startswith("stats"):
            cmdProcessor.processStats(line)
        elif line.startswith("config"):
            cmdProcessor.processConfig(line)
        elif line.strip():
            # Anything else which is not an empty string
            # is a command which is not supported
            print("#Error: Command not recognized")
        line = input("Command?> ").lower()
    print("Goodbye!")

