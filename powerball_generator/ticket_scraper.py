"""Scraps for powerball ticket history."""
from bs4 import BeautifulSoup
import requests


class ticket_scraper:
    """Used to create text file with ticket history."""

    #   TODO Bring remove date and sort methods to this class
    #   can get history, remove date, mulitipliers and sort in one class.

    def Get_ticket_history(self):
        """Gets ticket history."""
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
                ticket_without_date = self.remove_date(ticket)
                ticket_without_multiplier = self.remove_mulitplier(ticket_without_date)
                ticket_sorted = self.sort_tickets(ticket_without_multiplier) # TODO: fails on the split
                ticket_file.write(f"{ticket_sorted}\n")

        ticket_file.close()

    def remove_date(self, ticket):
        """Remove date from ticket."""
        list = ticket.split("  ")
        del list[0]

        return list

    def remove_mulitplier(self, ticket):
        """If ticket has 7 numbers remove last number."""
        if len(ticket) == 7:
            # print(ticket, len(ticket))
            ticket.pop()
        return ticket

    def sort_tickets(self, ticket):
        """Sorts individual tickets numbers except the powerball number."""
        print(f"ticket: {ticket}")
        sorted_ticket = []
        if len(ticket) != 0:
            powerball = ticket.pop()
            ticket.sort()
            sorted_ticket = list(ticket)
            # sorted_ticket.split(" ") # TODO: can't split on nonetype
            sorted_ticket.append(powerball)
            #TODO: sorted_ticket is nonetype: figure it out dumbass!!!

        return sorted_ticket


if __name__ == '__main__':
    """Used to test methods."""
    """
    # Steps
        get ticket history
        remove date
        remove mulitipliers
        sort history
    """
    Scraper = ticket_scraper()
    Scraper.Get_ticket_history()
