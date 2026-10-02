# Python and Database Assignment

This project contains Tasks 1 to 5 for the Python and Database assignment.

## Task 1 — API Data Retrieval and Storage

### Objective
Retrieve book data from an external REST API, store it in a local SQLite database, and display the retrieved data.

### Steps
1. Open the assignment folder in VS Code.
2. Create or open `collect_books.py`.
3. Install Requests:
   ```bash
   pip install requests
   ```
4. Run:
   ```bash
   python collect_books.py
   ```
5. The program retrieves book data from the Open Library API.
6. The data is stored in `books.db`.
7. Open `books.db` with the SQLite extension.
8. Expand `books.db` → `books` and verify the stored records.

### Files
- `collect_books.py`
- `books.db`

---

## Task 2 — Data Processing and Visualization

### Objective
Retrieve student test scores from an API, calculate averages, and create a bar chart.

### Steps
1. Create `student_scores.py`.
2. Install the required libraries:
   ```bash
   pip install requests matplotlib
   ```
3. Run:
   ```bash
   python student_scores.py
   ```
4. Check the terminal for the number of students and average scores.
5. Check that `student_average_scores.png` was created.
6. Open the PNG file to view the bar chart.

### Files
- `student_scores.py`
- `student_average_scores.png`

---

## Task 3 — CSV Data Import to Database

### Objective
Read user information from a CSV file and insert it into an SQLite database.

### Steps
1. Create `users.csv` with the name and email columns.
2. Create or open `csv_to_sqlite.py`.
3. Run:
   ```bash
   python csv_to_sqlite.py
   ```
4. The program reads the CSV file and inserts the users into `users.db`.
5. Open `users.db` using the SQLite extension.
6. Expand `users.db` → `users` and verify the imported records.

### Files
- `users.csv`
- `csv_to_sqlite.py`
- `users.db`

---

## Task 4 — Most Complex Python Code

### Objective
Provide a link to the most complex Python code written for the assignment.

### Steps
1. Create `complex_python.py`.
2. Add the resilient concurrent API pipeline code.
3. Install Requests:
   ```bash
   pip install requests
   ```
4. Run:
   ```bash
   python complex_python.py
   ```
5. Verify that the program runs successfully.
6. Upload `complex_python.py` to the GitHub assignment repository.
7. Open `complex_python.py` on GitHub.
8. Copy its GitHub URL.
9. Submit that URL for Task 4.

### Main concepts used
- REST API requests
- `ThreadPoolExecutor`
- Concurrent processing
- Retry handling
- Exponential backoff
- Error handling
- Dataclasses
- Average calculation
- Sorting results

### File
- `complex_python.py`

---

## Task 5 — Most Complex Database Code

### Objective
Provide a link to the most complex database-related Python code written for the assignment.

For this project, use `collect_books.py`.

### Steps
1. Open `collect_books.py`.
2. Run:
   ```bash
   python collect_books.py
   ```
3. Verify that `books.db` is created or updated.
4. Open `books.db` with the SQLite extension.
5. Verify the `books` table and its records.
6. Upload `collect_books.py` to the GitHub assignment repository.
7. Open `collect_books.py` on GitHub.
8. Copy its GitHub URL.
9. Submit that URL for Task 5.

### Database concepts used
- SQLite connection
- Table creation
- SQL INSERT operations
- SQL SELECT operations
- Storing API data
- Reading records from the database

### File
- `collect_books.py`

---

# Final Submission Checklist

---

# Project Structure

```text
Accuknox-assignment/
├── README.md
├── collect_books.py
├── books.db
├── student_scores.py
├── student_average_scores.png
├── users.csv
├── csv_to_sqlite.py
├── users.db
└── complex_python.py
```

## Technologies Used

- Python
- SQLite
- REST APIs
- Requests
- Matplotlib
- CSV
- GitHub
