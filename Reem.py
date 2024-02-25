

from datetime import datetime

class BoardingPass:
    def __init__(self, passenger_name, flight_number, departure_airport, destination_airport, arrival_datetime, gate, seat_number, electronic_ticket):
        self.passenger_name = passenger_name
        self.flight_number = flight_number
        self.departure_airport = departure_airport
        self.destination_airport = destination_airport
        self.arrival_datetime = arrival_datetime
        self.gate = gate
        self.seat_number = seat_number
        self.electronic_ticket = electronic_ticket

    def get_passenger_name(self):
        return self.passenger_name

    def get_flight_number(self):
        return self.flight_number

    def get_departure_airport(self):
        return self.departure_airport

    def get_destination_airport(self):
        return self.destination_airport

    def get_arrival_datetime(self):
        return self.arrival_datetime

    def get_gate(self):
        return self.gate

    def get_seat_number(self):
        return self.seat_number

    def get_electronic_ticket(self):
        return self.electronic_ticket

class Flight:
    def __init__(self, flight_number, departure_airport, destination_airport, departure_datetime, arrival_datetime, gate):
        self.flight_number = flight_number
        self.departure_airport = departure_airport
        self.destination_airport = destination_airport
        self.departure_datetime = departure_datetime
        self.arrival_datetime = arrival_datetime
        self.gate = gate

    def get_flight_number(self):
        return self.flight_number

    def get_departure_airport(self):
        return self.departure_airport

    def get_destination_airport(self):
        return self.destination_airport

    def get_departure_datetime(self):
        return self.departure_datetime

    def get_arrival_datetime(self):
        return self.arrival_datetime

    def get_gate(self):
        return self.gate

class Passenger:
    def __init__(self, name, ticket_number, seat_number):
        self.name = name
        self.ticket_number = ticket_number
        self.seat_number = seat_number

    def get_name(self):
        return self.name

    def get_ticket_number(self):
        return self.ticket_number

    def get_seat_number(self):
        return self.seat_number

class System:
    def __init__(self, name, flight):
        self.name = name
        self.flight = flight

    def get_name(self):
        return self.name

    def get_flight(self):
        return self.flight

from datetime import datetime

class BoardingPass:
    def __init__(self, passenger_name, flight_number, departure_airport, destination_airport, arrival_datetime, gate, seat_number, electronic_ticket):
        self.passenger_name = passenger_name
        self.flight_number = flight_number
        self.departure_airport = departure_airport
        self.destination_airport = destination_airport
        self.arrival_datetime = arrival_datetime
        self.gate = gate
        self.seat_number = seat_number
        self.electronic_ticket = electronic_ticket

    def display_boarding_pass(self):
        boarding_pass = f"""
        BOARDING PASS
        -------------

        Passenger: {self.passenger_name}
        Flight Number: {self.flight_number}
        Departure Airport: {self.departure_airport}
        Destination Airport: {self.destination_airport}
        Departure Date and Time: {self.arrival_datetime.strftime('%Y-%m-%d %H:%M')}
        Gate: {self.gate}
        Seat Number: {self.seat_number}
        Electronic Ticket: {self.electronic_ticket}
        """

        print(boarding_pass)

# Example usage:
boarding_pass = BoardingPass("Amna", "ABC123", "Airport A", "Airport B",
                             datetime(2024, 3, 15, 10, 0), "Gate 1", "A1", "1234567890")
boarding_pass.display_boarding_pass()

class BoardingPass:
    def __init__(self, passenger_name, flight_number, departure_airport, destination_airport, arrival_datetime, gate, seat_number, electronic_ticket):
        self.passenger_name = passenger_name
        self.flight_number = flight_number
        self.departure_airport = departure_airport
        self.destination_airport = destination_airport
        self.arrival_datetime = arrival_datetime
        self.gate = gate
        self.seat_number = seat_number
        self.electronic_ticket = electronic_ticket

    def display_boarding_pass(self):
        # ANSI escape codes for colors
        HEADER = '\033[95m'
        GREEN = '\033[92m'
        ENDC = '\033[0m'

        boarding_pass = f"""
        {HEADER}BOARDING PASS{ENDC}
        -------------

        {GREEN}Passenger: {self.passenger_name}
        Flight Number: {self.flight_number}
        Departure Airport: {self.departure_airport}
        Destination Airport: {self.destination_airport}
        Departure Date and Time: {self.arrival_datetime.strftime('%Y-%m-%d %H:%M')}
        Gate: {self.gate}
        Seat Number: {self.seat_number}
        Electronic Ticket: {self.electronic_ticket}{ENDC}
        """

        print(boarding_pass)

# Example usage:
boarding_pass = BoardingPass("Amna", "ABC123", "Airport A", "Airport B",
                             datetime(2024, 3, 15, 10, 0), "Gate 1", "A1", "1234567890")
boarding_pass.display_boarding_pass()

class BoardingPass:
    def __init__(self, passenger_name, flight_number, departure_airport, destination_airport, arrival_datetime, gate, seat_number, electronic_ticket):
        self.passenger_name = passenger_name
        self.flight_number = flight_number
        self.departure_airport = departure_airport
        self.destination_airport = destination_airport
        self.arrival_datetime = arrival_datetime
        self.gate = gate
        self.seat_number = seat_number
        self.electronic_ticket = electronic_ticket

    def update_passenger_name(self, new_name):
        self.passenger_name = new_name

    def update_seat_number(self, new_seat_number):
        self.seat_number = new_seat_number

    def update_gate(self, new_gate):
        self.gate = new_gate

    # Add similar update methods for other attributes as needed

    def display_boarding_pass(self):
        boarding_pass = f"""
        BOARDING PASS
        -------------

        Passenger: {self.passenger_name}
        Flight Number: {self.flight_number}
        Departure Airport: {self.departure_airport}
        Destination Airport: {self.destination_airport}
        Departure Date and Time: {self.arrival_datetime.strftime('%Y-%m-%d %H:%M')}
        Gate: {self.gate}
        Seat Number: {self.seat_number}
        Electronic Ticket: {self.electronic_ticket}
        """

        print(boarding_pass)

# Example usage:
boarding_pass = BoardingPass("Amna", "ABC123", "Airport A", "Airport B",
                             datetime(2024, 3, 15, 10, 0), "Gate 1", "A1", "1234567890")

print("Before Update:")
boarding_pass.display_boarding_pass()

boarding_pass.update_passenger_name("Amna")
boarding_pass.update_seat_number("B2")
boarding_pass.update_gate("Gate 2")

print("\nAfter Update:")
boarding_pass.display_boarding_pass()
