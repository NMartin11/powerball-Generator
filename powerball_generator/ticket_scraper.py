"""Scraps for powerball ticket history."""

from bs4 import BeautifulSoup
import requests


class ticket_scraper:
    """Used to create text file with ticket history."""

    def Get_ticket_history(self):
        """gets ticket history."""
        r = requests.get("http://www.powerball.com/powerball/winnums-text.txt")

        data = r.text

        soup = BeautifulSoup(data, "html.parser")

        ticket_text = soup.get_text()

        ticket_file = open('ticket_history.txt', 'w')

        ticket_file.seek(0)
        ticket_file.truncate()

        ticket_file.write(str(ticket_text))

        ticket_file.close()
