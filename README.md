# TimeEdit Course Schedule Automation Script

This is a Python script that uses **Selenium WebDriver** to automate the process of logging into the **Ladok** student portal, extracting registered course codes, and adding their schedules to the **TimeEdit** system used by **Chalmers University of Technology**. The script navigates to the Ladok portal, authenticates the user, retrieves course codes, then interacts with the TimeEdit public interface to add courses to the selection basket and display the final schedule.

---

## 🚀 Features

- Authenticates users on the Ladok student portal using provided credentials.
- Automatically extracts registered course codes from the Ladok "Current courses" section.
- Navigates to the Chalmers TimeEdit public interface.
- Searches for each extracted course code and adds it to the TimeEdit selection basket.
- Opens the final schedule page for all selected courses.
- Captures a screenshot (`final_result.png`) of the final TimeEdit page for verification.
- Handles errors gracefully with detailed logging for debugging.

---

## 🧑‍💻 Prerequisites

- **Python 3.7 or higher** installed.
- **Google Chrome** browser installed.
- **ChromeDriver** installed (version must match your Chrome browser version; place `chromedriver.exe` in the script's directory or specify its path).
- Python packages:
  - `selenium`: Install via `pip install selenium`.
- A valid **Ladok** account with access to the University of Gothenburg portal.

---
