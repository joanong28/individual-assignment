#how to set up and run the program
# README: Stock selection tool

## Overview
This is a simple Register and Login system that validates user registration and login credentials. The program ensures that:
- Registration confirms the email does not already exist.
- Login verifies both email and password match an existing record.

## Features
- Register new users.
- Login existing users.
- Error handling for invalid inputs.

---

## Prerequisites

To set up and run the program, ensure the following:

### Software
- Python 3.8 or higher

### Libraries
The following libraries are required and can be installed using pip:
```bash
pip install -r requirements.txt
```

### Database/Storage
The program uses a simple database, either:
1. A text file (`users.txt`) for storing user information.
2. SQLite for database storage (optional upgrade).

---

## Setup Instructions

### Step 1: Clone the Repository
```bash
git clone <repository-url>
cd <project-directory>
```

### Step 2: Set Up the Environment
- Install Python dependencies:
```bash
pip install -r requirements.txt
```
- Ensure a storage file/database is initialized (e.g., `users.txt`).

### Step 3: Running the Program
Execute the program using the following command:
```bash
python main.py
```

---

## Usage

### Register
1. Choose the **Register** option.
2. Enter your email and password.
3. If the email is not already registered, your account will be created successfully.

### Login
1. Choose the **Login** option.
2. Enter your email and password.
3. If the email and password match, you will be logged in.

---

## File Structure
```
.
├── main.py                # Main entry point of the program
├── users.txt              # Storage for registered users (if text file-based storage is used)
├── requirements.txt       # Python dependencies
├── README.md              # This README file
└── utils/                 # Utility functions (e.g., email validation, storage handling)
```
