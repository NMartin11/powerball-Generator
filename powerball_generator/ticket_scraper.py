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
                ticket_file.write(str(ticket))

        ticket_file.close()

    def remove_date(self, list):
        """Remove date from list."""
        new_ticket = []
        for ticket in list:
            my_list = ticket.split("  ")  # Split ticket to isolate date
            date_index = my_list[0].split(" ")  # Splits first num from date
            del date_index[0]  # Delete date from first num

            my_list[0] = date_index[0]  # Replace first num without date
            new_ticket.append(my_list)

        return new_ticket

    def remove_mulitplier(self, list):
        """If ticket has 7 numbers remove last number."""
        list_mulities_removed = []
        for ticket in list:
            if len(ticket) == 7:
                # print(ticket, len(ticket))
                ticket.pop()
                list_mulities_removed.append(ticket)
        return list_mulities_removed

    def sort_tickets(self, unsorted_tickets):
        """Sorts individual tickets numbers except the powerball number."""
        sorted_tickets = []
        for ticket in unsorted_tickets:
            powerball = ticket.pop()
            ticket = sorted(ticket)
            ticket.append(powerball)
            sorted_tickets.append(ticket)

        """Writes to file with all sorted tickets"""
        file = open('all_sorted_tickets.txt', 'w')
        file.seek(0)
        file.truncate()

        file.write('\n'.join(str(line) for line in sorted_tickets))

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
