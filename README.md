# SauceDemo Selenium Python Automation Testing Project

## Project Overview
This project automates the testing of the SauceDemo e-commerce web application using Selenium WebDriver with Python. It validates important functionalities such as login, product selection, adding products to the cart, checkout, and logout.

## Technologies Used
- **Programming Language:** Python
- **Automation Tool:** Selenium WebDriver
- **Testing Framework:** Pytest
- **Locators:** XPath and CSS Selectors
- **IDE:** PyCharm
- **Version Control:** Git and GitHub

## Features Tested
- Login with valid credentials
- Verify product availability
- Add products to the shopping cart
- Verify products in the cart
- Proceed to checkout
- Enter customer information
- Complete the order
- Verify successful order confirmation
- Return to the home page and log out

## Project Structure
```text
SauceDemo-Selenium-Python/
│
├── pages/
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   └── checkout_page.py
│
├── tests/
│   ├── conftest.py
│   └── test_saucedemo.py
│
├── utils/
│   └── config.py
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Prerequisites
- Python installed
- Google Chrome browser
- PyCharm or another Python IDE

## Installation and Setup

**1. Clone the repository**
```bash
git clone https://github.com/magesh0410/SauceDemo-Selenium-Python.git
```

**2. Open the project folder**
```bash
cd SauceDemo-Selenium-Python
```

**3. Install the required packages**
```bash
pip install -r requirements.txt
```

## How to Run the Tests

Run the following command from the project root directory:

```bash
python -m pytest tests -v
```

To display print statements and detailed test output, run:

```bash
python -m pytest tests -v -s
```

## Test Website
https://www.saucedemo.com/

**Demo Login Credentials**
- Username: `standard_user`
- Password: `secret_sauce`

## Learning Outcomes
- Practiced Selenium WebDriver automation using Python.
- Learned to locate web elements using XPath and CSS selectors.
- Practiced the Page Object Model (POM) structure.
- Used Pytest to execute automated test cases.
- Practiced end-to-end e-commerce checkout testing.

## Author
**Magesh V.**

Software Testing | Manual Testing | Selenium Python Automation
