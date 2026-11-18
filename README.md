# Movie Ticket Booking System

A beginner-friendly, menu-driven movie ticket booking application built with **Python 3**. It runs in the console and lets users book seats, cancel bookings, and view the seat map. Bookings are saved in a text file so they remain available the next time the program is started.

## Project Details

- **Project Title:** Movie Ticket Booking System
- **PS No.:** 36
- **Author:** NIKHIL
- **Language:** Python 3
- **External Libraries:** None

## Features

- Book seats in a 15-seat movie hall.
- Cancel an existing booking.
- Display the current seat map.
- Prevent users from booking an already-booked seat.
- Validate seat codes (A1 to C5).
- Calculate the ticket amount at Rs. 200 per seat.
- Display a housefull message when all seats are booked.
- Load previous bookings when the program starts.
- Save booking changes automatically.

## Seat Layout

The hall has 3 rows (A, B, C), with 5 seats in each row.

| Row | Seats |
|---|---|
| A | A1, A2, A3, A4, A5 |
| B | B1, B2, B3, B4, B5 |
| C | C1, C2, C3, C4, C5 |

**Seat map symbols:**
- `X` = Booked
- `_` = Available

Each ticket costs **Rs. 200**.

## Project Structure

```text
Movie_Ticket_Booking_System/
├── main.py
├── bookings.txt
└── README.md
```

- `main.py` contains the complete Python program.
- `bookings.txt` stores saved bookings. It starts empty and is updated automatically.
- `README.md` explains the project.

## Requirements

- Python 3
- A terminal or command prompt

No external Python packages are required.

## How to Run

1. Download or clone this repository.
2. Open a terminal in the project folder.
3. Run:

   ```bash
   python main.py
   ```

   On some systems, use:

   ```bash
   python3 main.py
   ```

## Menu

```text
1. Book a seat
2. Cancel a booking
3. Display seat map
4. Exit
```

### Example: Booking a Seat

```text
Enter your choice (1-4): 1
Enter seat code (example: A1): A1
Enter your name: Aman
Seat A1 booked for Aman. Amount: 200
```

### Example: Seat Map

```text
     1   2   3   4   5
Row A:  X   _   _   _   _
Row B:  _   _   _   _   _
Row C:  _   _   _   _   _

X = Booked    _ = Available
Seats left: 14
```

## Booking File Format

Each saved booking is stored on a separate line in `bookings.txt`:

```text
A1|Aman
B2|Riya
```

The program reads this file at startup and updates it after every successful booking or cancellation. Keep `bookings.txt` in the same folder as `main.py`.

## Concepts Used

- Lists and dictionaries
- Loops and conditional statements
- Functions
- User input and validation
- File handling (`open`, `read`, and `write`)
- Exception handling (`FileNotFoundError`)

## Notes

- The program starts with all seats available if no saved booking file exists.
- Do not delete `bookings.txt` if you want to keep the saved bookings.
- This is a simple console-based project intended for learning Python fundamentals.

---

**Developed by NIKHIL**
