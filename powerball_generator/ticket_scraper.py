"""Scraps for powerball ticket history."""

from bs4 import BeautifulSoup
import requests


class ticket_scraper:
    """Used to create text file with ticket history."""

    #TODO Bring remove date and sort methods to this class
    #   can get history, remove date, mulitipliers and sort in one class.

    def Get_ticket_history(self):
        """gets ticket history."""
        r = requests.get("http://www.powerball.com/powerball/winnums-text.txt")

        data = r.text

        soup = BeautifulSoup(data, "html.parser")

        ticket_text = soup.get_text()

        ticket_file = open('ticket_history.txt', 'w')

        ticket_file.seek(0)
        ticket_file.truncate()

        lines = enumerate(ticket_text.split("\n"))
        for i, line in enumerate(lines):
            if i is 0:
                print("Didn't print first line")
            else:
                ticket = line[1]
                ticket_file.write(str(f"{ticket}"))

        ticket_file.close()


if __name__ == '__main__':
    """Used to test methods."""
    Scraper = ticket_scraper()
    Scraper.Get_ticket_history()
