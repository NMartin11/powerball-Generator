"""Class for generating ticket."""
import random


class Generate(object):
    """methods to generate ticket."""

    def get_ticket_list(file):
        """Get ticket as list."""
        array = []
        with open(file) as f:
            for i, line in enumerate(f):
                if i > 0 and i < 10:
                    current_line = line.split(" ", 1)
                    line = ''.join(current_line)
                    line = line.strip('\r\n')
                    array.append(line)
        return array

    def remove_date(list):
        """Remove date from list."""
        new_ticket = []
        for ticket in list:
            my_list = ticket.split("  ")  # Split ticket to isolate date
            date_index = my_list[0].split(" ")  # Splits first num from date
            del date_index[0]  # Delete date from first num

            my_list[0] = date_index[0]  # Replace first num without date
            new_ticket.append(my_list)

        return new_ticket

    def remove_mulitplier(list):
        """If ticket has 7 numbers remove last number."""
        list_mulities_removed = []
        for ticket in list:
            if len(ticket) == 7:
                # print(ticket, len(ticket))
                ticket.pop()
                list_mulities_removed.append(ticket)
        return list_mulities_removed

    def sort_tickets(unsorted_tickets):
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
        sorted(unique_ticket)
        unique_ticket.append(powerball)

        file = open('all_sorted_tickets.txt', 'r')

        while False:
            for line in file:
                if line == unique_ticket:
                    unique_ticket = random.sample(range(100), 7)
                    powerball = unique_ticket.pop()
                    sorted(unique_ticket)
                    unique_ticket.append(powerball)
                else:
                    True

        return unique_ticket


if __name__ == '__main__':
    """Used to test methods."""
    Ticket_gen = Generate()
    list = Ticket_gen.create_unique_ticket #TODO This is not working for some stupid fucking reason
    print(list)

