"""Class for generating ticket."""
import random


class Generate(object):
    """methods to generate ticket."""

    def get_ticket_list(self, file_name):
        """Get ticket as list."""
        array = []
        with open(file_name, 'r') as f:
            for i, line in enumerate(f):
                current_line = line.split(" ", 1)
                line = ''.join(current_line)
                line = line.strip('\r\n')
                array.append(line)
        return array

    def create_unique_ticket(self):
        """Creates a unique ticket that isn't in history.txt"""
        unique_ticket = []
        for x in range(6):
            number = random.randint(0, 99)
            if number in unique_ticket:
                continue
            else:
                unique_ticket.append(number)

    def check_if_unique(self, ticket):
        sorted_file = open('all_sorted_tickets', 'r')
        for line in sorted_file:
            if line == ticket:
                return False
        unique_ticket = random.sample(range(100), 7)
        powerball = unique_ticket.pop()
        unique_ticket.sort()
        unique_ticket.append(powerball)

        file = open('all_sorted_tickets.txt', 'r')
        for line in file:
            if line == unique_ticket:
                unique_ticket = random.sample(range(100), 7)
                powerball = unique_ticket.pop()
                print("powerball: ", powerball)
                sorted(unique_ticket)
                unique_ticket.append(powerball)

        file.close()

        return unique_ticket


if __name__ == '__main__':
    """Used to test methods."""
    """"
        1. get ticket history ( should already be sorted, multiplier removed, and date removed )
        2. create ticket
        3. check if unique against the ticket history file
        4. if unique print
            else repeat step 2 and 3


    """
    generator= Generate()
    ticket_history = generator.get_ticket_list("ticket_history.txt")
    ticket_history = generator.remove_date(ticket_history)
    ticket_history = generator.remove_mulitplier(ticket_history)

    generator.sort_tickets(ticket_history)

    unigue_ticket = generator.create_unique_ticket()
    print(unigue_ticket)
