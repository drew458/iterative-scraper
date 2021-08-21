from src import IOConsole, ScraperMode

""" The script scrapes the page inserted as user input URL, looking for the text inserted as user input.
    Then it can either send notification if text is found on the page, or waiting and keep refreshing until the text
    goes away from the page. The mode choice is inserted as user input. 
    When triggered, it can send notification via screen, OS, Telegram. 
"""


def main():

    IOConsole.printStartMessage()

    # set the url
    url = IOConsole.inputUrl()

    # keywords to look for
    inputText = IOConsole.inputKeywords()

    # time from one check to another
    waitTime = IOConsole.inputTimeToSleep()

    mode = IOConsole.scraperMode()

    if int(mode) == 1:
        ScraperMode.mode1(url, inputText, waitTime)

    if int(mode) == 2:
        ScraperMode.mode2(url, inputText, waitTime)


if __name__ == "__main__":
    main()
