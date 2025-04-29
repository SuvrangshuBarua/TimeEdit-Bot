# 📅 TimeEdit-Bot

This is a Python script that uses **Selenium WebDriver** to automate adding multiple course schedules to the **TimeEdit** system used by **Chalmers University of Technology**. The script navigates to the TimeEdit public interface, searches for given course codes, adds them to the basket, and opens the schedule page for selected courses.

---

## 🚀 Features

- Automates navigation to Chalmers TimeEdit page.
- Accepts multiple course codes separated by semicolons (e.g., `TDA550;DAT320`).
- Searches each course and adds it to the selection basket.
- Opens the final schedule after adding all courses.
- Captures a final screenshot (`final_result.png`) for visual verification.

---

## 🧑‍💻 Prerequisites

- Python 3.7 or higher
- Google Chrome installed
- ChromeDriver installed (version must match your Chrome version)

