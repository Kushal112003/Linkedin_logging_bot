# LinkedIn Login Automation using Selenium

This Python project automates the LinkedIn login process using Selenium WebDriver. It securely logs in using credentials from a `.env` file, handles captchas, takes a screenshot upon successful login, and logs all activities to a rotating log file using Python’s `logging` module.

---

## 🚀 What We Learned and Improved

### 🔑 Key Concepts Implemented:
- **Selenium WebDriver** – for browser automation
- **Explicit Waits (WebDriverWait + Expected Conditions)** – for reliability
- **Environment Variables (`.env`)** – for secure credential storage
- **Screenshot Capture** – after login verification
- **Rotating Log Files** – using `RotatingFileHandler` for production-grade logging
- **Structured Folder Handling** – for screenshots, drivers, and logs
- **Captcha Handling** – with manual pause
- **Error Handling** – with `try-except-finally`
- **Modular Logging** – using named loggers

---

### 🛠 Improvements Step-by-Step

| Step | Enhancement |
|------|-------------|
| 1️⃣ | Automated login using Selenium with custom credentials |
| 2️⃣ | `.env` file usage to hide sensitive data |
| 3️⃣ | `.env` file presence check + fallback to manual input |
| 4️⃣ | Captcha detection logic (manual handling) |
| 5️⃣ | Screenshot saved on successful login with timestamp |
| 6️⃣ | Auto-creation of `/screenshots` and `/logs` folders |
| 7️⃣ | Log file saved and rotated using `RotatingFileHandler` |
| 8️⃣ | Errors, info, and warnings logged professionally |
| 9️⃣ | Added graceful `driver.quit()` in `finally` block |
| 🔟 | Clean project structure and security best practices |

---

## 🧰 Technologies Used

- Python 3.10+
- Selenium `pip install selenium`
- `python-dotenv` for loading environment variables
- ChromeDriver (compatible with Chrome browser)
- Built-in `logging`, `os`, `datetime`

---

## 🧪 Prerequisites

Before running the script, make sure:

- Python and Google Chrome are installed
- ChromeDriver is placed inside `drivers/chromedriver.exe`
- Required Python packages installed:
  ```bash
  pip install selenium python-dotenv

```bash
 A .env file exists with:
Email=your_email@example.com
Password=your_password
```

## ▶️ How to Run
 #### 1. Clone/download the project folder

#### 2. Open terminal inside the folder


#### 3. Run the script: python linkedin_login_bot.py
If .env is missing, it will ask you to enter email and password manually.
#### On successful login:

- Screenshot saved inside /screenshots/

- Logs saved inside /logs/linkedin_bot.log

# ⚖️ Legal & Ethical Considerations

-  This script does not bypass LinkedIn's captcha or security protocols.
- Use this tool only for educational or personal automation purposes
- Do not use this to scrape or automate actions that violate LinkedIn’s Terms of Service

## 📋 Limitations
- Manual captcha solving

- No 2FA support

- No headless mode

- Only logs in (no post-login activity)

- Credentials are assumed valid

## 🤝 Assumptions
- You have a valid LinkedIn account
- You run this script occasionally
- You understand automation triggers security checks
- You’re running this script from the same directory as .env

# 📄 License
### This project is licensed under the [MIT License](./LICENSE).
#### You are free to use, modify, and distribute this project with credit. It is intended strictly for learning and personal automation purposes.

## ✅ Final Notes

This project is ideal for:
- Beginners learning automation
- Understanding `.env` security handling
- Implementing real-world logging
- Practicing browser interaction & structured Python projects
