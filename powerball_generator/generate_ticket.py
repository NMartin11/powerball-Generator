"""Class for generating ticket."""
import random


class Generate(object):
    """methods to generate ticket."""

    def sort_tickets(self, ticket):
        """Sorts individual tickets numbers except the powerball number."""
        sorted_ticket = []
        if len(ticket) != 0:
            powerball = ticket.pop()
            ticket.sort()
            sorted_ticket = list(ticket)
            sorted_ticket.append(powerball)

        return sorted_ticket

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
        for x in range(5):
            number = random.randint(1, 69)
            while number in unique_ticket:
                number = random.randint(1, 69)
            unique_ticket.append(number)

        powerball = random.randint(1, 45)
        while powerball in unique_ticket:
            powerball =  random.randint(1, 45)

        unique_ticket.append(powerball)
        return unique_ticket

    def check_if_unique(self, unique_ticket):
        is_unique = True
        check_ticket = list(unique_ticket)
        file = open('ticket_history.txt', 'r')
        for line in file:
            print(line)
            check_ticket = self.sort_tickets(check_ticket)
            if check_ticket == line:
                is_unique = False
                return is_unique #return false
            else:
                continue
            # if line == unique_ticket:
            #     new_ticket = random.sample(range(70), 6)
            #     powerball = random.sample(range(46), 1)
            #     print("powerball: ", powerball)
            #     sorted(new_ticket)
            #     new_ticket.append(powerball)

        file.close()

        return is_unique #return true


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
    # ticket_history = generator.remove_date(ticket_history)
    # ticket_history = generator.remove_mulitplier(ticket_history)

    # generator.sort_tickets(ticket_history)

    unique_ticket = generator.create_unique_ticket()
    if generator.check_if_unique(unique_ticket):
        print(f"Unique ticket {unique_ticket}")
    else:
        print("ticket wasn't unique")









