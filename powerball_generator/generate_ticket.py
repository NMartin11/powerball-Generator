"""Class for generating ticket."""


class Generate:
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

    def sort_tickets(list):
        """Sorts individual tickets numbers except the powerball number."""

    """Used to test methods."""
    list = get_ticket_list('ticket_history.txt')
    list = remove_date(list)
    for x in list:
        print(x)

# if __name__ == "__main__":
#     """Execute only if run as a script."""
#     print(get_ticket_list('ticket_history.txt'))
