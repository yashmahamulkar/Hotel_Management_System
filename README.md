# Hotel_Management_System

This project is a Python-based Hotel Management system that utilizes a MySQL database to manage customer and room booking information. The system includes functionality to:

- Add new customers to the database.
- Book rooms for customers.

## Features

1. **Database Integration**: Connects to a MySQL database to store and retrieve customer and room booking details.
2. **Customer Management**: Allows the addition of new customers, storing their details such as name, address, contact information, ID proof, and occupancy details.
3. **Room Booking**: Enables booking of rooms for customers, marking rooms as occupied and storing booking details like date of occupancy and advance payment.
4. **Food Service** : Enables users to track their food and other expences.
5. **Input Validation**: Prompts users for input and validates availability of rooms and existence of customer records before proceeding.

## Prerequisites

- Python 3.x installed on your system.
- MySQL server installed and configured.
- A MySQL database named `hotel` with appropriate user credentials.

## Setup Instructions

1. **Install Required Libraries**:
   Ensure you have the `mysql-connector` library installed:
   ```bash
   pip install mysql-connector-python
   ```

2. **Create Database and Tables**:
   The script will automatically create the `customer` table if it does not exist.

3. **Modify Database Configuration**:
   Update the `conn` variable in the script with your MySQL credentials:
   ```python
   conn = mysql.connector.connect(
       host='localhost',
       database='hotel',
       user='root',
       password='yash',
       autocommit=True
   )
   ```

4. **Run the Script**:
   Execute the script in your Python environment.
   ```bash
   python room_booking.py
   ```

## Usage Instructions

### Adding a New Customer

1. Run the script and select the option to add a new customer.
2. Enter the following details when prompted:
   - Name
   - Address
   - Phone Number
   - Email
   - ID Proof Type (e.g., Aadhar, Passport, DL, Voter ID)
   - ID Proof Number
   - Number of Males, Females, and Children
   - Date of Entry (yyyy-mm-dd format)

3. Upon successful entry, the customer details will be stored in the `customer` table.

### Booking a Room

1. Enter the room number to book.
2. Enter the customer ID.
3. Enter the date of occupancy in `yyyy-mm-dd` format.
4. Enter the advance amount.

5. The system will:
   - Verify the availability of the room.
   - Check if the customer exists in the database.
   - Update the `rooms` table to mark the room as occupied.
   - Insert booking details into the `booking` table.

6. If successful, a confirmation message will be displayed.

### Error Handling

- If the room is already occupied, an appropriate message will be displayed.
- If the customer does not exist, the system will prompt you to add the customer first.



## Notes

- Ensure the MySQL `hotel` database has the required `rooms` and `booking` tables.
- The `clear()` function is used to simulate clearing the console output for better readability.
- Update the `rooms` and `customer_exist()` logic to match your database schema.


## License

This project is open-source and available for personal and educational use. Feel free to modify and distribute it.

## Author

Yash Mahamulkar


<a href="https://www.mysql.com/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/mysql/mysql-original-wordmark.svg" alt="mysql" width="40" height="40"/> </a> <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a>
