"""Class for generating ticket."""
import random


class Generate(object):
    """methods to generate ticket."""

    def get_ticket_list(self, file):
        """Get ticket as list."""
        array = []
        with open(file) as f:
            for i, line in enumerate(f):
                current_line = line.split(" ", 1)
                line = ''.join(current_line)
                line = line.strip('\r\n')
                array.append(line)
        return array

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


    def create_unique_ticket(self):
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
    generate = Generate()
    ticket_history = generate.get_ticket_list("ticket_history.txt")
    ticket_history = generate.remove_date(ticket_history)
    ticket_history = generate.remove_mulitplier(ticket_history)

    generate.sort_tickets(ticket_history)

    unigue_ticket = generate.create_unique_ticket()
    print(unigue_ticket)

