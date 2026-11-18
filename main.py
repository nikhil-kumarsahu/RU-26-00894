# Movie Ticket Booking System
# Author: NIKHIL
# A beginner-friendly console application using only Python's built-in features.

BOOKING_FILE = "bookings.txt"
TICKET_PRICE = 200
ROWS = ["A", "B", "C"]
SEAT_NUMBERS = [1, 2, 3, 4, 5]


def create_seat_map():
    """Create the hall's seat map. None means that a seat is available."""
    seats = {}

    for row in ROWS:
        for number in SEAT_NUMBERS:
            seat_code = row + str(number)
            seats[seat_code] = None

    return seats


def load_bookings(seats):
    """Load saved bookings from the file when the program starts."""
    try:
        with open(BOOKING_FILE, "r") as file:
            for line in file:
                line = line.strip()

                if "|" not in line:
                    continue

                seat_code, name = line.split("|", 1)
                seat_code = seat_code.strip()
                name = name.strip()

                # Load only valid seat codes and non-empty names.
                if seat_code in seats and name:
                    seats[seat_code] = name

    except FileNotFoundError:
        # The file will be created automatically when the first booking is saved.
        pass


def save_bookings(seats):
    """Save all current bookings to the file."""
    with open(BOOKING_FILE, "w") as file:
        for seat_code, name in seats.items():
            if name is not None:
                file.write(seat_code + "|" + name + "\n")


def display_seat_map(seats):
    """Display all seats. X = booked, _ = available."""
    print("\n========== SEAT MAP ==========")
    print("     1   2   3   4   5")

    for row in ROWS:
        seat_status = []

        for number in SEAT_NUMBERS:
            seat_code = row + str(number)

            if seats[seat_code] is None:
                seat_status.append("_")
            else:
                seat_status.append("X")

        print("Row " + row + ":  " + "   ".join(seat_status))

    print("\nX = Booked    _ = Available")
    print("Seats left:", count_available_seats(seats))
    print("==============================\n")


def count_available_seats(seats):
    """Return the number of seats that are still available."""
    available = 0

    for name in seats.values():
        if name is None:
            available += 1

    return available


def book_seat(seats):
    """Book one available seat for a passenger."""
    if count_available_seats(seats) == 0:
        print("\nSorry, the show is housefull.")
        return

    seat_code = input("Enter seat code (example: A1): ").strip().upper()

    if seat_code not in seats:
        print("Invalid seat. Rows are A to C and seat numbers are 1 to 5.")
        return

    if seats[seat_code] is not None:
        print("Seat", seat_code, "is already booked.")
        return

    name = input("Enter your name: ").strip()

    if not name:
        print("Name cannot be empty. Booking cancelled.")
        return

    seats[seat_code] = name
    save_bookings(seats)

    print("Seat", seat_code, "booked for", name + ". Amount:", TICKET_PRICE)

    if count_available_seats(seats) == 0:
        print("Seats left: 0")
        print("Show is now housefull.")


def cancel_booking(seats):
    """Cancel an existing booking."""
    seat_code = input("Enter the seat code to cancel (example: A1): ").strip().upper()

    if seat_code not in seats:
        print("Invalid seat. Rows are A to C and seat numbers are 1 to 5.")
        return

    if seats[seat_code] is None:
        print("Seat", seat_code, "is not currently booked.")
        return

    passenger_name = seats[seat_code]
    seats[seat_code] = None
    save_bookings(seats)

    print("Booking for", passenger_name, "at seat", seat_code, "has been cancelled.")


def show_menu():
    """Display the main menu."""
    print("========== MOVIE TICKET BOOKING ==========")
    print("1. Book a seat")
    print("2. Cancel a booking")
    print("3. Display seat map")
    print("4. Exit")
    print("==========================================")


def main():
    seats = create_seat_map()
    load_bookings(seats)

    print("\nWelcome to the Movie Ticket Booking System!")
    print("Ticket price: Rs.", TICKET_PRICE)
    print("Total seats:", len(seats))

    while True:
        show_menu()
        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            book_seat(seats)
        elif choice == "2":
            cancel_booking(seats)
        elif choice == "3":
            display_seat_map(seats)
        elif choice == "4":
            print("Thank you for using the Movie Ticket Booking System!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

        print()


if __name__ == "__main__":
    main()
